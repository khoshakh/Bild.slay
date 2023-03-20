'''A collection of function for doing my project.'''

'''List of biology-related words to be randomly selected upon for the hangman game'''
words = ['allele', 'adaptation', 'anatomy', 'anaphase', 'anticodon', 'apoptosis', 'autotroph', 'bacteria','basepair', 'brain', 'cell', 'centromere', 'centrosome', 'chitin', 'chlorophyll', 'chloroplast', 'centriole', 'chromatid', 'CRISPR', 'cytokinesis', 'cytoplasm', 'cytoskeleton','diploid','disaccharide', 'DNA', 'evolution', 'enzyme', 'ecosystem', 'ectotherm', 'endotherm', 'epistasis', 'eukaryote', 'exon', 'exoskeleton', 'fungi', 'gamete', 'gene', 'genotype', 'genus', 'glycerol', 'glycolysis', 'haploid', 'heredity', 'homozygous', 'interphase', 'intron', 'lactase', 'ligand', 'metaphase', 'mitosis', 'meiosis', 'mRNA', 'nucleotide', 'organ', 'osmosis', 'organelle', 'phenotype', 'phospholipid', 'prokaryote', 'prophase', 'pyruvate', 'receptor', 'RNA', 'synapsis', 'systole', 'telomere', 'thymine', 'transcription', 'transferrin', 'translation', 'vacuole', 'vesicle', 'virus', 'xylem', 'phloem', 'zooplankton', 'zygote', 'ribosome']

import random  ##This module allows us down the line to randomly choose a word
import string ##Allows us to to change the case structure of all letters in the game

def random_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    return word.upper() # Returning it upper to keep everything uniform


def hangman_game():
    word = random_word(words)
    secret_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    chosen = set()  #Empty list for chosen letters

    cat_lives = 9

#Making the input box
    while len(secret_letters) > 0 and cat_lives > 0:
        print(cat_lives, 'left! Past guesses: ', ' '.join(chosen))

#This puts together the correct guessed letters in order in the word
        word_so_far = [letter if letter in chosen else '-' for letter in word]
        #print(lives_visual_dict[lives])  # This will be where we link to and input the cat pics
        print('So far... ', ' '.join(word_so_far))   # this .join method returns a new string concatenated (basically it joins things together)

        guess = input('Choose a letter --> ').upper()  #making it upper case to keep uniform 
        if guess in alphabet - chosen:
            chosen.add(guess)
            if guess in secret_letters:
                secret_letters.remove(guess)
                print('')

            else:
                cat_lives = cat_lives - 1  # takes away a life if wrong
                print('Wrong!')

        elif guess in chosen:
            print('You already used that letter.')

        else:
            print('Invalid character detected! Must guess a letter.')

    if cat_lives == 0:
        #print(lives_visual_dict[lives])
        print('RIP... The word was', word)
    else:
        #print(cute cat picture)
        print('Good job! You guessed the word', word,' with', cat_lives, 'lives to spare!')
