from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.errors import AuthKeyDuplicatedError
import asyncio
import logging
import os
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
SESSION_STRING = os.environ["SESSION_STRING"]

EARNKARO_BOT = "ekconverter10bot"

SOURCE_CHANNELS = [
    "@dipayantech_kk",
    
    ]

FORWARD_DELAY = 15
seen_posts = set()

def is_duplicate(text):
    fingerprint = text[:80].strip() if text else ""
    if fingerprint in seen_posts:
        return True
    seen_posts.add(fingerprint)
    return False

async def main():
    try:
        client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
        await client.start()
        logger.info("✅ Client started successfully.")

        bot_entity = await client.get_entity(EARNKARO_BOT)
        logger.info("✅ EarnKaro bot found.")

        @client.on(events.NewMessage(chats=SOURCE_CHANNELS))
        async def handler(event):
            try:
                msg = event.message
                text = msg.text or msg.caption or ""

                if is_duplicate(text):
                    logger.info("Skipped: duplicate.")
                    return

                await asyncio.sleep(FORWARD_DELAY)
                await client.forward_messages(bot_entity, msg)
                logger.info(f"✅ Forwarded from {event.chat.title}")

            except Exception as e:
                logger.error(f"Handler error: {e}")

        logger.info(f"👀 Monitoring {len(SOURCE_CHANNELS)} channels...")
        await client.run_until_disconnected()

    except AuthKeyDuplicatedError:
        logger.error("❌ Session conflict detected. Exiting cleanly.")
        logger.error("Fix: Terminate all Telegram sessions except phone, regenerate session string.")
        sys.exit(1)

    except Exception as e:
        logger.error(f"❌ Unexpected error: {e}")
        sys.exit(1)

asyncio.run(main())