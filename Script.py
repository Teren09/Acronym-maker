from itertools import permutations, product, chain


def alpha_check():
    sentence = str.lower(input('Type something in: '))
    while not sentence.replace(' ', '').isalpha():
        print(f"You typed in {sentence}. Only letters A-Z allowed, not case sensitive.")
        sentence = input("Please, type something again: ")
    return sentence


def iterate(sentence):
    whimsical_sentences = [[]]
    my_set = set(line.strip() for line in open('file.txt'))
    word_list = sentence.split()

    for words in word_list:
        permutation = list(permutations(words))
        acronyms = my_set.intersection(["".join(word) for word in permutation])  # finds matches of permuted words in a file
        whimsical_sentences = [s+[word] for s, word in product(whimsical_sentences, acronyms)]

    whimsical_sentences = set(" ".join(fs) for fs in whimsical_sentences)
    yoda_speech = chain(*[permutations(fs.split()) for fs in whimsical_sentences])  # * converts the list items into individual parameters. So each list becomes a parameter to the chain() function.
    yoda_speech = set(" ".join(fs) for fs in yoda_speech)
    for fs in yoda_speech:
        print(fs)


iterate(alpha_check())


def again():
    check = True
    answer = input('One more? Enter yes or no (y/n): ').lower().strip()

    while not (answer == 'n' or answer == 'y' or answer == 'no' or answer == 'yes'):
        print(f'You entered {answer}, please try again.')
        answer = input('Enter yes or no (y/n): ').lower().strip()
    if answer[0] == 'n':
        check = False

    if __name__ == "__main__" and check:
        iterate(alpha_check())
        again()


again()
