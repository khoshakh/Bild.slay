'''A collection of function for doing my project.'''

'''List of biology-related words to be randomly selected upon for the hangman game'''
words = ['allele', 'adaptation', 'anatomy', 'anaphase', 'anticodon', 'apoptosis', 'autotroph', 'bacteria','basepair', 'brain', 'cell', 'centromere', 'centrosome', 'chitin', 'chlorophyll', 'chloroplast', 'centriole', 'chromatid', 'CRISPR', 'cytokinesis', 'cytoplasm', 'cytoskeleton','diploid','disaccharide', 'DNA', 'evolution', 'enzyme', 'ecosystem', 'ectotherm', 'endotherm', 'epistasis', 'eukaryote', 'exon', 'exoskeleton', 'fungi', 'gamete', 'gene', 'genotype', 'genus', 'glycerol', 'glycolysis', 'haploid', 'heredity', 'homozygous', 'interphase', 'intron', 'lactase', 'ligand', 'metaphase', 'mitosis', 'meiosis', 'mRNA', 'nucleotide', 'organ', 'osmosis', 'organelle', 'phenotype', 'phospholipid', 'prokaryote', 'prophase', 'pyruvate', 'receptor', 'RNA', 'synapsis', 'systole', 'telomere', 'thymine', 'transcription', 'transferrin', 'translation', 'vacuole', 'vesicle', 'virus', 'xylem', 'phloem', 'zooplankton', 'zygote', 'ribosome']

import random  ##This module allows us down the line to randomly choose a word
import string ##Allows us to to change the case structure of all letters in the game

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
        #print(lives_visual_dict[lives])This will be where we link to and input the cat pics
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
        #print visual of the cat hangman
        print('RIP... The word was', word)
        print('        ')
        print(' /ᐠ｡ꞈ｡ᐟ\ ')
    else:
        #print(cute cat picture)
        print('  —ฅ/ᐠ. ̫ .ᐟ\ฅ — ')
        print('            ')
        print('Good job! You guessed the word', word,' with', cat_lives, 'lives to spare!')
