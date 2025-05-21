# 📊 University Progression Outcome Predictor – Python Coursework

## 🎯 Overview

This is a command-line Python application developed as part of the **4COSC006C: Software Development I** module.  
The program helps the university determine student progression outcomes based on input credit values: **Pass**, **Defer**, and **Fail**.  
The progression categories follow strict university regulations and include:

- `Progress`
- `Progress (module trailer)`
- `Do not Progress – module retriever`
- `Exclude`

---

## ✅ Features

- Accepts and validates user input (integer check, value range, total = 120)
- Determines correct progression outcome
- Allows multiple entries for staff users
- Supports student and staff modes
- Displays outcomes using a graphical histogram (`graphics.py`)
- Stores outcomes in lists (Part 2)
- Writes outcomes to and reads from a text file (Part 3)
- Modular design with user-defined functions
- Clean and descriptive variable names

---

## 🛠️ Setup Instructions

### 🔹 1. Clone or Download the Repository

You can download the `.py` file or clone the project repository to your local machine.

### 🔹 2. Create a Virtual Environment (recommended)

```bash
python -m venv venv
```

## 🔹 3.Activate the Virtual Environment

### Windows

```bash
venv/Scripts/activate
```

### MacOS

```bash
source venv/bin/activate
```

## 🔹 4. Install the required dependencies

```bash
pip install graphics.py
```

## 🔹 5. Run the program

```bash
python progressionReport.py

```

# Declaration

```python
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Author: Senaath Suraweera
# Date: 2024.01.05
```

# References

- [@graphics.py](https://mcsp.wartburg.edu/zelle/python/) by John Zelle: For histogram plotting

- University of Westminster Coursework Specification: [4COSC006C – Software Development I]

## Authors

- [@Senaath-Suraweera](https://www.github.com/Senaath-Suraweera)
