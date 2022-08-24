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

#Function should create a dictionary with Key:file-name, value:date modified
def scanFolder(folder):
    content = {}
    for path, _, fileList in os.walk(folder):
        for fileName in fileList:
            time = str(timeModified(os.path.join(path, fileName)))
            content[os.path.join(path, fileName)] = [fileName, time, path]
    return content


def synchronise(folderSource, folderReplica, logPath):
    
    contentSource = scanFolder(folderSource)
    contentReplica = scanFolder(folderReplica)

    # print(contentSource)

    #Checking if the Source folder has any new files
    for filePathSource, dataSource in contentSource.items():
        
        fileNameSource = dataSource[0] # taking file name from content
        dateModifiedSource = dataSource[1] # taking date modified from content
        shortPathSource = dataSource[2]
        found = False

        for filePathReplica, dataReplica in contentReplica.items():
            fileNameReplica = dataReplica[0]
            dateModifiedReplica = dataReplica[1]
            shortPathReplica = dataReplica[2]

            if(fileNameSource == fileNameReplica):
                pass
                found = True
                if dateModifiedSource != dateModifiedReplica:
                    extensionRegex = re.compile(r'(?<=Source).*$')
                    extension = extensionRegex.findall(shortPathSource)
                    try:
                        os.makedirs(folderReplica + extension[0])
                    except:
                        pass
                    shutil.copy2(filePathSource, folderReplica + extension[0])
                    message = str(datetime.datetime.now()) + ': ' + fileNameReplica + ' was modified in ' + folderReplica + extension[0]
                    print(message)
                    logFolder(logPath, message)

              
        if found == False:
            extensionRegex = re.compile(r'(?<=Source).*$')
            extension = extensionRegex.findall(shortPathSource)
            try:
                os.makedirs(folderReplica + extension[0])
            except:
                pass
            shutil.copy2(filePathSource, folderReplica + extension[0])
            message = str(datetime.datetime.now()) + ': ' + fileNameSource + ' was created in ' + folderReplica + extension[0]
            print(message)
            logFolder(logPath, message)

    #There are going to be changes in replica so we scan it again before removing any files
    contentReplica = scanFolder(folderReplica)
    

    #removes from replica files no longer in  source
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



# #Function writes changes in log folder
def logFolder(path, message):
    os.chdir(path)
    log = open('log.txt', 'a')
    log.write('\n' + message)
    log.close()


