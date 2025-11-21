import telebot
# import test
# import time

# test.superpuperfunc()

bot = telebot.TeleBot('8560715077:AAF57e5hL5oXvHD-9hNzA-KOPLbF7wp9eWE')
ADMIN_CHAT_ID = 1318143866
# cute_cat_url = "https://cs12.pikabu.ru/post_img/2022/06/10/6/1654851267120726566.jpg"

# Переменная для хранения chat_id последнего пользователя

data_id = set()
# i = 1
# while i > 0:
#     bot.send_photo(1318143866, cute_cat_url)
#     time.sleep(2)

# Приветствие
@bot.message_handler(commands=['start'])
def start_cmd(message):
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name or ""
    full_name = f"{first_name} {last_name}".strip()
    bot.send_message(message.chat.id, f"Привет, {full_name}!")
    # bot.send_photo(message.chat.id, cute_cat_url)
    data_id.add(str(message.chat.id))
    # i = 1
    # while i > 0:
    #     bot.send_photo(message.chat.id, cute_cat_url)
    #     time.sleep(2)
        
    print("Запись в базу данных",data_id)
    


# Обработчик сообщений от пользователей
@bot.message_handler(func=lambda m: m.chat.id != ADMIN_CHAT_ID)
def forward_to_admin(message):
    global last_user_id
    user = message.from_user
    full_name = f"{user.first_name} {user.last_name or ''}".strip()

    # Пересылаем сообщение админу
    bot.forward_message(ADMIN_CHAT_ID, message.chat.id, message.message_id)

    # Сохраняем chat_id последнего пользователя
    last_user_id = message.chat.id

    # Отправляем админу текст с именем пользователя
    bot.send_message(ADMIN_CHAT_ID, f"Сообщение от {message.chat.id}:")

# Обработчик сообщений от админа
@bot.message_handler(func=lambda m: m.chat.id == ADMIN_CHAT_ID)
def admin_reply(message):
    format_ans_bot = message.text.split()
    del format_ans_bot[0]
    format_ans_bot = ' '.join(format_ans_bot)
    
    user_id_string = message.text
    user_id = user_id_string.split()
    user_id = user_id[0]
    bull = user_id.isdigit()
    if user_id not in data_id:
        bot.send_message(ADMIN_CHAT_ID, f"Нет такого пользователя или не правильно ввел ID")
        return
    
    if bull is not True:
        return
 
    if user_id is not None:
        bot.send_message(user_id, f"{format_ans_bot}")
    else:
        bot.send_message(ADMIN_CHAT_ID, "Нет пользователя для ответа.")
        
    
    print("Вроде удалили первый элем", format_ans_bot)
    print("Ищем текс",message.text)

bot.polling(non_stop=True)


