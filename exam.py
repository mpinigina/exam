import re
import os

def read_text() :
    global text
    file = open("экзамен.txt", "r", encoding = "utf-8")
    text = file.read()
    text = ". " + text + "."
    text = text.replace("\n", ". ")
    file.close()

def task1() :
    global text
    names = re.findall("[^А-ЯЁ]([А-ЯЁ]\. ?[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?)", text)
    names.sort() #так красивее
    for name in names :
        print(name)

def task2() :
    global text
    global all_names
    all_names = re.findall("((?:(?:[А-ЯЁ]\. ?){1,2}|[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)? )[А-ЯЁ][а-яё]+(?:-[А-ЯЁ][а-яё]+)?)[^А-ЯЁа-яё]", text)
    all_names.sort() #так красивее
    for name in all_names :
        print(name)

def task3() :
    global text
    for name in all_names :
        # поиск первого пробела с конца
        space_index = name.rfind(" ")
        dot_index = name.rfind(".")
        divider_index = max(space_index, dot_index)
        last_name = name[divider_index + 1:]
        # создание папки с именем last_name. exist_ok = True значит, что если папка уже существует, то программа не будет вылетать
        os.makedirs(last_name, exist_ok = True)
        file = open(last_name + "/" + name + ".txt", "w", encoding = "utf-8")
        regex = "[.?!…] ([^.]*?" + name.replace(".", "\.") + "[^.]*?[.?!…])"
        sentences = re.findall(regex, text)
        sentences_string = ""
        for sentence in sentences :
            sentences_string += sentence + "\n"
        file.write(sentences_string)
        file.close()

def main() :
    read_text()
    task1()
    task2()
    task3()

text = ""
all_names = []
main()
