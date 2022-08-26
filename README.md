# folder-sync

Program that synchronizes two folders: source and replica. The program should maintain a full, identical copy of destination folder at replica folder.
Requirements:

    • Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;

    • Synchronization should be performed periodically;

    • File creation/copying/removal operations should be logged to a file and to the console output;

    • Folder paths, synchronization interval and log file path should be provided using the command line arguments.

Program is called from command line/terminal and takes the following arguments:
1. Source folder path
2. Replica folder path
3. Log folder path
4. Synchronization interval (in seconds)

Paths should be in quotes
e.g. python3 main.py "Source path" "Replica path" "Log path" "time"
