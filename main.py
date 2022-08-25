import os
from functions import scanFolder, synchronize, timeModified
import datetime
import pathlib
import shutil
import re
import time
import sys

#Main function takes four system arguments: Source folder, Replica folder, log file folder and time of synchronisation 

while(True):
    synchronize(sys.argv[1], sys.argv[2], sys.argv[3])
    time.sleep(int(sys.argv[4]))
