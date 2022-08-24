import os
from functions import scanFolder, synchronise, timeModified
import datetime
import pathlib
import shutil
import re
import time
import sys

while(True):
    synchronise(sys.argv[1], sys.argv[2], sys.argv[3])
    time.sleep(int(sys.argv[4]))
