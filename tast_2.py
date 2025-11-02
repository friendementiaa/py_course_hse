import re

text = "Контакты: ivan@mail.ru, petr-ivanov@company.com, info@site.org"
# Задача: Найти все email-адреса
# Ожидаемый результат: ['ivan@mail.ru', 'petr-ivanov@company.com', 'info@site.org']

mail_list = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

print(mail_list)