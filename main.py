import os
import sys
from datetime import datetime

# Путь к файлу hosts в зависимости от операционной системы
if os.name == 'nt':
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:
    hosts_path = "/etc/hosts"

redirect = "127.0.0.1"

website_list = ["www.ya.ru", "ya.ru"]

def block_websites():
    try:
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website not in content:
                    file.write(f"{redirect} {website}\n")
        print("Сайты успешно заблокированы.")
    except PermissionError:
        print("Ошибка: Необходимы административные права для изменения файла hosts.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def unblock_websites():
    try:
        with open(hosts_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Сайты успешно разблокированы.")
    except PermissionError:
        print("Ошибка: Необходимы административные права для изменения файла hosts.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def display_menu():
    print("=== Меню блокировки сайтов ===")
    print("1. Заблокировать сайты")
    print("2. Разблокировать сайты")
    print("3. Выйти")

def main():
    while True:
        display_menu()
        choice = input("Выберите опцию (1/2/3): ")
        if choice == '1':
            block_websites()
        elif choice == '2':
            unblock_websites()
        elif choice == '3':
            print("Выход из программы.")
            sys.exit()
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
