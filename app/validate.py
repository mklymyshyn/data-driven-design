from .core import log

__all__ = ("validate",)


def validate(data):
    log("Validator started")

    for item in data:
        if "sun" not in item.weather.lower():
            item.is_valid = False
            item.log("Marked invalid")

        yield item
