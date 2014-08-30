from time import strftime

from parsedatetime import Calendar


class ParseDate(object):

    @staticmethod
    def parse(raw_str):
        parsed = Calendar().parse(raw_str)

        if parsed[1] is 0 or parsed[1] is 2:
            return raw_str

        return strftime('%Y-%m-%d', parsed[0])

    def __call__(self, values):
        return [self.parse(value) for value in values]