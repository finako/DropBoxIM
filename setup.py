from os import mkdir, listdir
import dropbox, lib #to test if existing

settings = open("settings.py", w)
print("Welcome to the setup!\n")

#set up settings.py
apiKey = '"' + input("Please enter your DropBox API-Key (OAuth): ") + '"'
print("Writing settings.py...", end="")
print("apiKey="+apiKey+" #your OAuth-Token for the Dropbox API", file=settings)
print('tmpFileEnding=".tmpROOM" #file ending for local tmp files, ROOM will be replaced with the number of the chat-room\nchatFileEnding=".chatROOM" #file ending for chat files on DropBox, ROOM will be replaced with the number of the chat-room\ntmpFolder="chat_data/" #folder location for all tmp- and chat-files\ndropboxDestination="" #where to write on dropbox, "" is for the root / -folder\nstandardChatRoom=1 #standard chat room to enter', file=settings)
print("done")

#create chat_data/
print("Creating folder structure...", end="")
mkdir("chat_data")
print("done")

#validate setup
if "chat_data" and "settings.py" in listdir():
    print("Success!")
else:
    print("Failed.")
