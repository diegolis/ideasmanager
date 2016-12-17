# -*- coding: utf-8 -*-
import markdown
import time
from toc import TocExtension
from markdown_include.include import MarkdownInclude
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

INPUT = "main.md"
OUTPUT = "output.html"


class GenerateFile(FileSystemEventHandler):

    def on_modified(self, event):
        markdown.markdownFromFile(
            input=INPUT,
            output=OUTPUT,
            encoding="iso-8859-1",
            extensions=[
                'markdown.extensions.tables',
                'markdown.extensions.sane_lists',
                'markdown.extensions.wikilinks',
                MarkdownInclude(),
                TocExtension(anchorlink=True),
                ])


if __name__ == "__main__":
    observer = Observer()
    observer.schedule(GenerateFile(), ".")
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
