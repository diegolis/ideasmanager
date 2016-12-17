# -*- coding: utf-8 -*-
import markdown
import argparse
import time
import os
from toc import TocExtension
from markdown_include.include import MarkdownInclude
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


INPUT = "main.md"
OUTPUT = "output.html"


class GenerateBook(FileSystemEventHandler):

    def __init__(self, path):
        self.path = path

    def on_modified(self, event):
        markdown.markdownFromFile(
            input=os.path.join(args.path, INPUT),
            output=os.path.join(args.path, OUTPUT),
            encoding="iso-8859-1",
            extensions=[
                'markdown.extensions.tables',
                'markdown.extensions.sane_lists',
                'markdown.extensions.wikilinks',
                MarkdownInclude(configs={'base_path': args.path}),
                TocExtension(anchorlink=True),
                ])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert markdown to html Mario Chalita's book.")
    parser.add_argument(
        '--path', type=str, help='Path containing main.hd file')
    args = parser.parse_args()

    handler = GenerateBook(args.path)
    handler.on_modified(None)

    observer = Observer()
    observer.schedule(handler, args.path)
    observer.start()
    print ("Ya puede realizar modificaciones sobre los archivos.\n"
           "El libro se generará automáticamente en {}\n"
           "Al terminar presione Ctrl-C".format(
                    OUTPUT
                ))
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
