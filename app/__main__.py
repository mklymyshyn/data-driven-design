import itertools
from .core import pipeline
from .config import read_sources
from .grab import grab
from .parse import parse


PIPELINE = [
    grab,
    parse
]

# read urls to grab
urls = read_sources("sources.cfg")

for item in list(pipeline(PIPELINE, urls))[-1]:
    for elem in item:
        print elem
