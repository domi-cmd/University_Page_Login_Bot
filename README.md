# University Page Login Bot

This repository contains a Python Selenium bot designed to automate logging into the university portal of the University Of Bern. The bot uses credentials stored in a `credentials.txt` file and requires a specific setup before running.

## Table of Contents 📚

- [Setup Guide](#setup-guide)
- [How to Run](#how-to-run)
- [File Structure](#file-structure)
- [License](#license)

## Setup Guide

Before you can run the bot, follow these steps to configure it:

### 1. Adjust the Path in `ilias.bat` 🛠️

The `.bat` file `ilias.bat` in the root folder needs to be adjusted to match your project setup. Specifically, make sure the path to your `ilias.py` script is correct.

- Open the file `ilias.bat`.
- Ensure that the line with the `python` command points to the correct location of `ilias.py` on your system. The current line looks like this:

```batch
cd C:\Users\Domi\Documents\Personal_Projects\University_Page_Login_Bot\code
```
Change "C:\path\to\your\ilias.py" to the correct directory in which ilias.py is located on your machine.

### 2. Create the credentials.txt File 📝
You need to create a credentials.txt file to store your username and password for the bot. Follow these steps:

Create a new text file named credentials.txt.

Save it in the code/ directory (i.e., root/code/credentials.txt).

The contents of the credentials.txt file must follow this format:

```
username=your_username_here
password=your_password_here
```
Replace your_username_here with your actual username, and your_password_here with your actual password.

*Important Notes:*
- The credentials.txt file must be saved in the code/ folder (i.e., root/code/credentials.txt).
- Ensure the file contains only two lines, one for the username and one for the password.
- The file should not be tracked by version control, and it is included in the .gitignore to prevent sharing your credentials.

### 3. Add credentials.txt to .gitignore 🚫
To ensure your credentials.txt file does not get pushed to a public repository, make sure it is added to .gitignore. If it's not already added, follow these steps:

Open the .gitignore file in the root directory.

Add the following line to ignore credentials.txt:
```
code/credentials.txt
```
This ensures that your credentials file will not be tracked by Git.

### 4. Add Root Folder to Your System Variables 🖥️
This allows for easy starting of the bot via terminal from anywhere (any directory). If you choose to skip this step, you will have to navigate to the bots root directory (this repository) every time you want to boot it up.
Press WindowsKey + S, then type 
```
Edit System Variables
```
Then under edit, go to the system section of the variable, click on the one labeled path, and press edit. Once there, add the absolute path to the root of this repo. For me, this looks as follows;
```
C:\Users\Domi\Documents\Personal_Projects\University_Page_Login_Bot\
```

## How to Run
Once the setup is complete, you can run the bot using the following steps:

Open a command prompt or terminal.

Enter
```
ilias
```

If you chose to omit adding the root folder of this repo to your system variables, you will have to first navigate to the root directory of the project in the terminal.
Then you can also boot up the bot by typing
```
ilias
```

This will execute the bot and automate the login process using the credentials you provided.

## File Structure
Here is the basic structure of the repository:

```
University_Page_Login_Bot/
├── code/
│   ├── ilias.py           # The main Python script that runs the bot
│   ├── credentials.txt    # Contains the username and password (not tracked by git)
├── ilias.bat              # Batch file to run the Python script
├── .gitignore             # Files that are ignored by Git (e.g., credentials.txt)
├── README.md              # This file
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
