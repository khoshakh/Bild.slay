"""A collection of function for doing my project."""

'''List of biology-related words to be randomly selected upon for the hangman game'''
words = ['allele', 'adaptation', 'anatomy', 'anaphase', 'anticodon', 'apoptosis', 'autotroph', 'bacteria','basepair', 'brain', 'cell', 'centromere', 'centrosome', 'chitin', 'chlorophyll', 'chloroplast', 'centriole', 'chromatid', 'CRISPR', 'cytokinesis', 'cytoplasm', 'cytoskeleton','diploid','disaccharide', 'DNA', 'evolution', 'enzyme', 'ecosystem', 'ectotherm', 'endotherm', 'epistasis', 'eukaryote', 'exon', 'exoskeleton', 'fungi', 'gamete', 'gene', 'genotype', 'genus', 'glycerol', 'glycolysis', 'haploid', 'heredity', 'homozygous', 'interphase', 'intron', 'lactase', 'ligand', 'metaphase', 'mitosis', 'meiosis', 'mRNA', 'nucleotide', 'organ', 'osmosis', 'organelle', 'phenotype', 'phospholipid', 'prokaryote', 'prophase', 'pyruvate', 'receptor', 'RNA', 'synapsis', 'systole', 'telomere', 'thymine', 'transcription', 'transferrin', 'translation', 'vacuole', 'vesicle', 'virus', 'xylem', 'phloem', 'zooplankton', 'zygote', 'ribosome']

import random  ##This module allows us down the line to randomly choose a word
import string ##Allows us to to change the case structure of all letters in the game

'''Function allows for randomized word to be selected'''
def get_word(words):
    word = random.choice(words) # Randomly selects a word from the word list
    return word

'''The hangman function''' 
def hangman():  # hangman game function 
    word = get_word(words)   # Calls the get_words function which randomly chooses a word
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  ##Letters upper case to not confuse the computer
    used_letters = set()  # what the user has guessed ## We're setting it to be in a list

    cat_lives = 9  # 9 lives to start
    
# Creating the user input box and setting restrictions
    
    user_letter = input('Guess a letter: ').upper() ##User prompt; capitalizes letter
    
    #Error handling step below, ensures the guess is actually a letter           
    if user_letter not in alphabet:
        print("Must guess a letter. Invalid character detected.")
    if user_letter in alphabet - used_letters:  #If guessed letter = new
        used_letters.add(user_letter)  #Then added to used_letters
    if user_letter in word_letters:   #If letter guessed = correct
        word_letters.remove(user_letter)  #Then letter = removed from "word_letters"
        print(user_letter) 
    elif user_letter in used_letters:
        print("You have already guessed that letter!")
    else:
        remaining_lives = cat_lives-1
        print("Your letter:", user_letter, ", is not in the word.")
        
    while len(word_letters) >0 and remaining_lives >0: #While loop kicks in 1st wrong guess
        print("You have", remaining_lives , "lives left. You have used the letters: ", used_letters)
 
    if remaining_lives == 0:
        print("Need to insert image from image function here") # Dislpay the whole hangman
        print("You have died (×_x)... The word was:", word)
    else: 
        print("Good job! You guessed the word",word,"!")
