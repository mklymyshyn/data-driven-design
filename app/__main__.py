
from .core import pipeline
from .config import read_sources
from .grab import grab
from .parse import parse
from .validate import validate

PIPELINE = [
    grab,
    parse,
    validate
]

# read urls to grab
urls = read_sources("sources.cfg")

for item in list(pipeline(PIPELINE, urls))[-1]:
    print item
