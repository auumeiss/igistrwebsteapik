#Подсчет слов со строчной буквы

#Задание 3. Не использовать регулярные выражения. В соответствии с заданием своего
# варианта составить программу для анализа текста, вводимого с клавиатуры.

#В строке, вводимой с клавиатуры, подсчитать количество слов,
#начинающихся со строчной буквы
def count_lowercase_start_words(text):
    # Разделение текста на слова
    words = text.split()

    # Подсчет количества слов, начинающихся со строчной буквы
    count = 0
    for word in words:
        if word and word[0].islower():
            count += 1
    return count


def lowercase_start_words_counter(func):
    def wrapper():
        # Ввод текста с клавиатуры
        text = input("Введите текст: ")
        # Подсчет слов, начинающихся со строчной буквы
        lowercase_start_words_count = func(text)
        # Вывод результата
        print(f"Количество слов, начинающихся со строчной буквы: {lowercase_start_words_count}")
    return wrapper
@lowercase_start_words_counter
def lab3(text):
    return count_lowercase_start_words(text)