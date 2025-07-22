# DNA/RNA Sequence Validator
# This program checks whether a user-provided nucleotide sequence is a valid DNA or RNA strand.
# It removes whitespace, converts the input to uppercase, and verifies that all characters are valid bases:
# - DNA: A (Adenine), T (Thymine), G (Guanine), C (Cytosine)
# - RNA: A (Adenine), U (Uracil), G (Guanine), C (Cytosine)
# The program prints whether the sequence is valid DNA, valid RNA, or invalid/anomalous.

def is_valid_dna(dna_strand):
    # Remove whitespace and convert to uppercase for consistency
    bases = dna_strand.strip().upper()
    # Check each base to ensure it's a valid DNA base (A, T, G, C)
    for base in bases:
        if base not in "ATGC":
            return False  # Return False if any invalid base is found
    return True  # Return True if all bases are valid


def is_valid_rna(rna_strand):
    # Remove whitespace and convert to uppercase for consistency
    bases = rna_strand.strip().upper()
    # Check each base to ensure it's a valid RNA base (A, U, G, C)
    for base in bases:
        if base not in "AUGC":
            return False  # Return False if any invalid base is found
    return True  # Return True if all bases are valid


def validate_sequence(sequence):
    # Check if the sequence is valid DNA
    if is_valid_dna(sequence):
        print("This is a valid DNA sequence.")
    # If not DNA, check if it's valid RNA
    elif is_valid_rna(sequence):
        print("This is a valid RNA sequence.")
    # If neither, it's invalid or an anomaly
    else:
        print("This is an invalid sequence or an anomaly.")


# Get sequence input from the user
sequence = input("Enter sequence: ")
# Validate sequence
validate_sequence(sequence)
