# Зчитати ввод від користувача - речення (текст)
# Порахувати кожне слово у реченні,кількість разів воно зустрічається у реченні.
# Порахувати статистику використаних літер. Для зберігання статистик використати словники.

# Підказки:
# * input
# * str.split
# * for word in sequence
# * if key in dict
# * if key not in dict


text_input = input('Type any text')
list_words = text_input.split()

same_words_in_text = {}

for word in list_words:
    count_words = list_words.count(word)
    same_words_in_text[word] = count_words

counter_letter = {}

for i in list_words:
    for j in i:
        if j not in counter_letter:
            counter_letter[j] = 0
        if j in counter_letter:
            counter_letter[j] += 1
