"""
 🧬 Transcription Simulator
 This program simulates the biological process of transcription, where a DNA strand
 is converted into an RNA strand. In transcription:
 - A (Adenine) → U (Uracil)
 - T (Thymine) → A (Adenine)
 - G (Guanine) → C (Cytosine)
 - C (Cytosine) → G (Guanine)
 The user inputs a DNA sequence, and the program outputs the corresponding RNA sequence.

"""

def transcription_simulator(dna_strand):
    # Convert the DNA strand string into a list of bases
    bases = list(dna_strand)
    rna_bases = []  # List to store the transcribed RNA bases
    # Loop through each base in the DNA strand
    for base in bases:
        # Transcribe Adenine (A) to Uracil (U)
        if base == "A":
            rna_bases.append("U")
        # Transcribe Thymine (T) to Adenine (A)
        elif base == "T":
            rna_bases.append("A")
        # Transcribe Guanine (G) to Cytosine (C)
        elif base == "G":
            rna_bases.append("C")
        # Transcribe Cytosine (C) to Guanine (G)
        elif base == "C":
            rna_bases.append("G")
        # Handle invalid bases
        else:
            print("Invalid sequence")
    # Join the RNA bases
    return "".join(rna_bases)


dna_strand = input("Enter DNA sequence: ").strip().upper()
rna_strand = transcription_simulator(dna_strand)
print(f"The transcripted RNA strand of the given DNA strand is {rna_strand}")
