import markdown
from markdown.extensions.toc import TocExtension
from markdown_include.include import MarkdownInclude


INPUT = "main.md"
OUTPUT = "output.html"

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
