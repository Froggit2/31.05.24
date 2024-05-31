import os
import time

directory = 'C:\\Users\\User\\Piton\\File\\7_module'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file) #2
        filetime = os.path.getmtime(filepath)   #3
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))  #3
        filesize = os.path.getsize(filepath) #4 размер файла
        parent_dir = os.path.dirname(filepath)  #5 папка до текущей
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
              f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
