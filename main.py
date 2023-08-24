import random
import string


count = int(input("Сколько паролей желаете сгенерировать? "))
password_length = int(input("Введите нужное количество символов для пароля: "))

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

passwords_list = [generate_password(password_length) for _ in range(count)]
passwords = ' '.join(passwords_list)

with open("passwords.txt", "w") as file:
    for password in passwords.split():
        file.writelines(password + '\n')

print("Пароли сохранены в файл passwords.txt")