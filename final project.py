import telebot
from telebot import types

bot = telebot.TeleBot('6965356607:AAF2vz5XTsPdbthkd9CNTXY8DykCKda_5fA')


@bot.message_handler(commands=["start"])
def start(msg):
    key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Go shopping")
    key.add(btn1)
    bot.send_message(msg.chat.id, "teatime is a new brand for young people based in Moscow, Russia\nWorldwide shipping "
                                  "is available! This brand is mostly liked by universities students"
                                  "because it has a dar academia vibe which is quite popular nowadays."
                     , reply_markup=key)

@bot.message_handler(content_types=["text"])
def main(msg):
    if msg.text == "Go shopping":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("shoe")
        btn2 = types.KeyboardButton("trouses")
        btn3 = types.KeyboardButton("shirt")
        btn4 = types.KeyboardButton("coat")
        btn5 = types.KeyboardButton("dress")
        key.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(msg.chat.id, "Choose a category", reply_markup=key)
    if msg.text == "shoe":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("shoe for men")
        btn2 = types.KeyboardButton("shoe for women")
        btn3 = types.KeyboardButton("shoe for women2")
        btn4 = types.KeyboardButton("Go back")
        key.add(btn1, btn2, btn3, btn4)
        bot.send_message(msg.chat.id, "Choose your preference", reply_markup=key)
    if msg.text == "trouses":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("trouses for men")
        btn2 = types.KeyboardButton("shorts")
        btn3 = types.KeyboardButton("skirt")
        btn4 = types.KeyboardButton("Go back")
        key.add(btn1, btn2, btn3, btn4)
        bot.send_message(msg.chat.id, "Choose your preference", reply_markup=key)
    if msg.text == "shirt":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("shirt for women")
        btn2 = types.KeyboardButton("sweater for men")
        btn3 = types.KeyboardButton("cardigan for men")
        btn4 = types.KeyboardButton("cardigan for women")
        btn5 = types.KeyboardButton("Go back")
        key.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(msg.chat.id, "Choose your preference", reply_markup=key)
    if msg.text == "coat":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("coat for men")
        btn2 = types.KeyboardButton("coat for women")
        btn3 = types.KeyboardButton("Go back")
        key.add(btn1, btn2, btn3, )
        bot.send_message(msg.chat.id, "Choose your preference", reply_markup=key)
    if msg.text == "dress":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("dress")
        btn2 = types.KeyboardButton("suit for women")
        btn3 = types.KeyboardButton("suit for men")
        btn4 = types.KeyboardButton("Go back")
        key.add(btn1, btn2, btn3, btn4)
        bot.send_message(msg.chat.id, "Choose your preference", reply_markup=key)
    if msg.text == "Go back":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("shoe")
        btn2 = types.KeyboardButton("trouses")
        btn3 = types.KeyboardButton("shirt")
        btn4 = types.KeyboardButton("coat")
        btn5 = types.KeyboardButton("dress")
        key.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(msg.chat.id, "Choose a category", reply_markup=key)
    if msg.text == "shoe for men":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/men shoes.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 540 dollars", reply_markup=key)
    if msg.text == "shoe for women":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/shoes w.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 400 dollars", reply_markup=key)
    if msg.text == "shoe for women 2":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/shoes w 2.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 350 dollars", reply_markup=key)
    if msg.text == "trouses for men":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/men trouses.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 250 dollars", reply_markup=key)
    if msg.text == "shorts":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/shorts.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 450 dollars", reply_markup=key)
    if msg.text == "skirt":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/skirt.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 200 dollars", reply_markup=key)
    if msg.text == "shirt for women":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/shirt w.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 320 dollars", reply_markup=key)
    if msg.text == "sweater for men":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/sweater m.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 450 dollars", reply_markup=key)
    if msg.text == "cardigan for men":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/cardigan men.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 300 dollars", reply_markup=key)
    if msg.text == "cardigan for women":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/cardigan.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 250 dollars", reply_markup=key)
    if msg.text == "coat for men":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/coat m.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 1000 dollars", reply_markup=key)
    if msg.text == "coat for women":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/coat w.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 1200 dollars", reply_markup=key)
    if msg.text == "dress":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/dress.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 700 dollars", reply_markup=key)
    if msg.text == "suit for women":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/suit w.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 1590 dollars", reply_markup=key)
    if msg.text == "suit for men":
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Go back")
        key.add(btn1)
        img = open("pics/suit.jpg", "rb")
        bot.send_photo(msg.chat.id, img, caption="The price is 2000 dollars", reply_markup=key)

bot.polling(non_stop=True)