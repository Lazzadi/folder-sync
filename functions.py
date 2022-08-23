import os
import datetime
import pathlib

def timeModified(path):

    file = pathlib.Path(path)

    # get modification time
    timestamp = file.stat().st_mtime

    # convert timestamp to dd-mm-yyyy hh:mm:ss
    time = datetime.datetime.fromtimestamp(timestamp)
    return(time)

# #Function should create a dictionary with Key:file-name, value:date modified
# def scanFolder(folder):
#     list = os.listdir(folder)
#     list.sort()
#     return list

# #Function writes changes in log folder
# def logFolder(folder):
#     os.chdir(folder)
#     log = open('log.txt', 'a')
#     # log.write what changes were made to source
#     log.write('Hello World')
#     log.close()

# #Function copies changed files from Source to Replica
# def synchronise(folderS, folderR):
#     pass

