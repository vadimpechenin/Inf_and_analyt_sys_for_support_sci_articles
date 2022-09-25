"""
Чат-бот, по разному реагирующий на вежливое и невежливое приветствия с использованием AIML 1.0
"""

import os
import time
#from nlpia.constants import DATA_PATH
DATA_PATH = "D:\PYTHON\Programms\Inf_and_analyt_sys_for_support_sci_articles"
#pip install AIML-Bot
#time.clock() на time.process_time()
import aiml_bot
bot = aiml_bot.Bot(learn=os.path.join(DATA_PATH, 'greeting_step1.aiml'))
print(bot.respond("Hello Rosa,"))
print(bot.respond("hello !!!troll!!!"))
print(bot.respond("hello troll"))
print(bot.respond("Helo Rosa"))
print(bot.respond("Hello Ro-sa"))

#Улучшение шаблонов
time.sleep(1)
print("Улучшенный шаблона ответов")
bot.learn(os.path.join(DATA_PATH, 'greeting_step2.aiml'))
print(bot.respond("Hey Rosa"))
print(bot.respond("Hi Rosa"))
print(bot.respond("hello **troll** !!!"))
print(bot.respond("Helo Rosa"))

#Дальнейшее улучшение шаблонов. Случайные ответы в одном стиле
time.sleep(1)
print("Дальнейшее улучшение шаблонов. Случайные ответы в одном стиле")
bot.learn(os.path.join(DATA_PATH, 'greeting_step3.aiml'))
print("Hey Rosa")
print(bot.respond("Hey Rosa"))
print("Hey Rosa")
print(bot.respond("Hey Rosa"))
print("Hey Rosa")
print(bot.respond("Hey Rosa"))
print(bot.respond("Hi Rosa"))
print(bot.respond("hello **troll** !!!"))
print(bot.respond("Helo Rosa"))