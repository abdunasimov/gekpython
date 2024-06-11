import os

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for idx, line in enumerate(lines):
                print(f"{idx + 1}: {line.strip()}")
            return lines
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return []

def write_to_file(filename, line):
    with open(filename, 'a') as file:
        file.write(line + '\n')
    print(f"Строка добавлена в файл {filename}.")

def copy_line(source_file, target_file, line_number):
    lines = read_file(source_file)
    if lines and 1 <= line_number <= len(lines):
        line_to_copy = lines[line_number - 1].strip()
        write_to_file(target_file, line_to_copy)
    else:
        print("Некорректный номер строки.")

def main():
    source_file = input("Введите имя исходного файла: ")
    target_file = input("Введите имя целевого файла: ")

    if not os.path.isfile(source_file):
        print(f"Исходный файл {source_file} не существует.")
        return
    
    read_file(source_file)
    
    try:
        line_number = int(input("Введите номер строки для копирования: "))
        copy_line(source_file, target_file, line_number)
    except ValueError:
        print("Введите корректное число.")

if __name__ == "__main__":
    main()
