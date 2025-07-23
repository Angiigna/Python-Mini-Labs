# Note Taker Program
# This program allows the user to create a new note or add content to an existing note.
# If the user chooses to start a new note, it creates a new text file and writes the content.
# If the user chooses to add to an existing note, it appends the new content to the specified file.

import os  # Import the os module for file existence checking

# Ask the user if they want to start a new note
start_input = input(
    "Do u wish to start a new note? (yes/no): ").strip().lower()

if start_input == "yes":
    # If user wants a new note, ask for the note name
    note_name = input("Enter the name of your note: ")
    # Check if the note file already exists
    if not os.path.exists(note_name + ".txt"):
        # If not, ask for the note content
        note_content = input("Enter the content of your note: ")
        # Create and write the content to the new file
        file = open(note_name + ".txt", "w")
        file.write(note_content)
        print("Note created sucessfully.")
        file.close()
else:
    # If user wants to add to an existing note, ask for the note name
    input_notename = input("Enter the name of note you wish to add to :")
    # Open the file in append mode and add the new content
    with open(input_notename + ".txt", "a") as file:
        note_content = input("Enter the content you wish to add: ")
        file.write("\n" + note_content)
        print("Content added to note successfully.")
        file.close()
