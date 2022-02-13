from collections import defaultdict


def find_word(displaced_letters, incorrect_letters, correct_places):
    found = []
    with open('five_letter_words.txt') as input_file:
        for line in input_file:
            word = line.strip()
            if any(letter not in word for letter in displaced_letters):
                continue
            if any(letter in word for letter in incorrect_letters):
                continue
            if any(word[index] != letter for index, letter in correct_places):
                continue
            found.append(word)
    return found


def create_letter_count(words):
    letter_count = defaultdict(int)
    for word in words:
        for letter in word:
            letter_count[letter] += 1
    return letter_count


def calc_word_score(word, letter_count):
    score = 0
    for letter in set(word):
        score += letter_count[letter]
    return score


if __name__ == '__main__':
    displaced_letters = ['r', 'n', 'i', 'o']
    incorrect_letters = ['c', 'a', 'e', 'h']
    correct_places = [(0, 'r')]
    print('Finding words...')
    found_words = find_word(displaced_letters, incorrect_letters, correct_places)
    print('Creating letter count...')
    letter_count = create_letter_count(found_words)
    print(letter_count)
    words_with_scores = [(word, calc_word_score(word, letter_count)) for word in found_words]
    top_ten = sorted(words_with_scores, key=lambda x: x[1], reverse=True)
    print(top_ten)
