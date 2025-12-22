# The Cookie Clicker Bot

It's pretty self explanatory on what it is. The script opens up an instance of Cookie Clicker, and automates cookie clicking, upgrade purchases and building purhcases. The app comes with a basic GUI with an on/off switch, a keybind, and logs.
This project was made for Hack Club's YSWS Haxmas Day 8.

## How to use the bot

### Installation

For this script, you will require pip, at least Python 3.13, Google Chrome, and any editor of choice. (I recommend VSCode)

Download the main.py file into a new folder in your file manager. You can name the folder whatever you like.

<img width="1700" alt="Download main.py" src="https://github.com/user-attachments/assets/85e87342-1d02-42f1-9b54-195ddc0a413e" />
<img width="1700" alt="File Manager" src="https://github.com/user-attachments/assets/116cd9ea-4575-4469-a08a-489a44080852" />

### Set-Up

#### Virtual Environment (venv)

Open the folder in your editor:

<img width="1700" alt="VSCode" src="https://github.com/user-attachments/assets/61273380-3fec-41ee-8350-a824d2f90baf" />

<br>Now we need to open a virtual environment (venv).

In the top search bar (command palette):
- type `>Python: Create Environment` and hit enter
- select "Venv"
- select your current version of Python (recommended is 3.13+)

The above guide is for VSCode users. For other editors, search up how to create a virtual environment.

You should then have a new folder in your workspace called ".venv".

<img width="1700" alt=".venv" src="https://github.com/user-attachments/assets/74aba902-32db-46df-8aa7-53e61a64d5a4" />

#### Selenium Installation

<br> Next, we need to install Selenium in our venv. Selenium is a python package that can open up the web and run commands in it.
To install Selenium, first we need to open up the terminal in the editor. The method to do this may vary across editors, so make sure to search up how to do this if this tutorial is unclear.
1. In the command palette, type `>Create New Terminal (with profile)` and hit enter.
2. A terminal should pop up. Make sure that the beginning of the command line has (.venv). If not, type:
   - `source .venv/bin/activate` if you are on macOS/Linux, or
   - `.venv/Scripts/activate.bat` if you are on Windows.
<br>If you are already in (.venv), you can skip this step.
3. In the terminal, type `pip install selenium` and hit enter.
4. Wait until Selenium has finished installing.

<img width="1700" alt=".venv terminal" src="https://github.com/user-attachments/assets/b879752f-5c46-481e-a597-e4dfca92f9e7" />

#### Running the bot
Open up the terminal in your editor (see [Selenium Installation](#selenium-installation) on how to open terminal), type "python3.13 main.py" and hit enter.
After a few seconds, you should be redirected to a new Chrome window opening up Cookie Clicker. Wait a few more seconds, and the language will be auto selected to English and a new window will open up. The new window is the interface to turn the bot on and off. The keybind to turn the bot on/off is Ctrl+D.

## Updates

Updates to be expected:

- Custom keybinds
- CPS tracking
- Custom interval
- And more!

## Releases
_v1.01:_
<br>GUI update

- Added GUI using tkinter
  - On/off switch
  - Ctrl+D keybind
  - Logs

_v1.00:_
<br>Initial release

- Added automated upgrade purchases
- Added automated English language selection

_Beta:_
<br>Made with [Haxmas Day 8 tutorial](https://haxmas.hackclub.com)

- Added automated cookie clicking
- Added automated building purhcases
