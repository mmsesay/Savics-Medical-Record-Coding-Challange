# Savics-Medical-Record-Coding-Challange
This is a medical record coding challange for junior developer

## Prerequisites
Below are the tools you need to have in order to execute this program:
1. Python:
    - Installation for windows
        - Download the Python 3 Installer
        - Open a browser window and navigate to https://www.python.org/downloads/windows/ or at https://www.python.org/.
        - Underneath the heading at the top that says Python Releases for Windows, click on the link for the Latest Python 3 Release - Python 3.x.x. (As of this writing, the latest is Python 3.6.5.)
        - Scroll to the bottom and select either Windows x86-64 executable installer for 64-bit or Windows x86 executable installer for 32-bit. (See below.)
        - run the installer

    - Installation for Python
        - There is a very good chance your Linux distribution has Python installed already, but it probably won’t be the latest version, and it may be Python 2 instead of Python 3.
        - To find out what version(s) you have, open a terminal window and try the following commands:
            ```python --version```
            ```python2 --version```
            ```python3 --version```

        - If no python version dispaly, open your terminal ```CTRL + ALT + T``` and type the following commands:
        ```sudo add-apt-repository ppa:jonathonf/python-3.7```
        ```sudo apt-get update```
        ```sudo apt-get install python3.7```

    - Installation for macOS / Mac OS X
        - Well the current versions of macOS include a version of Python 2 but still follow the process to install the python 3.
        - Open a browser and navigate to http://brew.sh/. After the page has finished loading, select the Homebrew bootstrap code under “Install Homebrew”. Then hit Cmd+C to copy it to the clipboard. Make sure you’ve captured the text of the complete command because otherwise the installation will fail.
        - Now you need to open a Terminal.app window, paste the Homebrew bootstrap code, and then hit Enter. This will begin the Homebrew installation.
        - If you’re doing this on a fresh install of macOS, you may get a pop up alert asking you to install Apple’s “command line developer tools”. You’ll need those to continue with the installation, so please confirm the dialog box by clicking on “Install”.
        - Confirm the “The software was installed” dialog from the developer tools installer.
        - Back in the terminal, hit Enter to continue with the Homebrew installation.
        - Homebrew asks you to enter your password so it can finalize the installation. Enter your user account password and hit Enter to continue.
        - Depending on your internet connection, Homebrew will take a few minutes to download its required files. Once the installation is complete, you’ll end up back at the command prompt in your terminal window.
        - Once Homebrew has finished installing, return to your terminal and run the following command:
        ```$ brew install python3```

2. Clone the repo and cd into it
3. Run the command ```python app.py```
