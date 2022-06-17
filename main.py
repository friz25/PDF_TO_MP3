from gtts import gTTS #текст в звук (gtts = Google-Text-To-Sound)
from art import tprint #для вывода лого (в терминале)
import pdfplumber #pdf в текст
from pathlib import Path #для работы с путями

import pdfplumber

def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        # return 'Файл найден!'
        print(f'[+] Файл: {Path(file_path).name}')
        print('[+] Обрабатываеться...')
        #Достаём текст из pdf (при помощи pdfplumber)
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
            
        text = ''.join(pages)
        text = text.replace('\n','') #из X строк делаем 1 длинную строку
        #(чтобы избивить от длин.пауз (изза концов строки))
        '''
        with open('text2.txt', 'w') as file:
            file.write(text)
        '''
        #формируем аудио файл
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem #.stem даёт имя файла (без разширения) == "Гарри Поттер"
        #сохраняем файл с именем filename + .mp3
        my_audio.save(f'{file_name}.mp3')
        #проинформ-ем Юзера об успешном создании нашего mp3 файла
        return f'[+] {file_name}.mp3 успешно сохранён!\n---Хорошего вам дня---'
            
    else:
        return 'Файл не найден, проверь путь к файлу!'
    
def main():
    tprint('PDF>>TO>>MP3', font='bulbhead')#выводим наше (красивое) лого (в терминале)
    file_path = input("\nВведите путь к файлу: ")
    language = input("Введите язык, например 'en' или 'ru': ")
    print(pdf_to_mp3(file_path=file_path, language=language))

if __name__ == '__main__':
    main()