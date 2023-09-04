# Password Manager

[![Latest release](https://badgen.net/github/release/Naereen/Strapdown.js)](https://github.com/INF331-tarea1/tarea-1/releases) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)

## Members

- Adolfo Espinosa
- Bayron Valenzuela

## Description

This password manager is a software application designed to help users securely and conveniently manage and protect their passwords. This application allows users to store, generate, and retrieve passwords securely, all under the control of a master password. This project was built as an assignment for the Software Testing course at Universidad Técnica Federico Santa Maria.

## Installation

This software is designed to use on Windows.

There are two options:

- Download the latest release for console execution; no additional packages need to be downloaded.
- Download the [source code](https://github.com/INF331-tarea1/tarea-1), in `<>Code` you can download the ZIP file, or you can clone the repository. For this, you will need to have installed python 3.10+
  Then you need to install some packages, you have to open a console in the main directory of the project, where `requirements.txt` is located, and run this command to install the required dependencies: `pip install -r requirements.txt`, or `pip3 install -r requirements.txt`.
  Once installed the required dependencies, you are ready to use it with `python main.py`, or `python3 main.py`.

## How to Use

Once the password manager is installed, when you run it, it will prompt you for a master password. This master password will be required every time the program is executed. After entering the master password, a menu with various options will be displayed on the screen. Write the number of the desired option to access it and follow the instructions provided by the software.

You can't create a new master password, so make sure to remember it. If you forget it, you will lose all your passwords, as the only way to continue using the program is by manually deleting the database.db file created by the program. If you delete that file, all the passwords saved will be lost and the program will ask you to enter your new master password.

## How to Contribute

If you wish to contribute, you can follow the next steps:

- Fork the repository from the "Fork" button in the upper-right corner.
- Clone the forked repository
  - Click the `<> Code` button on the forked repository, copy the URL obtained by clicking the copy button on the HTPS menu.
  - Then, to clone you need to have a recent git version, and run the next command:
    `git clone <URL>`
- Create a branch on the repository with a meaningful name, by running inside the project's folder:
  `git checkout -b <branch_name>`

- Now you can make all the changes needed.
- When you're done adding or changing code, you have to commit and push your changes with:
  ```
  git add.
  git commit -m "<commit_message>"
  git push origin <branch_name>
  ```
- Now you have to create a pull request, you can do that on your forked repository main page, click the "Compare & pull request" button.
  You will need to provide some details about the changes, once this details are provided, you can create the pull request and the maintainers of the code will decide whether to accept the pull request or not.

For bug or error reports, create an issue by clicking [here](https://github.com/INF331-tarea1/tarea-1/issues/new). Please be as detailed as possible with the bug or error.
