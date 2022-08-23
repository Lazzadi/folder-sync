import os
import datetime
import pathlib
import shutil

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
                filePath = path + '/' + fileName
                time = str(timeModified(filePath))
                content[filePath] = [fileName, time]
                # print(str(content.keys()))
    return content

# #Function copies changed files from Source to Replica
# Three situations: New files, deleting files and changing files
def synchronise(folderSource, folderReplica):
    
    contentSource = scanFolder(folderSource)
    contentReplica = scanFolder(folderReplica)
    
    for filePathSource, dataSource in contentSource.items():
        found = False
        fileNameSource = dataSource[0]
        dateModifiedSource = dataSource[1]
        for filePathReplica, dataReplica in contentReplica.items():
            fileNameReplica = dataReplica[0]
            dateModifiedReplica = dataReplica[1]
            if(fileNameSource == fileNameReplica):
                found = True
                if(dateModifiedSource != dateModifiedReplica):
                    shutil.copy2(filePathSource, folderReplica)
        if found == False:
            shutil.copy2(filePathSource, folderReplica)
    
    contentReplica = scanFolder(folderReplica)
    
    for filePathReplica, dataReplica in contentReplica.items():
        fileNameReplica = dataReplica[0]
        found = False
        for dataSource in contentSource.values():
            fileNameSource = dataSource[0]
            if fileNameReplica == fileNameSource:
                found = True
                # print(found)
        if found == False:
            os.remove(filePathReplica)
    






        

###
#Scan Source
#Scan Replica
#Take one file in source and check if it can be found in replica
    #if it can be found in replica check if it has the same timestamp. 
    #if it has the same timestamp do nothing
    #if it has a different timestamp find file in replica and delete it then add file in source to replica
    #if it can't be found in Replica add file from source to replica
    #to check for deleted items we will look in replica and compare to Source. If we have a file in Replica that is not in source, we remove that file from replica
    #maybe sort after last modified date. Save last modified date from latest sync iteration in a temp variable and only check until final . 
###                 

# #Function writes changes in log folder
# def logFolder(folder):
#     os.chdir(folder)
#     log = open('log.txt', 'a')
#     # log.write what changes were made to source
#     log.write('Hello World')
#     log.close()



