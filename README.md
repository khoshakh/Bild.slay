# Biology Hangman Game: Biohazard Escape Room

## Project Description
The goal of the project is to create a game of hangman, where the user will guess a word letter by letter, with words relating to a wide variety of biological topics. We wanted to take a fun approach to the project, yet still a challenging one that tested our knowledge of coding and biology. We decided to go for a light-hearted game such as hangman, which would allow us to incorporate some creativity into a game that will also help us share our knowledge about biology and hopefully teach others new biological concepts and terms. We wanted to create a different, more entertaining version of hangman by implementing a storyline involving a cat stuck in a laboratory who has to guess a passcode to escape. We chose a playful game like hangman as we wanted to approach the project from an exciting standpoint but also chose it as it was stimulating enough to test our knowledge of coding and biology. We also hope this game will help us share our knowledge about biology and hopefully teach others new biological concepts and terms. To set up our game, we first made a list containing all possible answers for the game and used a function to generate a random word. The user is then prompted to guess a letter and a return counter is used to let the user know how many tries they have left. The game will continue until the player runs out of attempts or guesses the word correctly. We will focus on the user-experience by adding visuals to show how many guesses are left, update the hangman based on the guesses, and have a display showing which letters the user has guessed.

## Team Member Names & Contributions
* Jillian Menez (A15564534) wrote the hangman_game function
* Jovina Djulamsah (A17225420): wrote the words list and word determination function
* Name (PID): Cleaned data & wrote script to load, etc.

<hr>


___________________________________

## Setup 
Run the following cell to import the necessary modules to play.

-CODE CELL BEGIN-
from my_module.functions import random_word
from my_module.functions import cat_game
from my_module.functions import final_task
-CODE CELL END-

# Oh no!

You are a cat and you've found yourself in a sticky predicament! 

You're trapped in a PI's laboratory and you need to guess his password to leave the room.

The problem: If you guess the password incorrectly, a cloud of poisonous gas will fill release and fill the room!

Guess the passcode one letter at a time and escape!

## Rules and Hints:

- The PI is a huge biology nerd and his passcode reflects it.

- Once you guess a letter correctly, the letter and it's proper position will show in the Passcode region.

- You can guess one letter at a time... but every wrong letter loses you one of your 9 lives! 

- After 9 incorrect guesses, you lose!

##### Can you escape?  (ꏿ ᆺ ꏿ) 

### Run the following code to begin guessing!

-CODE CELL (cat_game())-
_______________________________________________
### Good job on your harrowing escape!

#### But...

In your haste to plug in the final letter of the passcode, your fat little paw slips and you punch in the final letter incorrectly!

You are faced with one saving grace task before the noxious gas is released into the room... 

The passcode lock screen now reads:
#### Answer the following security question to bypass poison cloud: 

### Run the code in the next section to begin the task

-CODE CELL (final_task()) -
_____________________________________________________________________

_______________________________________________________________________________

# Reflection


### Jillian Menez: 
- I enjoyed this project and I had fun with creating a silly narrative along with it. I entered this class without any prior coding experience and I did not believe that I would be able to carry out such a task by the end of the quarter. The code behind our little game is very simple, but I am really proud of how we were able to work it out and build our own game. I am more confident in my abilty to troubleshoot after this assignment as I could not just turn to google to answer my questions, I had to actively search through python-specific forums and look through others' code and resources in order to piece together the answers I needed. Our project felt so difficult when we were working through it, but the end product is so simple. It really gives me perspective to just how much more there is to learn, I haven't even scratched the surface. I enjoyed my dive into coding and I intend to continue learning python and explore other coding languages as well. 

### Jovina Djulamsah: 
I enrolled into BILD62 without any coding knowledge, unaware of what to expect. I think that the functions we learned in class were extremely helpful as we worked on the project, especially loops and if statements which our project greatly consisted of. I felt nervous working on the project as I did not think I had the knowledge or skills to create such project but after working through it with my peers, I now feel more confident in my ability to code and debug errors. This project has given me the assurance that coding does not entirely rely on skills/intelligence and has helped me expand my coding knowledge. I thoroughly enjoyed my time in this class and am looking forward to using Python in the future and learning more languages.
### Gary Taing: 
The course as a whole was a very challenging but fun experience. Prior to this class, I had no coding experience and thus did not know what to expect the coding process to be like, which I found out to be incredibly frustrating yet fulfilling. The notebooks and assignments we worked on in class definitely soldified some of my coding skills, but what I believed helped me succeed in this class, especially the final project, was learning how to search for resources to help me achieve my end code. Because of this, I was confident tackling our final project as a hangman game did not seem too complicated and could be accomplished by using what we learned in class and finding answers to solutions on the internet. What I did have trouble with was learning how to piece functions together cohesively, especially since I am so used to focusing on one type of code at a time. Overall, tt was very fun to see all the pieces come together and working cohesively to create a well-functioned game. What I took from this project and the class is that there are endless possibilties to what coding offers, and the best way to enjoy coding is to be patient and not rush through it.
