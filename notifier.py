import requests


def send_telegram_notification(message, bot_token, chat_id):
    """
    Sends a notification to a Telegram chat.
    
    :param message: The message to send
    :param bot_token: The bot's API token
    :param chat_id: The chat ID where the message will be sent
    """
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message,
    }
    response = requests.post(url, data=payload)
    return response.json()


# Example usage:
# send_telegram_notification('Hello, this is a test message!', 'YOUR_BOT_TOKEN', 'YOUR_CHAT_ID')
