import glob
import string
import os
import shutil

def main():
    print("Please enter a working directory; starting with '/' and eding with '/'")
    currentDir = "/Users/alexpelletier/Desktop/royalties/"
    currentDir = raw_input(">>>")
    filesToSort = trimListOfFile(glob.glob(currentDir + "staging/*.pdf"))
    endFolders = trimListOfFile(glob.glob(currentDir + "statements/*"))

    all=string.maketrans('','')
    nodigs=all.translate(all, string.digits)

    if not os.path.exists(currentDir):
        print("Invalid Path!\n\n")
        return
    if not os.path.exists(currentDir + "filed"):
        os.makedirs(currentDir + "filed")

    
    fileCnt = 0
    moveCnt = 0
    totalMoveCnt = 0
    
    for i in filesToSort:
        #get year
        year = i.translate(all, nodigs)
        year = year[(len(year)-4):]

        #guess folder to move to
        foldersToMoveTo = []
        for folder in endFolders:
            if folder in i.replace("_","-"):
                foldersToMoveTo.append(folder)

        #get right folder to move to
##        print("Moving to: " + str(foldersToMoveTo))
##        guessedFolder = i.split("-")[0].replace(".pdf","")
##        print("Guess: " + guessedFolder)
##        userFolders = raw_input(">>>")
##        if "-1" in userFolders:
##            foldersToMoveTo.append(guessedFolder)
##            userFolders.replace("-1","")
##        if userFolders.replace(" ", "") != "":
##            for folder in userFolders.replace(" ", "").split(","):
##                foldersToMoveTo.append(folder)

        if len(foldersToMoveTo) > 0:
            for folder in foldersToMoveTo:
                if not os.path.exists(currentDir + "statements/" + folder):
                    os.makedirs(currentDir + "statements/" + folder)
                if not os.path.exists(currentDir + "statements/" + folder + "/" + str(year)):
                    os.makedirs(currentDir + "statements/" + folder + "/" + str(year))
                src = (currentDir + "staging/" + i).lower()
                dst = (currentDir + "statements/" + folder + "/" + str(year) + "/" + i).replace("_","-").lower()
                if folder == foldersToMoveTo[-1]:
                    shutil.copyfile(src, dst)
                else:
                    shutil.copyfile(src, dst)
                totalMoveCnt += 1
            src = (currentDir + "staging/" + i).lower()
            dst = (currentDir + "filed/" + i).replace("_","-").lower()
            shutil.move(src, dst)
            moveCnt += 1
            print("Moved: " + i)
            
        fileCnt += 1

    print("\n\nFiles Parsed: " + str(fileCnt))
    print("Files Moved: " + str(moveCnt))
    print("Total File Moves: " + str(totalMoveCnt))
    print("Done")               
        
        
    
def trimListOfFile(ls):
    ret = []
    for i in ls:
        ret.append(basename(i))
    return ret
def basename(filename):
    return filename.split("/")[-1].lower()


while 1:    
    main()
