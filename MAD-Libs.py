
#solution


"""
Mad Libs (a play on ad lib, from Latin ad libitum - as you wish) is a word game where one player prompts another for
a list of words to substitute for blanks in a story; these word substitutions have a humorous effect when the resulting
story is then read aloud.

Create your own MAD LIBS!
Join in on the hilarious fun and write a MAD LIB of your own by following the steps below:

    1. Write a story that is 6-8 sentences long.
    2. Highlight a few of the key words in the story.
    3. Determine what part of speech those words are (noun, pronoun, verb, adjective, etc.).
    4. Remove those words from the story and leave a numbered blank space for write-ins.
    5. Create a key with the number and part of speech on a separate sheet of paper.
    6. Do a test run to make sure your story works.
    7. Share with your friends and family to see what nonsensical stories they come up with!

"""

## Mabage packages
##################################
## gtts
## playsound
##################################

from gtts import gTTS
import os
import time
from playsound import playsound


#Display Title
########################################
print("LETS play MAD-Libs")


#Gather list of words from  player
########################################

# Word One
# Proper Noun (Person’s Name)
name = input("Give me a boy's name :")

# Word Two
# Adjective
adjective = input("Give me a adjective :")

# Word Two
# Adjective
job =input("Name a kind of job :")


# Word ...
# Adjective
item =input("Random item :")

# Word ...
# Adjective
animal =input("Name animal :")


# Word ...
# Adjective
cost= input("Give me a cost :")


# Word ...
# Adjective
colour= input("next I would like a colour :")

########################################
 
#Print story with random words.
########################################

#Declare a string variable called paragraph to hold our sentences. 
paragraph= ""

#Concatenate (Add) sentences to our paragraph.
# -------------------------------------------- #

#Sentences One
# Uses the play's adjective and name.
paragraph += f"Once upon a time, there was a {adjective} man named {name}."

#Sentences Two
# Uses the play's {},{} and {}. 
paragraph+= f"{name} worked as a {job} by day but...by night.."

#Sentences .....
# Uses the play's {},{} and {}. 
paragraph+= f" {name} was the amazing Mr.{item}!!!!!!\n"

#Sentences ...
# Uses the play's {},{} and {}. 
paragraph+= f"The amazing Mr.{item} would save cats & {animal}'s from trees."

#Sentences ....
# Uses the play's {},{} and {}. 
paragraph+= f"Using the power of the {item}\n"

#Sentences ...
# Uses the play's {},{} and {}. 
paragraph+= f" Mild mannered {name} would put on his {colour} costume"

#Sentences ...
# Uses the play's {},{} and {}. 
paragraph+= f"To help those in need for the low low fee of €{cost}"

#Sentences ...
# Uses the play's {},{} and {}.
paragraph+= f" because he is the amazing Mr. {item}!!!!!!"


########################################
# Dispaly the MAD-Libs in the Shell
print(paragraph)

########################################
f = open("MAD-Libs.txt", "w")
f.write(paragraph)
f.close()

f = open("MAD-Libs.txt", "r")
mytext = f.read()


audio = gTTS(text=mytext, lang="en", slow=False)
audio.save("MAD-Libs_speech.mp3")

time.sleep(3) # Sleep for 3 seconds
playsound("MAD-Libs_speech.mp3")














