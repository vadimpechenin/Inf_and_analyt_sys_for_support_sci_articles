"""
Простой чат бот из главы 1.4.3
Использование шаблонов приветствия

наши машины будут взаимодей- ствовать с людьми, которые говорят что-то вроде «Доброе утро, Роза».
Мы не хотим, чтобы чат-бот издавал какое-нибудь чириканье или писк либо отправлял сообще- ния ACK,
как это происходит при синхронизации модема или HTTP-соединении в начале разговора/сеанса просмотра веб-страниц.
Вместо этого подойдут регулярные выражения для распознавания нескольких различных приветствий в начале установления
 связи при разговоре:

Необходимо в предложении упомянуть 'Hello Rosa', например 'Hello Rosa, how is it going?'
"""

#В Python есть два "официальных" пакета регулярных выражений. Мы используем пакет re здесь только потому,
#что он устанавливается вместе со всеми версиями Python. Пакет regex посталяется только с последними версиями Python,
# и он гораздо мощнее


import re

r = "(hi|hello|hey)[ ]*([a-z]*)"

#Игнорирование регистра символов - довольно распространенная техника.
# Это упрощает регулярные выражения
re.match(r, 'Hello Rosa', flags = re.IGNORECASE)
re.match(r, "hi ho, hi ho, it's off to work ...", flags = re.IGNORECASE)
re.match(r, "hey, what's up", flags = re.IGNORECASE)

#Детализируем наше регулярное выражение, чтобы ему соответствовало большее количество приветствий
r = r"[^a-z]*([y]o|[h']?ello|ok|hey|(good[ ])&(morn[gin']{0,3}|"\
    r"afternoon|even[gin']{0,3}))[\s,;:]{1,3}([a-z]{1,20})"
#Регулярные выражения можно скомпилировать, чтобы не указывать параметры (флаги) при каждом использовании
re_greeting = re.compile(r, flags = re.IGNORECASE)
re_greeting.match('Hello Rosa')
re_greeting.match('Hello Rosa').groups()
re_greeting.match("Good morning Rosa")
re_greeting.match("Good Manning Rosa") #Это регулярное выражение не может распознать (найти соотвествтие) слова с опечатками

#Наш чат-бот может разделять различные части приветствия на группы,
# но он не будет знать об известной фамилии Розы, так как у нас нет паттерна для сопоставления каких-либо символов после имени
#re_greeting.match('Good evening Rosa Parks').groups()
re_greeting.match("Good morning Rosa")
re_greeting.match("Good Morn'n Rosa")
re_greeting.match("yo Rosa")


#Генератор входных даных. Бот должен что-то сказать.
my_names = set(['rosa', 'rose', 'chatty', 'chatbot', 'bot', 'chattetbot'])
curt_names = set(['hal', 'you', 'u'])
greeter_name = ''
numb1=1
while (1==numb1):
    match = re_greeting.match(input())
    if match:
        at_name = match.groups()[-1]
        if at_name in curt_names:
            print("Good one.")
        elif at_name.lower() in my_names:
            print("Hi {}, How are you?".format(greeter_name))

    numb1 = int(input("Выйти (0) или остаться (1)?: "))

