import os
from functions import scanFolder, synchronise, timeModified
import datetime
import pathlib
import shutil

# print(timeModified('/home/l/Documents/repos/folder-sync/folder-sync/Source/log.txt'))



# print(scanFolder('/home/l/Documents'))
# print(timeModified('/home/l/Documents/repos/folder-sync/folder-sync/Source/log.txt'))

synchronise('/home/l/Documents/repos/folder-sync/folder-sync/Source', '/home/l/Documents/repos/folder-sync/folder-sync/Replica')

# scanFolder('/home/l/Documents/repos/folder-sync/folder-sync/Source')
