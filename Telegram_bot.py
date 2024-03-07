
import telebot
from telebot import types
bot = telebot.TeleBot("6985475314:AAHSrC520hzSQWz8SWvL1wpGH_ZKnvDfnQA")

def get_data():
    filee = open("output.txt", "r")
    data = filee.read()
    data = data.split("\n")
    filee.close()
    return data

def get_company_codes():
    data = get_data()
    company_codes = []
    for i in data:
        if i != "":
            company_codes.append(i.split(",")[0].split('"')[1].strip())
    data = list(set(company_codes))
    data = sorted(data)
    print(data)
    return data

def get_company_data(company_code):
    data = get_data()
    company_data = []
    for i in data:
        if i != "":
            if i.split(",")[0].split('"')[1].strip() == company_code:
                company_data.append(i)
    return company_data[0]

def message_formatter(data):
    #"SYMBOL" "COMPANY NAME" "SUBJECT" "DETAILS" "BROADCAST DATE/TIME" "RECEIPT" "DISSEMINATION" "DIFFERENCE" "ATTACHMENT"
    data = data.split(",")
    SYMBOL = data[0].split('"')[1].strip()
    COMPANY_NAME = data[1].split('"')[1].strip()
    SUBJECT = data[2].split('"')[1].strip()
    DETAILS = data[3].split('"')[1].strip()
    BROADCAST_TIME = data[4].split('"')[1].strip()
    RECEIPT = data[5].split('"')[1].strip()
    DISSEMINATION = data[6].split('"')[1].strip()
    DIFFERENCE = data[7].split('"')[1].strip()
    ATTACHMENT = data[8].split('"')[1].strip()
    return f"SYMBOL: {SYMBOL}\nCOMPANY NAME: {COMPANY_NAME}\nSUBJECT: {SUBJECT}\nDETAILS: {DETAILS}\nBROADCAST TIME: {BROADCAST_TIME}\nRECEIPT: {RECEIPT}\nDISSEMINATION: {DISSEMINATION}\nDIFFERENCE: {DIFFERENCE}\nATTACHMENT: {ATTACHMENT}"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 1
    itembtn1 = types.InlineKeyboardButton("Get all data", callback_data="all data")
    itembtn2 = types.InlineKeyboardButton("Get specific data", callback_data="check")
    markup.add(itembtn1, itembtn2)
    bot.reply_to(message, "Get corporate fillings", reply_markup=markup)

@bot.callback_query_handler(lambda query: query.data.split()[0] == "getdata")
def needb(query):
    print("getdata", query.data.split()[1])
    company_data = get_company_data(query.data.split()[1])
    bot.send_message(query.message.chat.id, message_formatter(company_data))

@bot.callback_query_handler(lambda query: query.data.split()[0] == "giveb")
def giveb(query):
    pass

@bot.message_handler(commands=['need'])
def need_entry(message):
    pass

@bot.message_handler(commands=['give'])
def give_entry(message):
    pass

@bot.callback_query_handler(lambda query: query.data.split()[0] == "all")
def process_callback_enter(query):
    print("all data")
    markup = types.InlineKeyboardMarkup()
    markup.row_width = 3
    buttons = []
    company_codes = get_company_codes()
    for i in company_codes:
        if i != "":
            buttons.append(types.InlineKeyboardButton(i, callback_data="getdata "+i))
    markup.add(*buttons)
    bot.send_message(query.message.chat.id, "Select a company code", reply_markup=markup)

@bot.callback_query_handler(lambda query: query.data == "check")
def process_callback_check(query):
    print("check")
    bot.send_message(query.message.chat.id, "check")

#while 2>1:
try:
    bot.polling()
except Exception as e:
    print("error in polling"+str(e))