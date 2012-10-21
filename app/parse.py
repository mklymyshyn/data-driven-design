# -*- coding: utf-8 -*-

import datetime
import re

from bs4 import BeautifulSoup

from .entity import Entry
from .core import process, log

__all__ = ("parse",)


def parse_structured_data(data):
    log("Processing data {}".format(id(data)),
        level="parse_structured_data")

    if (isinstance(data, dict) and "response" in data and
        len(data["response"]) > 0 and
            "periods" in data["response"][0]):

        for item in data["response"][0]["periods"]:
            date = datetime.datetime.fromtimestamp(item["timestamp"])
            weather = item["weather"]
            temperature = item["avgTempC"]

            yield Entry(
                temperature=temperature,
                date=date,
                weather=weather
            )


def parse_yandex(data):
    log("Processing data {}".format(id(data)), level="parse_yandex")

    weather_map = {
        "bkn_d.png": "Sunny with clouds",
        "skc_d.png": "Sunny"
    }

    try:
        doc = BeautifulSoup(data)
    except TypeError:
        return

    # should be extended
    months_map = {
        "жовт.": 10
    }
    # hardocing, for examaple
    year = 2012

    dates = []
    months = []
    temperatures = []

    for elem in doc.find_all("div"):
        try:
            if u"b-forecast-detailed__date" in elem["class"]:
                dates.append(int(elem.text))
            if u"b-forecast-detailed__month" in elem["class"]:
                months.append(
                    months_map[elem.text.strip().encode("utf-8")])
            if u"b-forecast-detailed__temp" in elem["class"]:
                temperatures.append(elem.text)
        except KeyError:
            continue

    image_srcs = []
    for elem in doc.find_all("img"):
        try:
            if "30x30" in elem["src"]:
                image_srcs.append(elem["src"])
        except KeyError:
            continue

    temperatures = map(
        lambda s: re.search(r"([\+\-]\d+)", s).groups(0)[0],
        temperatures
    )

    weather = []
    for img in image_srcs:
        weather_title = "Unknown"
        for key, val in weather_map.iteritems():
            if key in img:
                weather_title = val
                break

        weather.append(weather_title)

    weather = weather[2:]
    for wr in range(0, len(weather), 4):
        if len(months) == 0 or len(dates) == 0:
            break

        yield Entry(
            weather=weather[wr + 1],
            temperature=int(temperatures[wr + 1]),
            date=datetime.datetime(
                year=year,
                month=months.pop(0),
                day=dates.pop(0)
            ))


def parse_weather_com(data):
    log("Processing data {}".format(id(data)), level="parse_weather_com")
    return None


PARSERS_PROCESSORS = [
    parse_structured_data,
    parse_yandex,
    parse_weather_com
]


def parse(data):
    log("Parsers started")
    return process(PARSERS_PROCESSORS, [data])
