import re

text = "Пост в соцсети: #python #machinelearning @username1 @user_name2"
# Задача: Найти все упоминания
# Ожидаемый результат:
# Упоминания: ['@username1', '@user_name2']

print(re.findall(r'@\w+', text))