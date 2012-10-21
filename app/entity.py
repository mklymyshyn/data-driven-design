

__all__ = ("Entry",)


class Entry(object):
    """
    Sample entry which describe our weather entry.
    ``is_valid`` by default is ``False``
    """

    endpoint = None
    temperature = 0
    date = None
    weather = None

    is_valid = True

    pipeline = []

    def __init__(self, **kwargs):
        for key, val in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, val)
                self.log("{}={}", key, val)

    def __repr__(self):
        return "{} - {}C - {} - {}".format(
            self.date.strftime("%d/%m/%Y %H:%d"),
            self.temperature,
            self.weather,
            "valid" if self.is_valid else "invalid"
        )

    def log(self, msg, *args, **kwargs):
        """
        Record the flow
        """
        self.pipeline.append(
            msg.format(*args, **kwargs)
        )

    def path(self):
        return " -> ".join(self.pipeline)
