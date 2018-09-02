class formatedResponse:
    def __init__(self, url, status, ttfb):
        self.url = url
        self.status = status
        self.ttfb = ttfb

    def asString(self):
        return (str(self.status) + " - " + str(self.ttfb) + "s - " + str(self.url))


class limitsForTTFB:
    def __init__(self, _min, _mid, _max):
        self.min = _min
        self.mid = _mid
        self.max = _max

