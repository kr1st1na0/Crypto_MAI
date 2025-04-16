import os
import random
import string
import requests

def random_letters_text_generator(filename, n):
    random_string = ''
    while len(random_string) < n:
        len_string = random.randint(3, 10)
        str = ''.join(random.choice(string.ascii_letters) for _ in range(len_string))
        random_string += str + ' '
    tmp = len(random_string) - n
    if tmp != 0:
        random_string = random_string[:-tmp] 
    with open(filename, 'w') as file:
        file.write(random_string)

def random_words_text_generator(filename, n):
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"
    response = requests.get(url)
    random_words = response.text.splitlines()
    
    random_words = [word.strip() for word in random_words if len(word.strip()) > 2]
    
    generated_text = ''
    while len(generated_text) < n:
        generated_text += random.choice(random_words) + ' '
    tmp = len(generated_text) - n
    if tmp != 0:
        generated_text = generated_text[:-tmp]
    with open(filename, 'w') as f:
        f.write(generated_text)

def compare(file1, file2, n):
    with open(file1) as file1, open(file2) as file2:
        text1 = file1.read()
        text2 = file2.read()

        text1 = text1[:n]
        text2 = text2[:n]

        count = 0
        for symbol1, symbol2 in zip(text1, text2):
            if symbol1 == symbol2:
                count += 1
        return count / n

def case1(text1, text2, n):
    res = compare(text1, text2, n)
    print('1. Два осмысленных текста на естественном языке'.ljust(50), f'Длина: {n}'.ljust(20), f'Доля совпадений: {res:.5f}')

def case2(text, n):
    text_letters = 'generated_letters.txt'
    random_letters_text_generator(text_letters, n)
    res = compare(text, text_letters, n)
    print('2. Осмысленный текст и текст из случайных букв'.ljust(50), f'Длина: {n}'.ljust(20), f'Доля совпадений: {res:.5f}')
    os.remove(text_letters)

def case3(text, n):
    text_words = 'generated_words.txt'
    random_words_text_generator(text_words, n)
    res = compare(text, text_words, n)
    print('3. Осмысленный текст и текст из случайных слов'.ljust(50), f'Длина: {n}'.ljust(20), f'Доля совпадений: {res:.5f}')
    os.remove(text_words)

def case4(n):
    text_letters1 = 'generated_letters1.txt'
    text_letters2 = 'generated_letters2.txt'
    random_letters_text_generator(text_letters1, n)
    random_letters_text_generator(text_letters2, n)
    res = compare(text_letters1, text_letters2, n)
    print(f'4. Два текста из случайных букв'.ljust(50), f'Длина: {n}'.ljust(20), f'Доля совпадений: {res:.5f}')
    os.remove(text_letters1)
    os.remove(text_letters2)

def case5(n):
    text_words1 = 'generated_words1.txt'
    text_words2 = 'generated_words2.txt'
    random_words_text_generator(text_words1, n)
    random_words_text_generator(text_words2, n)
    res = compare(text_words1, text_words2, n)
    print(f'5. Два текста из случайных слов'.ljust(50), f'Длина: {n}'.ljust(20), f'Доля совпадений: {res:.5f}', end='\n\n')
    os.remove(text_words1)
    os.remove(text_words2)

def main():
    text1 = '1984.txt'
    text2 = 'Fahrenheit451.txt'

    for n in [500, 1000, 5000, 10000, 50000]:
        case1(text1, text2, n)
        case2(text1, n)
        case3(text1, n)
        case4(n)
        case5(n)

if __name__ == '__main__':
    main()