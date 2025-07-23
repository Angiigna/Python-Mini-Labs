# 🐍 Python Mini Labs – My Learning Journey

Welcome! This repository is a personal catalog of mini Python programs that document my learning process as I study Python from the ground up. Each program corresponds to a concept or group of concepts I’ve learned—starting from the very basics like variables and loops, to more advanced topics like functions, file handling, and data analysis.

## 🎯 Purpose

- ✅ **Practice & Reinforce:** I write these mini-programs to solidify my understanding of Python.
- 📘 **Share & Teach:** Every program is structured to be beginner-friendly and is accompanied by a short explanation.
- 🌱 **Track Progress:** Each script represents a “session deliverable” as I work through my 1-year learning plan.
- 🤝 **Help Others:** If you're also learning Python, feel free to fork, clone, and use this repo as a guided reference.

## 🧩 What You'll Find

- Standalone `.py` files for each concept.
- Descriptive filenames and comments inside the code.
- A concept summary in each folder or file.
- No frameworks or dependencies—just pure Python basics!

> Whether you're a beginner or revisiting Python after a break, I hope this repo helps you on your journey too.

---

Happy Coding! ✨

---
### 🔢 Program 1: Terminal-Based Calculator

**📝 Description:**  
A simple calculator that runs in the terminal and performs basic arithmetic operations:  
Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`), Exponentiation (`**`), and Floor Division (`//`).  
The user inputs two numbers and an operator, and the result is displayed.

**📌 Concepts Covered:**
- Input/Output
- Variables & Data Types
- Arithmetic Operators
- Conditional Statements (`if-elif-else`)
- Basic Error Handling (e.g., division by zero)
- String Formatting using `f-strings`

**📚 Reference:**  
Learned from the [Programming with Mosh](https://www.youtube.com/@programmingwithmosh) Python Basics tutorial.  
Prior experience with C, C++, and JavaScript helped in picking up Python quickly.

📂 **[View Code →](./simple_calculator.py)**

---

### 🧪 Program 2: FizzBuzz

**📝 Description:**  
This classic beginner-level program prints numbers from `1` to a user-defined limit. Based on divisibility:
- Prints `"Fizz"` if divisible by 3
- Prints `"Buzz"` if divisible by 5
- Prints `"FizzBuzz"` if divisible by both 3 and 5
- Otherwise, prints the number itself

**📌 Concepts Covered:**
- Input/Output
- Loops (`for`, `range`)
- Conditionals (`if`, `elif`, `else`)
- Modulo Operator (`%`)
- Functions
- Logic Building

**📚 Reference:**  
Learned from the [Programming with Mosh](https://www.youtube.com/@programmingwithmosh) Python Basics tutorial.

📂 **[View Code →](./FizzBuzz.py)**

---
### 🧪 Program 3: Number Guessing Game  
**📝 Description:**  
This is an interactive terminal-based number guessing game with three difficulty levels:  

- **Easy**: Guess a number between 1 and 10 (5 attempts)  
- **Medium**: Guess a number between 1 and 50 (10 attempts)  
- **Hard**: Guess a number between 1 and 100 (15 attempts)  

The program randomly generates a number and gives the player hints ("too low" or "too high") after each guess. The game supports replaying and ends gracefully when the user chooses to quit.

**📌 Concepts Covered:**  
- Input/Output  
- Loops (`for`, `while`)  
- Conditional Statements (`if`, `elif`, `else`)  
- Random Number Generation (`random.randint()`)  
- Functions and Code Structuring  
- Basic Game Logic  

**📚 Reference:**  
Learned from the Programming with Mosh Python Basics tutorial.

📂 **[View Code →](./number_guessing_game.py)**

---
### 🔍 Program 4: Linear Search

📝 **Description:**
This program performs a **linear search** on a list of numbers provided by the user. It goes through each element in the list one by one to find the specified item. If found, it prints the index at which the item occurs; if not, it notifies the user that the item is not present.

📌 **Concepts Covered:**

* User Input and Output
* Type Conversion (`str` → `int`)
* Lists (created using `split()` and `map()`)
* `for` loop with `enumerate()`
* `if-else` control structures
* Search logic and early loop termination (`break`, `else` on loop)

💡 **Why It’s Important:**
Linear Search is one of the most fundamental algorithms in computer science. It introduces beginners to algorithmic thinking and search operations, forming the foundation for more advanced algorithms like Binary Search and data structures like arrays and linked lists. It also reinforces iteration, conditionals, and loop control flow.

📚 **References:**

* [CodeSavant YouTube Channel](https://www.youtube.com/@CodeSavant)
* [Corey Schafer - Python Programming Beginner Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)

📂 **[View Code →](./Linear_search.py)**

---
### 🧪 Program 5: Binary Search

📝 **Description:**
This program demonstrates the **Binary Search** algorithm, a powerful method for efficiently finding an item in a sorted list. It repeatedly divides the search interval in half to quickly narrow down the location of the target number.

* First, the user inputs a list of integers and a number to search for.
* The list is automatically sorted.
* A recursive function is used to apply the binary search logic.
* If the item is found, its index is displayed; if not, a message is shown.

📌 **Concepts Covered:**

* Input/Output
* Sorting a List
* Recursion
* Binary Search Logic
* Conditionals
* Divide and Conquer Strategy

📚 **Reference:**
This program was inspired by:

* [CodeSavant](https://www.youtube.com/@CodeSavant)
* [Corey Schafer's Python Tutorials](https://www.youtube.com/user/schafer5)

🧠 **Why It Matters:**
Binary search is one of the most **fundamental algorithms in computer science**, especially relevant in contexts where **performance matters** (like searching large databases or implementing search bars). Understanding how it narrows down options using mathematical logic helps build a solid foundation for learning more advanced algorithms.

⚠️ **Note:**
I’ve jumped ahead to implement this relatively advanced search algorithm even though I haven’t yet formally covered some basics like **lists and loops in depth**. This is possible due to my prior experience with programming. Simpler programs that focus on those basic concepts will likely be added in upcoming sessions to balance the learning curve.

📂 **[View Code →](./Binary_search.py)**

---
### 🧪 Program 5: Transcription Simulator
**📝 Description:**
This biology-inspired program simulates the process of DNA transcription, converting a DNA strand entered by the user into its corresponding RNA strand. The simulation follows the real-life base pairing rules in transcription:

A (Adenine) → U (Uracil)

T (Thymine) → A (Adenine)

G (Guanine) → C (Cytosine)

C (Cytosine) → G (Guanine)

Invalid bases are handled with an error message. This is a foundational concept in molecular biology and makes for an exciting blend of programming and life sciences.

**📌 Concepts Covered:**

String manipulation

Lists and iteration

Conditionals (if, elif, else)

Basic biological logic implementation

Error handling for unexpected input

**📚 Reference:**
Self-developed based on prior knowledge of Python and genetics. No external tutorials used.

**[📂 View Code →](./transcription_simulator.py)**

---
### 🧪 Program 6: DNA/RNA Sequence Validator
**📝 Description:**
This program checks if a user-input nucleotide sequence is a valid DNA or RNA strand by verifying the characters in the input against biological rules:

DNA bases: A (Adenine), T (Thymine), G (Guanine), C (Cytosine)

RNA bases: A (Adenine), U (Uracil), G (Guanine), C (Cytosine)

It processes the input to remove whitespace and standardizes case before validation. This tool is especially useful for learners combining biology with basic programming.

**📌 Concepts Covered:**

String manipulation (strip(), upper())

Conditional statements (if, elif, else)

Looping through strings

Custom function creation

Basic bioinformatics logic

**📚 Reference:**
Original idea based on real biological rules. Program developed independently using concepts covered in earlier sessions.

**[📂 View Code →](./dnaorrna_validator.py)**

---
### 🔢 Program X: Central Dogma – DNA to Protein Translator


📝 **Description:**
This program simulates the **Central Dogma of Molecular Biology**, covering both:

* **Transcription**: Converts a given DNA strand to mRNA.
* **Translation**: Begins from the first `AUG` start codon in the mRNA and translates codons into their corresponding amino acids using a codon dictionary.

Transcription is implemented using a **dictionary mapping** of base pairs (A→U, T→A, G→C, C→G), offering a cleaner and more scalable alternative to the if-else ladder used in the earlier `Transcription Simulator`.
The translation process uses a standard codon table (64 entries) to map RNA triplets to full amino acid names.


📌 **Concepts Covered:**

* Biological Processes: Transcription and Translation
* DNA → mRNA → Protein
* String Manipulation
* Dictionary Usage
* Functions and Reusability
* Basic Validation and Error Handling
* Loops and Conditional Logic

📚 **Reference:**
This program was created entirely from scratch, based on understanding of biology concepts (central dogma, codons) and previously learned Python logic from  [Corey Schafer's Python Tutorials](https://www.youtube.com/user/schafer5)

**📂[View Code →](./Central_dogma.py)** 
---
### 🎯 Goal

These mini programs are part of a structured, hands-on approach to learning Python. Each script is designed to reinforce specific topics while providing practical examples. The aim is to create a useful reference for myself and other beginners who want to follow a topic-wise, project-backed learning path.


