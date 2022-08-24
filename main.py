import os
from functions import scanFolder, synchronise, timeModified
import datetime
import pathlib
import shutil
import re

source = '/home/l/Documents/repos/folder-sync/folder-sync/Source'
replica = '/home/l/Documents/repos/folder-sync/folder-sync/Replica'
logPath = '/home/l/Documents/repos/folder-sync/folder-sync'

# print(timeModified('/home/l/Documents/repos/folder-sync/folder-sync/Source/log.txt'))


# scanFolder(source)

synchronise(source , replica, logPath)

# print(scanFolder('/home/l/Documents/repos/folder-sync/folder-sync/Source'))
# print(x.keys())
# folder = os.walk('/home/l/Documents/repos/folder-sync/folder-sync/Source')

# for x, y, z in folder:
#     print('*************')
#     print(x)
#     print(y)
#     print(z)
#     print('**************8')

# shutil.copytree('/home/l/Documents/repos/folder-sync/folder-sync/Source', '/home/l/Documents/repos/folder-sync/folder-sync/Replica')
# temp = 
# temp = source + '/Bookss/vice/test'
# os.makedirs(source + '/Bookss/vice/test')
# shutil.copy2(source + '/Bookss/2.txt', replica + '/Bookss/2.txt')




