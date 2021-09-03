import random
import string
from words_02 import words
from hangman_visual import lives_visual_dict

# words = ['ace', 'ava', 'batman']


def get_valid_word(words):
    word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet0 = set(string.ascii_uppercase)
    used_letters = set()  # that user has guessed

    lives = 7

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a','b','cd']) -- 'a ,b, cd'
        print(
            f'You have {lives} lives left and You have used this letters: {used_letters}')

        # what current word is (ie W - R D)
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])

        print(f'current word: {word_list}')

        user_letter = input('Guess letter: ').upper()
        if user_letter in alphabet0 - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('--------------------------\tgood')
            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('you have already used that character.please try again.')

        else:
            print('invalid input. try again')

        # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print(lives)
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed right the word is', word, '!!')


if __name__ == '__main__':
    hangman()
