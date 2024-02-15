def copylinefromfile(source_file_path, target_file_path, line_number):
    try:
        with open(source_file_path, 'r', encoding='utf-8') as source_file:
            lines = source_file.readlines()
        if line_number > len(lines) or line_number <= 0:
            print("Номер строки вне диапазона.")
            return False
        with open(target_file_path, 'a', encoding='utf-8') as target_file:
            target_file.write(lines[line_number - 1])
        
        print(f"Строка {line_number} была успешно скопирована из {source_file_path} в {target_file_path}.")
        return True
    except FileNotFoundError:
        print("Один из файлов не найден.")
        return False
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False

# Пользовательский интерфейс для получения входных данных
def main():
    source = input("Введите путь к исходному файлу: ")
    target = input("Введите путь к целевому файлу: ")
    line_num = int(input("Введите номер строки для копирования: "))
    
    copylinefromfile(source, target, line_num)

if __name__ == '__main__':
    main()