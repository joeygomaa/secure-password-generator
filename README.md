# Secure Password Generator

## Description
This program generates cryptographically secure passwords using Python's secrets module. Password length, amount and character types are determined by the user. Every selected character type is guaranteed to appear in every generated password through rejection sampling. The program can support interactive input and command-line arguments simultaneously. 

## Features 
- Cryptographically secure password generation
- Multiple password generation
- Built-in password validation
- Command-line interface (CLI) support 
- Interactive user inputs 
- User input validation 
- Unit-tested functionality  
- Tailored error messages
- Password entropy calculation

## Usage 
### CLI Usage 
Options can be supplied directly through command-line arguments:

```bash
python password_generator.py --length 20 --amount 5 --type low up num sym
```
Available Options:
- `--length` --> Password length
- `--amount` --> Number of passwords to generate 
- `--type` --> Character types to include 
    - `low` = lowercase letters
    - `up` = uppercase letters 
    - `num` = numbers 
    - `sym` = symbols 

Arguments can also be provided partially. Missing arguments will be requested interactively. 

### Interactive Input Usage 
To use the program interactively run the program through the terminal:

```bash
python password_generator.py
```
The program will prompt for the amount of passwords, length of the passwords and character types. 

## Security
Password characters are selected using Python's `secrets` module. The `secrets` module provides cryptographically secure randomness intended for security sensitive applications. The generator uses rejection sampling to guarantee that every character type appears at least once in every generated password. A complete password is generated from the combined character pool and is rejected and regenerated if it does not meet the selected character-type requirements.

## Testing 
The program uses Python's built-in `unittest` framework to test score functions critical to the generator's functionality. The tests can be run as follows:
```bash
python -m unittest
```
For more detailed output:
```bash 
python -m unittest -v
```
## Requirements 
- Python 3.11 or later 
- No external dependencies 

## Project Structure 
password_generator.py       # Main application 
test_password_generator.py  # Unit tests
README.md                   # Project documentation