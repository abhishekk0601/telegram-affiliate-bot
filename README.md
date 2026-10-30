# Telegram Affiliate Marketing Automation Bot

A 24/7 automated affiliate marketing system built with Python and Telethon.

## How it works
1. Monitors multiple Telegram deal channels in real time
2. Forwards new posts to the EarnKaro converter bot
3. The bot converts product links into my affiliate links
4. The converted post is published to my public Telegram channel

## Tech Stack
- Python 3.11
- Telethon (Telegram MTProto API)
- Asyncio
- Railway (cloud hosting)

## Features
- Real-time monitoring of multiple channels
- Duplicate post filtering
- Delay between forwards to avoid account restrictions
- Credentials stored as environment variables, never in code
- Runs 24/7 on Railway

## Setup
1. Get `API_ID` and `API_HASH` from my.telegram.org
2. Run `get_session_string.py` once to generate a session string
3. Set `API_ID`, `API_HASH`, and `SESSION_STRING` as environment variables
4. Deploy with `python affiliate_forwarder.py`

## Author
Abhishek Kumar, BCA student, Kanpur
