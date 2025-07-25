# FASTA File Reader Program
# This program reads a FASTA-format file containing biological sequences.
# It extracts each sequence and its identifier/description, storing them in a dictionary.
# The program handles multi-line sequences and prints all sequence IDs and their sequences.
# The user provides the file name, and the program checks for its existence before reading.

import os
# Import os model to ensure existence of file
file_name = input("Enter the name of the FASTA file: ")
# Get the name of the file ffrom the reader
file_name = file_name.strip()
# Solve careless writing by user
if not os.path.exists(file_name + ".txt"):
    print("The file is not found.")
    # The file can only be run if it exists in the system
else:
    with open(file_name + ".txt") as file:
        # provided the name is valid open it
        lines = file.readlines()
        # read all lines
        file_dict = {}
        # create a dict to store our data
        sequence_id_description = ""
        # this will hold the sequence id
        sequence = ""
        # thid will hold the actual sequence
        for line in lines:
            # Itterate through each line in the file
            if line.startswith(">"):  # check if it is an identifier line
                if sequence_id_description and sequence:
                    file_dict[sequence_id_description] = sequence
                    sequence_id_description = ""
                    sequence = ""
                    # if a data set is already in the variables store it in dict then clear the variables
                sequence_id_description = line.strip()
                # now store the next sequence id
            else:
                sequence += line.strip()
                # if it is not an id it is a sequence so add it here
        if sequence_id_description and sequence:
            # the last one wont itterate through the loop so add it here
            file_dict[sequence_id_description] = sequence
        file.close()  # close the file
        print("The FASTA file has been read successfully.")
        print("Contents of the FASTA file:")
        for key, value in file_dict.items():
            print(f"{key}: {value}")
        # Print the output
