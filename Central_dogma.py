"""
DNA to Protein Converter 🧬

This program simulates the process of gene expression by converting a DNA sequence
to its corresponding protein sequence. It performs two biological steps:
1. Transcription: DNA → mRNA
2. Translation: mRNA → Protein (amino acid sequence)

Author: [Your Name]
"""

# Function to transcribe a DNA strand into mRNA
def transcription(strand):
    # DNA to RNA base pairings
    base_pairings = {'A': 'U', 'T': 'A', 'G': 'C', 'C': 'G'}
    
    # Clean and convert the strand to uppercase
    dna_list = strand.strip().upper()
    rna_list = []
    
    # Loop through each base and transcribe it
    for base in dna_list:
        if base not in base_pairings:
            return "Invalid sequence"
        else:
            rna_list.append(base_pairings[base])
    
    # Return the complete mRNA strand
    return "".join(rna_list)

# Function to find the start codon (AUG) in the mRNA sequence
def find_AUG(mrna):
    start_index = mrna.find("AUG")
    if start_index == -1:
        print("No start codon found")
    else:
        # Return the index right after AUG to begin translation
        return start_index + 3

# Function to translate the mRNA into a protein sequence
def translation(mrna):
    codon_list = []          # List to store codons from mRNA
    protein_sequence = []    # List to store translated amino acids

    # Codon to amino acid translation table
    codon_table = {
        "UUU": "Phenylalanine", "UUC": "Phenylalanine",
        "UUA": "Leucine",       "UUG": "Leucine",
        "CUU": "Leucine",       "CUC": "Leucine",
        "CUA": "Leucine",       "CUG": "Leucine",
        "AUU": "Isoleucine",    "AUC": "Isoleucine",
        "AUA": "Isoleucine",    "AUG": "Methionine",
        "GUU": "Valine",        "GUC": "Valine",
        "GUA": "Valine",        "GUG": "Valine",
        "UCU": "Serine",        "UCC": "Serine",
        "UCA": "Serine",        "UCG": "Serine",
        "CCU": "Proline",       "CCC": "Proline",
        "CCA": "Proline",       "CCG": "Proline",
        "ACU": "Threonine",     "ACC": "Threonine",
        "ACA": "Threonine",     "ACG": "Threonine",
        "GCU": "Alanine",       "GCC": "Alanine",
        "GCA": "Alanine",       "GCG": "Alanine",
        "UAU": "Tyrosine",      "UAC": "Tyrosine",
        "UAA": "Stop",          "UAG": "Stop",
        "CAU": "Histidine",     "CAC": "Histidine",
        "CAA": "Glutamine",     "CAG": "Glutamine",
        "AAU": "Asparagine",    "AAC": "Asparagine",
        "AAA": "Lysine",        "AAG": "Lysine",
        "GAU": "Aspartic acid", "GAC": "Aspartic acid",
        "GAA": "Glutamic acid", "GAG": "Glutamic acid",
        "UGU": "Cysteine",      "UGC": "Cysteine",
        "UGA": "Stop",          "UGG": "Tryptophan",
        "CGU": "Arginine",      "CGC": "Arginine",
        "CGA": "Arginine",      "CGG": "Arginine",
        "AGU": "Serine",        "AGC": "Serine",
        "AGA": "Arginine",      "AGG": "Arginine",
        "GGU": "Glycine",       "GGC": "Glycine",
        "GGA": "Glycine",       "GGG": "Glycine"
    }

    # Get starting point of translation
    start_index = find_AUG(mrna)
    if start_index is None:
        return -1
        print("No start codon found in mRNA sequence")
    else:
        # Extract codons from the mRNA starting after AUG
        for i in range(start_index, len(mrna), 3):
            codon = mrna[i:i+3]
            codon_list.append(codon)

    # Translate codons into protein sequence using the codon table
    for codon in codon_list:
        if codon in codon_table and codon_table[codon] != "Stop":
            protein_sequence.append(codon_table[codon])
        elif codon in codon_table and codon_table[codon] == "Stop":
            break  # Stop translation at stop codon

    return protein_sequence

# --- Execution starts here ---
dna_strand = input("Enter DNA sequence to begin transcription: ")
mrna = transcription(dna_strand)
protein_sequence = translation(mrna)
if protein_sequence != -1:
  print(f"The predicted protein sequence is: {protein_sequence}")
