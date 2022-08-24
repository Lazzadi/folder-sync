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


def synchronise(folderSource, folderReplica):
    
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

              
        if found == False:
            extensionRegex = re.compile(r'(?<=Source).*$')
            extension = extensionRegex.findall(shortPathSource)
            print(extension)
            try:
                os.makedirs(folderReplica + extension[0])
            except:
                pass
            shutil.copy2(filePathSource, folderReplica + extension[0])






    
    # for filePathSource, dataSource in contentSource.items():
    #     found = False
    #     fileNameSource = dataSource[0]
    #     dateModifiedSource = dataSource[1]
    #     for filePathReplica, dataReplica in contentReplica.items():
    #         fileNameReplica = dataReplica[0]
    #         dateModifiedReplica = dataReplica[1]
    #         if(fileNameSource == fileNameReplica):
    #             found = True
    #             if(dateModifiedSource != dateModifiedReplica):
    #                 shutil.copy2(os.path.join(filePathSource, fileNameSource), folderReplica)
    #     if found == False:
    #         shutil.copy2(os.path.join(filePathSource, fileNameSource), folderReplica)
            
    
    # contentReplica = scanFolder(folderReplica)
    
    # for filePathReplica, dataReplica in contentReplica.items():
    #     fileNameReplica = dataReplica[0]
    #     found = False
    #     for dataSource in contentSource.values():
    #         fileNameSource = dataSource[0]
    #         if fileNameReplica == fileNameSource:
    #             found = True
    #             # print(found)
    #     if found == False:
    #         os.remove(filePathReplica)
    






        


# #Function writes changes in log folder
# def logFolder(folder):
#     os.chdir(folder)
#     log = open('log.txt', 'a')
#     # log.write what changes were made to source
#     log.write('Hello World')
#     log.close()



