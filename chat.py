#! /usr/bin/python3
#import
import dropbox
from dropbox.files import WriteMode
import time
from os import system, popen, listdir
from contextlib import suppress
from lib import *
import settings

#function definitions
def db_upload(file, destination):
    with open(file, 'rb') as f:
        db.files_upload(f.read(), destination, mode=WriteMode('overwrite'))

def db_ls(directory):
    for entry in db.files_list_folder(directory).entries:
        yield entry.name

#declare variables and so
db = dropbox.Dropbox(settings.apiKey)
name = input("Your name (Letters and numbers only): ").strip()
if not isOnly(name, "abcdefghijklmnopqrstuvwxyz0123456789", False):
    print("Please use only letters from a-z and A-Z and digits!")
    exit
chatRoom = int(input("Number of the chat-room (0 for standard value): "))
if chatRoom == 0:
    chatRoom = settings.standardChatRoom
tmp = settings.tmpFolder + name + settings.tmpFileEnding.replace("ROOM", str(chatRoom))
dbFile = "/" + name + settings.chatFileEnding.replace("ROOM", str(chatRoom))
dbChatFilesEnding = settings.chatFileEnding.replace("ROOM", str(chatRoom))
dbDestination = settings.dropboxDestination

#empty the local chat (tmp) file
with open(tmp, "w") as f:
    f.write("")

#main loop
system("clear")
while True: #receive, sort and print out messages; send messages by pressing ctrl-c
    try:
        #receive and filter
        for file in db_ls(dbDestination):#list folder contents
            if not ".chat" in file:#filter for *.chat* files
                continue
            with open(settings.tmpFolder+file, "wb") as f:#download files
                metadata, res = db.files_download(path="/"+file)
                f.write(res.content)
                del metadata
        chatFilesList = []
        for entry in listdir(settings.tmpFolder):#filter files in local tmp folder
            if not ".chat" in entry:
                continue
            chatFilesList.append(settings.tmpFolder+entry)#append *.chat* files to a list

        sorted_msg = sortieren(erzeuge_nachrichtenliste(*chatFilesList))#sort every message from every file in the list by time
        if sorted_msg:#if there are messages, print them
            system("clear")
            for element in sorted_msg:
                print(sonderzeichen(element.gesamt()), end="")
    except KeyboardInterrupt:#toggle send prompt by pressing ctrl-c, pressing it one more time will exit the program
        try:
            time.sleep(0.01)
            print("\r\r", end="")#set cursor position
            text = input('>>')#prompt
            t = time.strftime('%T')#get time
            with open(tmp, "a") as message:#write message to tmp-file, format: time;name::message,\n
                message.write(t + name + "::" + entferne_sonderzeichen(text) + "\n")
            print("Senden...")
            db_upload(tmp, dbFile)#upload tmp-file as .chat-file
        except KeyboardInterrupt:#exit program when pressing ctrl-c 2 times
            print("\rGoodbye...")
            exit()
