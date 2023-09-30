import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'c:\Users\usuario\Downloads'

class FileEventHandler(FileSystemEventHandler):
    
    def on_created(self,event):
        print(f"Olá, {event.src_path} foi criado!")
        
    def on_modified(self,event):
        print(f"Olá, {event.src_path} foi modificado!")
    
    def on_moved(self,event):
        print(f"Olá, {event.src_path} foi movido!")
        
    def on_deleted(self,event):
        print(f"Opa, alguém excluiu {event.src_path}!")

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print('executando...')
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()