# folder-sync

Program that synchronizes two folders: source and replica. The program should maintain a full, identical copy of destination folder at replica folder.
Requirements:

    • Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;

    • Synchronization should be performed periodically;

    • File creation/copying/removal operations should be logged to a file and to the console output;

    • Folder paths, synchronization interval and log file path should be provided using the command line arguments.

Latest version of script copies, modifies and deletes all files from Source folder, including those in subfolders. However, I still need to create the subfolders in the replica folder, which are not currently created. Maybe use recursion on any folder I find?? Or just call it a feature and move on.

Other TODO's can be found in the main file

TODO Make regex applicable regardless of the name of the folder

TODO: If we have a file in Replica that is not in source, we remove that file from replica

TODO: maybe sort after last modified date. Save last modified date from latest sync iteration in a temp variable and only check until final .                

TODO: Synchronise moving files internally

    Maybe make a regex function to deal with that

TODO: Synchronise creating empty folders. At the moment empty folders are not recreated in Replica but they will be created once empty folder is populated with a file