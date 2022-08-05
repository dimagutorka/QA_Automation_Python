text_input = input('Type any text')
list_words = text_input.split()

same_words_in_text = {}
counter_letter = {}

for word in list_words:
    if word not in same_words_in_text:
        count_words = list_words.count(word)
        same_words_in_text[word] = count_words

    for j in word:
        if j not in counter_letter:
            counter_letter[j] = 0
        counter_letter[j] += 1




