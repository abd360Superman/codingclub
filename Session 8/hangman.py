#importing modules
from turtle import *
import random

#Making the wordlist, and choosing the word
word_list = ["pizza",
             "pasta",
             "burger",
             "dimsums",
             "sushi",
             "lasagna",
             "fries",
             "bao",
             "rice",
             "noodles"]
word = random.choice(word_list)

#Setting up Turtle
t = Pen()
t.hideturtle()

#Making Functions to draw the Hangman Figure
def twrong1():
    t.up()
    t.backward(150)
    t.left(90)
    t.backward(150)
    t.down()
    t.forward(435)
    t.right(90)
    t.forward(230)
    t.right(45)
    t.forward(130)
    t.right(45)

def twrong2():
    t.up()
    t.backward(3)
    t.right(90)
    t.forward(5)
    t.down()
    t.circle(50)
    
def twrong3():
    t.up()
    t.left(90)
    t.forward(100)
    t.down()
    t.forward(150)

def twrong4():
    t.up()
    t.right(180)
    t.forward(145)
    t.left(150)
    t.down()
    t.forward(115)

def twrong5():
    t.up()
    t.right(180)
    t.forward(115)
    t.right(115)
    t.down()
    t.forward(115)

def twrong6():
    t.up()
    t.right(180)
    t.forward(115)
    t.right(215)
    t.forward(145)
    t.right(35)
    t.down()
    t.forward(120)

def twrong7():
    t.up()
    t.right(180)
    t.forward(120)
    t.right(120)
    t.down()
    t.forward(120)

#Setting the answers up
answerArray = []
for i in range(0, len(word)):
    answerArray.insert(i, "_")
    
#Defining Variables to track the amount of wrongs and letters remaining
wrongs = 0
remLetters = len(word)

#Starting the mainloop - Continuing it until the remaining letters are 0
while remLetters > 0:

    #Printing the word guess uptil now
    stringAnswer = ''
    for j in answerArray:
        stringAnswer = stringAnswer + j
        stringAnswer = stringAnswer + ' '

    print(stringAnswer)

    #Taking the input from the user as their guess
    guess = input("Guess a letter (ALL LOWERCASE): ")

    #Setting up a variable to help in see later if person gets a wrong; Initializing it to the letters remaining
    prevRem = remLetters

    #Seeing if person guessed more or less than one letter
    if len(guess) != 1:
        print('Enter one letter ONLY')
        
    else:
        #Seeing if letter guessed is right
        for l in range(0, len(word)):
            if word[l] == guess:
                answerArray[l] = guess
                remLetters = remLetters - 1

        #If letter was wrong, continuing the Hangman figure - If seventh wrong, then you're out
        if prevRem == remLetters:
            wrongs = wrongs + 1
            if wrongs == 1:
                twrong1()

            elif wrongs == 2:
                twrong2()

            elif wrongs == 3:
                twrong3()

            elif wrongs == 4:
                twrong4()

            elif wrongs == 5:
                twrong5()

            elif wrongs == 6:
                twrong6()

            else:
                twrong7()
                print('You lose')
                print('The correct answer is %s' % (word)) 
                break    
    
#Seeing if players won
if wrongs < 7:
    print('You guessed right! You win!')
