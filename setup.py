from os import mkdir, listdir, system
#to test if existing:
try:
    import dropbox
except:
    ans = input("Can't import module dropbox. Install with pip3 (Yes/No)? ")
    if ans == "Yes":
        system("pip3 install dropbox")
    elif ans == "No":
        print("Abort.")
        quit()
    else:
        ans = input("Please type 'Yes' or 'No': ")
        if ans == "Yes":
            system("pip3 install dropbox")
        else:
            print("Abort.")
            quit()
    quit()
import lib

#set up settings.py
apiKey = '"' + input("Please enter your DropBox API-Key (OAuth): ") + '"'
print("Writing settings.py...", end="")
settings = open("settings.py", "w")
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
