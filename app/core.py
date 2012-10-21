
__all__ = ("pipeline", "process", "log")


def pipeline(pipeline_funcs, data):

    for pipe in pipeline_funcs:
        results = []

        for item in data:
            results.extend(pipe(item))

        data = filter(lambda r: r is not None, results)

        yield data


def process(processor_funcs, data):

    for item in data:
        for processor in processor_funcs:
            yield processor(item)


def log(msg, level=None):
    if level is None:
        fmt = "{}{}"
        level = ""
    else:
        fmt = " {} -> {}"

    print fmt.format(level, msg)
