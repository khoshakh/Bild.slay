"""A collection of function for doing my project."""

words = ['allele', 'adaptation', 'anatomy', 'anaphase', 'anticodon', 'apoptosis', 'autotroph', 'bacteria','basepair', 'brain', 'cell', 'centromere', 'centrosome', 'chitin', 'chlorophyll', 'chloroplast', 'centriole', 'chromatid', 'CRISPR', 'cytokinesis', 'cytoplasm', 'cytoskeleton','diploid','disaccharide', 'DNA', 'evolution', 'enzyme', 'ecosystem', 'ectotherm', 'endotherm', 'epistasis', 'eukaryote', 'exon', 'exoskeleton', 'fungi', 'gamete', 'gene', 'genotype', 'genus', 'glycerol', 'glycolysis', 'haploid', 'heredity', 'homozygous', 'interphase', 'intron', 'lactase', 'ligand', 'metaphase', 'mitosis', 'meiosis', 'mRNA', 'nucleotide', 'organ', 'osmosis', 'organelle', 'phenotype', 'phospholipid', 'prokaryote', 'prophase', 'pyruvate', 'receptor', 'RNA', 'synapsis', 'systole', 'telomere', 'thymine', 'transcription', 'transferrin', 'translation', 'vacuole', 'vesicle', 'virus', 'xylem', 'phloem', 'zooplankton', 'zygote', 'ribosome']

import random  ##This module allows us down the line to randomly choose a word
import string ##Allows us to to change the case structure of all letters in the game

def get_word(words):
    word = random.choice(words)
    return word


'''The hangman function''' 

def hangman():  #Making the hangman game function 
    word = get_word(words)   ## word = choose_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  ##Letters upper case to not confuse the computer
    used_letters = set()  # what the user has guessed ## We're setting it to be in a list

    cat_lives = 9  ## Cat hang man = 9 Lives (cat lives)
    
    while len(word_letters) >0 and lives >0: #While loop kicks in with 1st wrong guess
        word_letters.append()
        print("You have", remaining_lives, "lives left. You have used the letters:", used_letters,")
    
    '''Creating the user input box and setting restrictions'''
    
    user_letter = input('Guess a letter: ').upper() ##User prompt; capitalizes letter 
    if user_letter in alphabet - used_letters:  #If guessed letter = new
        used_letters.add(user_letter)  #Then added to used_letters
    if user_letter in word_letters:   #If letter guessed = correct
        word_letters.remove(user_letter)  #Then letter = removed from "word_letters"
        print(user_letter)
              
    else:
        remaining_lives = cat_lives-1
        return remaining_lives
        print("Your letter",user_letter,"is not in the word")
    elif user_letterin used_letters:
        print("You have already guessed that letter")
              
              
  '''Error handling step below, ensures the guess is actually a letter'''
              
    else:   # We can make this more complex with is instance or type. etc. for grading
        print("Must guess a letter. Invalid character detected.")
              
    if remaining_lives == 0:
        print("Need to insert image from image function here") # Dislpay the whole hangman
        print("You have died (×_x)... The word was:",word")
    else: 
        print("Good job! You guessed the word",word,"!")
              
def images():
    
        
    
##Need error handling
    ##Check if valid characters (only letters are used)
        ##- If numbers or other nonletters are used then the code will display an error message ("Invalid input")
        ##type.letter or word or whatever proper syntax is
        ##numpy package?
        ##is instance()
