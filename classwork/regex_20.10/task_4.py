import re

text = "Пост в соцсети: #python #machinelearning @username1 @user_name2"
# Задача: Найти все хештеги
# Ожидаемый результат:
# Хештеги: ['#python', '#machinelearning']

hashtags = re.findall(r'#\w+', text)

print(hashtags)