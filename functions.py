"""A collection of function for doing my project."""

### We can put our words list in here as well as the images for hangman

"""A collection of function for doing my project."""

words = ['allele', 'adaptation', 'anatomy', 'anaphase', 'anticodon', 'apoptosis', 'autotroph', 'bacteria','basepair', 'biodiversity', 'brain', 'cell', 'centromere', 'centrosome', 'chitin', 'chlorophyll', 'chloroplast', 'centriole', 'chromatid', 'competition', 'CRISPR', 'cytokinesis', 'cytoplasm', 'cytoskeleton', 'decomposition','diploid']
         
##‘disaccharide’, ‘DNA’, ‘evolution’, ‘enzyme’, ‘ecosystem’, ‘ectotherm’, ‘endotherm’, ‘epistasis’, ‘eukaryote’, ‘exon’, ‘exoskeleton’, ‘fungi’, ‘gamete’, ‘gene’, ‘genotype’, ‘genus’, ‘glycerol’, ‘glycolysis’, ‘haploid’, ‘heredity’, ‘heterozygous’, ‘homozygous’, ‘interphase’, ‘intron’, ‘lactase’, ‘ligand’, ‘metaphase’, ‘mitosis’, ‘meiosis’, ‘mRNA’, ‘nucleotide’, ‘organ’, ‘osmosis’, ‘organelle’, ‘phenotype’, ‘phospholipid’, ‘phytoplankton’, ‘prokaryote’, ‘prophase’, ‘pyruvate’, ‘receptor’, ‘RNA’, ‘synapsis’, ‘systole’, ‘telomere’, ‘thymine’, ‘transcription’, ‘transferrin’, ‘translation’, ‘vacuole’, ‘vesicle’, ‘virus’, ‘xylem’, ‘phloem’, ‘zooplankton’, ‘zygote’, ‘ribosome’, ‘mitochondria’]

import random  ##This module allows us down the line to randomly choose a word

def get_word(words):
    word = random.choice(words)
    return word

def my_func():
    pass

def my_other_func():
    pass
