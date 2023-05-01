import tkinter as tk
import random, time

# Word List
words_list = [ "computer", "programming", "vacation", "sandwich", "kangaroo", "elephant", "xylophone", "microphone", "astronaut", "basketball"]
wrong_guess_count = 0

# Main GUI
root = tk.Tk()
root.title("Hangman Game")

# Unknown Word
def getRandomWord():
    global random_word
    random_word = random.choice(words_list).upper()
    print(random_word)
    print(len(random_word))
    return random_word

dashes_label = tk.Label(root, text="- "*len(getRandomWord()), justify="center")
dashes_label.grid(row=0, column=1, columnspan=2)

# Guess Entry
guess_label = tk.Label(root, text="Guess a Letter :")
guess_entry = tk.Entry(root)
guess_label.grid(row=1, column=1)
guess_entry.grid(row=1, column=2)

# Wrong Guesses
wrong_guess_label = tk.Label(root, text="Wrong Guesses :")
wrong_guess = tk.Label(root, text="6")
wrong_guess_label.grid(row=2, column=1)
wrong_guess.grid(row=2, column=2)

# Game Logic
def submit():
    revealed_word = ""
    letter = guess_entry.get().upper()
    current_word = dashes_label.cget("text").split()
    if letter != "":
        if letter in random_word:
            for i in range(len(random_word)):
                if random_word[i] == letter:
                    current_word[i] = letter
            revealed_word = " ".join(current_word)
            if revealed_word.replace(" ", "") == random_word:
                results = tk.Label(root, text="You Win!")
                results.grid(row=3, column=1, columnspan=3)
            dashes_label.config(text=revealed_word)
        else:
            wrong_guess_count = int(wrong_guess.cget("text"))
            wrong_guess_count -= 1
            wrong_guess.config(text=str(wrong_guess_count))
            if wrong_guess_count == 0:
                results = tk.Label(root, text="You Lose!")
                results.grid(row=3, column=1, columnspan=3)
        
        guess_entry.delete(0, tk.END)


submit_button = tk.Button(root, text="Submit" ,command=lambda: submit())
submit_button.grid(row=1, column=3)

root.mainloop()