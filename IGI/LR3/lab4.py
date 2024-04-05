from typing import List

#Задание 4. Не использовать регулярные выражения. Дана строка текста, в
# которой слова разделены пробелами и запятыми.
# В соответствии с заданием своего варианта составьте программу для
# анализа строки, инициализированной в коде программы:

#а) определить количество слов в строке;
#б) найти самое длинное слово и его порядковый номер;
#в) вывести каждое нечетное слово


def count_words(text):
    words = text.split()
    return len(words)

def find_longest_word(text):
    words = text.split()
    # Находим самое длинное слово и его индекс
    longest_word = max(words, key=len)
    index = words.index(longest_word) + 1

    return longest_word, index

def print_odd_words(text):
    words = text.split()
    wordslist=[]
    # Выводим каждое нечетное слово
    print("Нечетные слова:")
    k=0
    for i in range(len(words)):
            if i % 2 == 0:
                wordslist.append(words[i])
                k+=1
    print (wordslist)

def lab4():
    # Инициализация строки текста
    text = "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    print(text)
    text = text.replace(',', '')
    text = text.replace('.', '')
    # Определение количества слов в строке
    words_count = count_words(text)
    print(text)
    print("Количество слов в строке:", words_count)

    # Находим самое длинное слово и его порядковый номер
    longest_word, index = find_longest_word(text)
    print("Самое длинное слово:", longest_word)
    print("Порядковый номер самого длинного слова:", index)

    # Выводим каждое нечетное слово
    print_odd_words(text)

