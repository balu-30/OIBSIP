# Random Password Generator

This is a simple Random Password Generator that I developed as part of my **Oasis Infobyte Python Programming Internship**.

The application allows users to create passwords by choosing the password length and the types of characters they want to use. It is built as a small Flask web application so that it can be used through a browser.

## What the project does

* Generates passwords with a minimum length of 8 characters.
* Allows the user to choose:

  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* Generates a normal random password using Python's `random` module.
* Generates a more secure password using Python's `secrets` module.
* Provides a button to copy the generated password.
* Allows the user to generate another password whenever needed.
* Has a simple web interface using HTML, CSS and JavaScript.

## Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* `random` module
* `secrets` module

## Project Structure

```text
Python-Task3-RandomPasswordGenerator/
│
├── app.py
├── requirements.txt
├── README.md
│
└── Web/
    ├── index.html
    ├── style.css
    └── script.js
```

## How to Run

First, install the required package:

```bash
pip install -r requirements.txt
```

Then run the application:

```bash
python app.py
```

After the server starts, open this address in your browser:

```text
http://127.0.0.1:5000
```

## How to Use

1. Enter the password length. The minimum length is 8 characters.
2. Select the character types you want in the password.
3. Click the generate button.
4. The generated password will be displayed on the page.
5. Use the copy button if you want to copy the password.
6. Generate another password whenever required.

## Purpose of the Project

The main purpose of this project was to practice Python programming and learn how to connect Python logic with a simple web application using Flask.

It also helped me understand password generation using both the `random` and `secrets` modules.

## Internship

This project was completed as part of the **Oasis Infobyte Python Programming Internship**.

**Task:** Random Password Generator
