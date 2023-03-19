"""A collection of function for doing my project."""

words = ['allele', 'adaptation', 'anatomy', 'anaphase', 'anticodon', 'apoptosis', 'autotroph', 'bacteria','basepair', 'biodiversity', 'brain', 'cell', 'centromere', 'centrosome', 'chitin', 'chlorophyll', 'chloroplast', 'centriole', 'chromatid', 'competition', 'CRISPR', 'cytokinesis', 'cytoplasm', 'cytoskeleton', 'decomposition','diploid']
         
## , ‘disaccharide’, ‘DNA’, ‘evolution’, ‘enzyme’, ‘ecosystem’, ‘ectotherm’, ‘endotherm’, ‘epistasis’, ‘eukaryote’, ‘exon’, ‘exoskeleton’, ‘fungi’, ‘gamete’, ‘gene’, ‘genotype’, ‘genus’, ‘glycerol’, ‘glycolysis’, ‘haploid’, ‘heredity’, ‘heterozygous’, ‘homozygous’, ‘interphase’, ‘intron’, ‘lactase’, ‘ligand’, ‘metaphase’, ‘mitosis’, ‘meiosis’, ‘mRNA’, ‘nucleotide’, ‘organ’, ‘osmosis’, ‘organelle’, ‘phenotype’, ‘phospholipid’, ‘phytoplankton’, ‘prokaryote’, ‘prophase’, ‘pyruvate’, ‘receptor’, ‘RNA’, ‘synapsis’, ‘systole’, ‘telomere’, ‘thymine’, ‘transcription’, ‘transferrin’, ‘translation’, ‘vacuole’, ‘vesicle’, ‘virus’, ‘xylem’, ‘phloem’, ‘zooplankton’, ‘zygote’, ‘ribosome’, ‘mitochondria’]

import random  ##This module allows us down the line to randomly choose a word
import string ##Allows us to to change the case structure of all letters in the game

def get_word(words):
    word = random.choice(words)
    return word


'''The hangman function''' 

def hangman():  ## Making the hangman game function 
    word = get_word(words)   ## word = choose_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  ##Letters upper case to not confuse the computer
    used_letters = set()  # what the user has guessed ## We're setting it to be in a list
    return used_letters

    cat_lives = 9  ## Cat hang man = 9 Lives (cat lives)
    
    '''User input'''
    
    
    
##Need error handling
    ##Check if valid characters (only letters are used)
        ##- If numbers or other nonletters are used then the code will display an error message ("Invalid input")
        ##type.letter or word or whatever proper syntax is
        ##numpy package?
        ##is instance()
