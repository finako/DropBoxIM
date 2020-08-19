# DropBoxIM
Instant-Messaging in chat-rooms with Python 3 and DropBox.
## Files
- *chat.py*  main program
- *lib.py*  functions and classes used by the program
- *(example_)settings.py*  where settings for chat.py are stored
- *setup.py*  setup assistant; helps generating settings.py, chat_data/ and validates install
## Dependencies
- a [DropBox-Account](https://www.dropbox.com/) and an [Dropbox-Developer-App](https://www.dropbox.com/developers/apps/create)
- [Python 3](https://www.python.org)
- module *dropbox* ([PyPI](https://pypi.org/project/dropbox/)) from the PyPI
## Setup
1. make sure you installed _dropbox_
2. set up an [DropBox-App](https://www.dropbox.com/developers/apps/create) and generate an OAuth access token
3. clone this repository to your computer and change the working directory to the folder
4. launch setup.py, follow instructions
5. people you want to chat with must use an access token **for the same app**
## Usage
1. start the program with `python3 chat.py` or by double-clicking it on Windows
2. enter your name
3. You'll be prompted to enter the number of the chat-room you're using. To chat with others, you must use the same number.
4. If you want to write a message, press `CTRL-C`. After you typed in your message, press `RETURN`. The program will now send your message. **Don't press `CTRL-C` while the program is sending the message!**
5. to exit, press `CTRL-C` again
