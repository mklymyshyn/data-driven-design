import ConfigParser


def read_sources(path):
    """
    Read ``sources`` section from the config file
    """
    config = ConfigParser.ConfigParser()
    config.read(path)

    urls = config.get("sources", "urls").split("\n")
    urls = map(lambda s: s.strip(), urls)

    return [url for url in urls if url != ""]
