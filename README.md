
# Gupshup ↔ Telegram Bridge

### Description
This simple Python Flask app bridges Gupshup WhatsApp messages to a Telegram bot and allows replying from Telegram using a message format like:

```
PHONE_NUMBER:: message
```

### Deploy on Render

1. Fork this repo to your GitHub account.
2. Connect your GitHub to Render and select this repo.
3. Add the following environment variables in Render:
   - `GUPSHUP_API_KEY`
   - `GUPSHUP_APP_NAME`
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`

4. Set Gupshup webhook URL to `https://your-render-url/gupshup-webhook`
5. Set Telegram webhook URL to `https://your-render-url/telegram-webhook`
