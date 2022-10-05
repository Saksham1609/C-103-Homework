import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Sample"



#Event Handler Class
class FileMovementHandler(FileSystemEventHandler):
    #Code to create New file Cration in a directory
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")


eventHandler = FileMovementHandler()

#Initialise Observer
observer = Observer()

#Schedule the Observer
observer.schedule(eventHandler, from_dir, recursive = True)

#Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()              