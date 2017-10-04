###hangman.py
##Hangman game is based on guessing what is the hidden word in limited number of tries
##In this version the number of tries is 6 , So you must guess the correct letters
##That form the hidden word in 6 tries or less
##There is an option that you guess the whole word , but if it was wrong ,It will cost you 2 tries


#libraries used
from string import *
from random import randrange
from hangman_lib import *

#choosing the category from which the hidden word will be chosen
def topic_file(topic):
    file = open(topic+'.txt','r')
    lines = file.readlines()
    return choose_word(lines)

def choose_word(words):
    return words[randrange(0,len(words))].strip()   #strip() to remove spaces after words


#gloabl variables should be here to use in the functions below
max_tries = 6
all_guesses = []
hidden_word = ''
mistakes = 0

#printing the available letters
def available_letters():
    global all_guesses
    all_alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in all_guesses:
            all_alphabets.remove(i)
    return join(all_alphabets,sep=' ')  #To show them without braces

#printing the letters geussed till now
def current_guesses():
    global hidden_word
    global all_guesses
    current_word = list('-'*len(hidden_word))
    for i in range(len(hidden_word)):
        if hidden_word[i] in all_guesses:
            current_word[i]=hidden_word[i]
    if '-' not in current_word:     #if there is no '-' thats means i have figured it all
        return hidden_word
    else:
        return current_word
#check if i got it in word guess
#TRUE will terminate the game
#False will continue
def one_shot(word):
    global hidden_word
    global mistakes
    if word == hidden_word:
        print "GOTCHA"
        return True
    else:
        mistakes +=2 #special penalty
        return False
#check my letter if its right , wrong or even chosen before
#TRUE will terminate the game
#False will continue
def guess_checker(letter):
    global hidden_word
    global all_guesses
    global mistakes
    if letter in all_guesses:
        print "You have guessed this before"
        return False
    all_guesses.append(letter)
    if letter not in hidden_word:
        mistakes+=1
        return False
    elif current_guesses()==hidden_word:
        return True
#main
def play():
    global hidden_word
    global all_guesses
    global mistakes
    print "Please ,Choose a topic"
    print "Sports,Animals,Countries or Random"
    hidden_word=lower(topic_file(lower(raw_input()))).replace(" ","") #lower() to turn all letters to lowercase
                                                #replace() to remove all spaces if the word splitted in two parts
    mistakes = 0
    letters_guessed = list()
    while mistakes < max_tries:
        print
        print_hangman_image(mistakes)
        print
        print available_letters()
        print
        print join(current_guesses(),sep=' ')
        print
        print 'You have %i guesses remaining'%(max_tries-mistakes)
        guess=lower(raw_input("Guess a letter , or the whole word(costs 2 tries)"))
        if len(guess)>1:
            if one_shot(guess):
                return None
        else:
            if guess_checker(guess):
                print hidden_word
                return None
    print
    print_hangman_image(mistakes)
    print
    print "GAME OVER"
    print hidden_word
    return None

play()
