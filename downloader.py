import os
import subprocess
import requests
from PIL import Image

# user explanation fsdffsda
print("INSTRUCTIONs!!! \n Paste a discord message that consists of CUSTOM emojis ONLY with NO SPACES. (ex: <a:example1:1040690867947720755><:example2:1311247090180952074>) \n After that just press enter and it should download them all!! yay!!!")

splitList = []
idList = []

initialMessage = str(input("Input copied message: "))

# ex: <a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010><a:c2:1066546925190520902><a:cf:1066547934088401010><a:c1:1066546842415935518><a:cf:1066547934088401010>

def isAnimatedGif(filepath):
    try:
        with Image.open(filepath) as img:
            if hasattr(img, 'is_animated') and img.is_animated:
                return True
            try:
                img.seek(1)
                return True
            except EOFError:
                return False
    except IOError:
        return False
    return False

def splitter(message):
    editedMessage = message
    while len(editedMessage) > 0:
        i = editedMessage.find(">")
        split = editedMessage[:i+1]
        splitList.append(split)
        editedMessage = editedMessage[i+1:]
        print(split)
    else:
        print("split")
        return editedMessage

def addIdsToList(givenList):
    tempList = []
    for message in givenList:
        editedMessage = message
        editedMessage = editedMessage[:-1]
        editedMessage = editedMessage[-19:]
        print(editedMessage)
        tempList.append(editedMessage)
    return tempList

def downloadList(downloadList):
    for id in downloadList:
        url = f"https://cdn.discordapp.com/emojis/{id}?size=80"
        print("Downloading...")
        response = requests.get(url)
        
        if response.status_code == 200:
            pathName = f"output/emoji_{id}"
            directory = os.path.dirname(pathName)
            if not os.path.exists(directory):
                os.makedirs(directory)
            
            with open(pathName, "wb") as newImage:
                newImage.write(response.content)
                print(f"Saved file emoji_{id}")
                if isAnimatedGif(pathName):
                    newDirectory = os.path.dirname(pathName+".gif")
                    if not os.path.exists(newDirectory):
                        os.makedirs(newDirectory)
                    with open(pathName+".gif", "wb") as finalImage:
                        finalImage.write(response.content)
                else:
                    newDirectory = os.path.dirname(pathName+".png")
                    if not os.path.exists(newDirectory):
                        os.makedirs(newDirectory)
                    with open(pathName+".png", "wb") as finalImage:
                        finalImage.write(response.content)
            os.remove(pathName)
        else:
            print("uhohhh something weent wronggg")
        
initialMessage = splitter(initialMessage)

idList = addIdsToList(splitList)

downloadList(idList)

print("You can close the window now")