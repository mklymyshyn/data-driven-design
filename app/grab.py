import requests
from .core import process, log


__all__ = ("grab",)


def grab_json(url):
    log("Downloading {}".format(url), level="grab_json")
    response = requests.get(url)

    if not "application/json" in response.headers["content-type"]:
        return None

    return requests.get(url).json


def grab_rss(url):
    log("Downloading {}".format(url), level="grab_rss")
    response = requests.get(url)

    if not "text/xml" in response.headers["content-type"]:
        return None

    # TODO: parse XML
    return None


def grab_html(url):
    log("Downloading {}".format(url), level="grab_html")
    response = requests.get(url)

    if ("text/xml" in response.headers["content-type"] or
            "application/json" in response.headers["content-type"]):
        return None

    return response.content


# pipeline of grabbers
GRAB_PROCESSORS = [
    grab_rss,
    grab_json,
    grab_html
]


def grab(data):
    log("Grabber started")
    return process(GRAB_PROCESSORS, [data])
