# 🔐 Python Password Generator

A simple and secure password generator built using Python's `secrets` module. Generate customized passwords using alphabets, numbers, and special characters.

The project provides a Streamlit-based user interface as well as a reusable Python package that can be imported into other Python applications.

**GitHub Repository:**  
[Python Password Generator](https://github.com/enileshk/Python/tree/main/Password%20Generator)

## 🚀 Features

- Generate cryptographically secure random passwords.
- Customize the number of:
  - Uppercase and lowercase letters
  - Numeric characters
  - Special characters
- Password length validation (minimum 8 and maximum 128 characters).
- Password strength estimation:
  - Weak
  - Medium
  - Strong
  - Very Strong
- Simple Streamlit-based user interface.
- Reusable Python package for integration into other projects.
- No external dependencies required for the core password generator.

## 🛠️ Technology Stack

- **Python 3.8+**
- **Streamlit** – User interface
- **Secrets** – Cryptographically secure random generation
- **String** – Character sets
- **Math** – Password entropy estimation

## 📥 Download and Installation

### Step 1: Download the Project

1. Visit the [GitHub repository](https://github.com/enileshk/Python/tree/main/Password%20Generator).
2. Click the green **Code** button.
3. Select **Download ZIP**.
4. Extract the downloaded ZIP file.

### Step 2: Open the Project

Open the extracted `Password Generator` folder using PyCharm, VS Code, or your preferred Python IDE.

### Step 3: Install Dependencies

If you want to run the Streamlit application, open the terminal inside the project folder and execute:

```bash
pip install -r requirements.txt
```

## 🖥️ Option 1: Run the Streamlit Application

Execute:

```bash
streamlit run app.py
```

The application will automatically open in your default web browser.

You can generate passwords by specifying the required number of letters, numbers and special characters.

## 🐍 Option 2: Use the Python Package Independently

You can use the password generator package directly in your own Python projects without running the Streamlit application.

The core package uses Python built-in modules and does not require Streamlit or any other external dependency.

### Package Structure

```text
password_generator/
│
├── __init__.py
└── generator.py
```

**1. generator.py – Core Module**

Contains the main password-generation functionality and supporting functions:

| Function | Description |
|---|---|
| `generate_password()` | Generates a secure random password |
| `validate_length()` | Validates character counts and total password length |
| `estimate_strength()` | Estimates password strength and entropy |

**2. __init__.py – Package Initialization**

Exposes the functions from `generator.py` at the package level, allowing users to import them directly:

```python
from password_generator import generate_password, estimate_strength
```

### Example: Generate a Password

Create a Python file, for example `my_password.py`, in the project directory:

```python
from password_generator import generate_password

password = generate_password(
    letters=8,
    numbers=4,
    special=4
)

print("Generated Password:", password)
```

### Example: Generate and Estimate Password Strength

```python
from password_generator import generate_password, estimate_strength

password = generate_password(
    letters=8,
    numbers=4,
    special=4
)

result = estimate_strength(password)

print("Generated Password:", password)
print("Password Strength:", result["strength"])
print(result["message"])
```

### Importing Individual Functions

Users can also import only the functions they need:

```python
from password_generator import generate_password
```

Or import the module directly:

```python
from password_generator import generator

password = generator.generate_password(10, 4, 2)
print(password)
```

### Function Parameters

`generate_password(letters=8, numbers=4, special=4)`

| Parameter | Description | Default |
|---|---|---:|
| `letters` | Number of alphabetic characters | 8 |
| `numbers` | Number of numeric characters | 4 |
| `special` | Number of special characters | 4 |

**Password length rules:**
- Minimum combined length: 8 characters.
- Maximum combined length: 128 characters.
- Individual character categories can have a count of zero, provided the combined length is valid.
- Negative character counts are not allowed.

## 🔒 Security

This project uses Python's built-in `secrets` module instead of the standard `random` module.

The `secrets` module is designed to generate cryptographically strong random values, making it suitable for password generation.

**Note:** Password strength is an approximate estimate based on password length and character diversity. It is not a guarantee against password cracking.

## 📁 Complete Project Structure

```text
Password Generator/
│
├── password_generator/
│   ├── __init__.py
│   └── generator.py
│
├── app.py
├── example.py
├── README.md
├── requirements.txt
└── pyproject.toml
```

## 👨‍💻 Author

**Nilesh Kulkarni**

GitHub: [enileshk](https://github.com/enileshk)

**Project Repository:**  
[Python Password Generator](https://github.com/enileshk/Python/tree/main/Password%20Generator)
