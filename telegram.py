import requests

# Укажите ваш токен бота
bot_token = 'YOUR_BOT_TOKEN'

# Укажите ID чата или пользователя, которому вы хотите отправить сообщение
chat_id = 'CHAT_OR_USER_ID'

# Текст сообщения для отправки
message = 'Hello, Telegram!'

# Формирование URL для отправки запроса
url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

# Параметры запроса
params = {
    'chat_id': chat_id,
    'text': message
}

# Отправка запроса
response = requests.post(url, params=params)

# Проверка статуса ответа
if response.status_code == 200:
    print('Сообщение успешно отправлено!')
else:
    print('Произошла ошибка при отправке сообщения.')
