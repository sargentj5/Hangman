import random

print("H A N G M A N")
play_or_exit = ""
word_bank = ['python', 'java', 'kotlin', 'javascript']
guess_word = random.choice(word_bank)
attempt_list = []
attempts = 0
while play_or_exit == "":
    play_statement = input('Type "play" to play the game, "exit" to quit: ')
    if play_statement == "exit":
        play_or_exit = "exit"
    elif play_statement == "play":
        while attempts < 8:
            print("")
            for char in guess_word:
                if char in attempt_list and guess_word:
                    print(char, end="")
                else:
                    print("-", end="")
            print("")
            guess = input("Input a letter: ")
            if len(guess) != 1:
                print("You should input a single letter")
            elif not 'a' <= guess <= 'z':
                print("It is not an ASCII lowercase letter")
            elif guess in attempt_list:
                print("You already typed this letter")
            elif guess not in guess_word:
                print("No such letter in the word")
                attempts += 1
            attempt_list.append(guess)

        if guess == guess_word:
            print("You survived!")
        else:
            print("You are hanged!")
    else:
        continue
