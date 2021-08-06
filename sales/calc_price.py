from sales.formatter.price import real


def increase(value, percent, formatx=False):
    total = value + (value * (percent / 100))
    return real(total) if formatx else total


def decrease(value, percent, formatx=False):
    total = value - (value * (percent / 100))
    return real(total) if formatx else total

