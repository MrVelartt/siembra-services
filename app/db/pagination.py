def parse_range(range_param: str | None):
    if range_param is None:
        return 0, 50
    range_param = range_param.replace("items=", "")
    start, end = range_param.split("-")
    start = int(start)
    end = int(end)
    limit = (end - start) + 1
    return start, limit
