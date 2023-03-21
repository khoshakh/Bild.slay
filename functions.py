'''A collection of function for doing my project.'''

'''List of biology-related words to be randomly selected upon for the hangman game'''
words = ['allele', 'adaptation', 'anatomy', 'anaphase', 'anticodon', 'apoptosis', 'autotroph', 'bacteria','basepair', 'brain', 'cell', 'centromere', 'centrosome', 'chitin', 'chlorophyll', 'chloroplast', 'centriole', 'chromatid', 'CRISPR', 'cytokinesis', 'cytoplasm', 'cytoskeleton','diploid','disaccharide', 'DNA', 'evolution', 'enzyme', 'ecosystem', 'ectotherm', 'endotherm', 'epistasis', 'eukaryote', 'exon', 'exoskeleton', 'fungi', 'gamete', 'gene', 'genotype', 'genus', 'glycerol', 'glycolysis', 'haploid', 'heredity', 'homozygous', 'interphase', 'intron', 'lactase', 'ligand', 'metaphase', 'mitosis', 'meiosis', 'mRNA', 'nucleotide', 'organ', 'osmosis', 'organelle', 'phenotype', 'phospholipid', 'prokaryote', 'prophase', 'pyruvate', 'receptor', 'RNA', 'synapsis', 'systole', 'telomere', 'thymine', 'transcription', 'transferrin', 'translation', 'vacuole', 'vesicle', 'virus', 'xylem', 'phloem', 'zooplankton', 'zygote', 'ribosome']

import random  ##This module allows us down the line to randomly choose a word
import string ##Allows us to to change the case structure of all letters in the game
import matplotlib.pyplot as plt #Imports the pyplot module and assigns it as plt
import matplotlib.image as mpimg #Imports the image module and assigns it as mpimg
from cat_pictures import hangman_cat_dict #imports the hangman_cat_dict function from another folder that reads an image
'''We will put the following block in a separate code, this is just temporary to collaborate on'''
hangman_cat_dict = { #this is the hangman_cat_dict[lives] function that we will use to read an image. the function will be in another folder with actual images.
        9: mpimg.imread('./life9.jpeg'), #still need to draw out all 11 photos of a hangman cat (trying to get function to work before i do that)
        8: mpimg.imread('./life8.jpeg'), #main issue is that the from cat_pictures import hangman_cat_dict function says the cat_pictures is an invalid module, might just be a bug on my part so smoeone else can try?
        7: mpimg.imread('./life7.jpeg'),
        6: mpimg.imread('./life6.jpeg'),
        5: mpimg.imread('./life5.jpeg'),
        4: mpimg.imread('./life4.jpeg'),
        3: mpimg.imread('./life3.jpeg'),
        2: mpimg.imread('./life2.jpeg'),
        1: mpimg.imread('./life1.jpeg'),
        0: mpimg.imread('./life0.jpeg'),
        10:mpimg.imred('.life/10.jpeg')}

plt.imshow(img)
plt.show()

'''Randomly selects a word from the generated list of biology-related words'''
def random_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    return word.upper() # Returning it upper to keep everything uniform

'''The hangman game. Can be put into action via the syntax: hangman_game()'''
def hangman_game():
    word = random_word(words)
    secret_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    chosen = set()  #Empty list for chosen letters

    cat_lives = 9
    
    print("You are a cat and you've found yourself in a sticky predicament! You're trapped in a scientist's laboratory and you need to guess his password to leave the room before it's too late! You can guess one letter at a time... but every wrong letter loses you one of your 9 lives! Can you escape?  (ꏿ ᆺ ꏿ) ")
          
    while len(secret_letters) > 0 and cat_lives > 0:
        print('        ')
        print(cat_lives, 'lives left! Past guesses: ', ' '.join(chosen))

        word_so_far = [letter if letter in chosen else '-' for letter in word]
        print(hangman_cat__dict[lives])#This will be where we print out a picture of the cat depending how many lives are left
        print('So far... ', ' '.join(word_so_far)) #.join concatenates a string

        guess = input('Choose a letter --> ').upper() #This makes the input prompt box
        if guess in alphabet - chosen:
            chosen.add(guess)
            if guess in secret_letters:
                secret_letters.remove(guess)
                print('Yes! Good guess, almost got it!   —ฅ/ᐠ. ̫ .ᐟ\ฅ —  ') 
                print('        ')
            else:
                cat_lives = cat_lives - 1  # takes away a life if wrong
                print('Oh no, wrong guess! Keep trying!  /ᐠ・ᆽ・ᐟ \ ')
                print('        ')
                print('        ')
        elif guess in chosen:
            print('You already guessed that letter!')
            print('        ')
            print('        ')
        else:  #Error handling ; If a character not a letter, does not count guess
            print('Invalid character detected! Must guess a letter.')
            print('        ')
            print('        ')

    if cat_lives == 0:
        print hangman_cat_dict[0] #prints a fully drawn hangman cat
        print('RIP... The word was', word)
        print('        ')
        print(' /ᐠ｡ꞈ｡ᐟ\ ')
    else:
        print hangman_cat_dict[10] #prints a real happy cat
        print('  —ฅ/ᐠ. ̫ .ᐟ\ฅ — ')
        print('            ')
        print('Good job! You guessed the word', word,' with', cat_lives, 'lives to spare!')
