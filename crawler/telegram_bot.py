import telegram

bot = telegram.Bot(token = '999630453:AAGjO2fijWMeWmCYMt6kFw5-C6IKJ8UINtY')

#for i in bot.getUpdates() :
#    print(i.message)
#

bot.sendMessage(chat_id=967963705, text="테스트입니다.")
