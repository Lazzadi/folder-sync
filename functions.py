import os
import datetime
import pathlib
import shutil
import re

def timeModified(path):

    file = pathlib.Path(path)

    # get modification time
    timestamp = file.stat().st_mtime

    # convert timestamp to dd-mm-yyyy hh:mm:ss
    time = datetime.datetime.fromtimestamp(timestamp)

    return(time)

#Function creates a dictionary with Key: file path, value: file name, time, file folder
def scanFolder(folder):
    content = {}
    for path, _, fileList in os.walk(folder):
        for fileName in fileList:
            time = str(timeModified(os.path.join(path, fileName)))
            content[os.path.join(path, fileName)] = [fileName, time, path]
    return content

# #Function writes changes in log folder
def logFolder(path, message):
    os.chdir(path)
    log = open('log.txt', 'a')
    log.write('\n' + message)
    log.close()

def synchronize(folderSource, folderReplica, logPath):
    
    contentSource = scanFolder(folderSource)
    contentReplica = scanFolder(folderReplica)

    for filePathSource, dataSource in contentSource.items(): #Checking if Source folder has any new files
        
        fileNameSource = dataSource[0] # taking file name from content
        dateModifiedSource = dataSource[1] # taking date modified from content
        shortPathSource = dataSource[2] # taking file path without file name
        found = False

        for filePathReplica, dataReplica in contentReplica.items():
            fileNameReplica = dataReplica[0]
            dateModifiedReplica = dataReplica[1]
            shortPathReplica = dataReplica[2]

            #Checking if file exists anywhere in folder structure
            if(fileNameSource == fileNameReplica):
                pass
                found = True
                if dateModifiedSource != dateModifiedReplica: #If file exists, we check if it was modified by checking the last time files were changed
                    extensionRegex = re.compile(r'(?<=Source).*$') #Regex is used to create subfolder paths in the Replica folder
                    extension = extensionRegex.findall(shortPathSource)
                    try:
                        os.makedirs(folderReplica + extension[0])
                    except:
                        pass
                    try:
                        shutil.copy2(filePathSource, folderReplica + extension[0]) #shutil.copy2 method ensures file is copied along with metadata
                    except:
                        print("User is still modifying files. Please wait...")
                    message = str(datetime.datetime.now()) + ': ' + fileNameReplica + ' was modified in ' + folderReplica + extension[0]
                    print(message)
                    logFolder(logPath, message)

        #If file is not found then it is created from scratch      
        if found == False:
            extensionRegex = re.compile(r'(?<=Source).*$')
            extension = extensionRegex.findall(shortPathSource)
            try:
                os.makedirs(folderReplica + extension[0])
            except:
                pass
            try:
                shutil.copy2(filePathSource, folderReplica + extension[0])
            except:
                print('User is modifying file while synchronization is taking place. Please wait')

            message = str(datetime.datetime.now()) + ': ' + fileNameSource + ' was created in ' + folderReplica + extension[0]
            print(message)
            logFolder(logPath, message)

    #There are going to be changes in replica so we scan it again before removing any files
    contentReplica = scanFolder(folderReplica)
    

    #Loop checks for files in replica that are no longer in source and removes them
    for filePathReplica, dataReplica in contentReplica.items():
        fileNameReplica = dataReplica[0]
        found = False
        for dataSource in contentSource.values():
            fileNameSource = dataSource[0]
            if fileNameReplica == fileNameSource:
                found = True
        if found == False:
            os.remove(filePathReplica)
            message = str(datetime.datetime.now()) + ': ' + fileNameReplica + ' was deleted from ' + filePathReplica
            print(message)
            logFolder(logPath, message)