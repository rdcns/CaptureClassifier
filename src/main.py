from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time
import json

if __name__ == "__main__":

    class MyHandler(FileSystemEventHandler):
        def on_created(self, event):
            if not event.is_directory:
                print(f"Created: {event.src_path}")

    with open("config.json", "r") as f: 
        data = json.load(f)

    path = data["path_to_watch"]
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()