"""
2.1.1.10 Python core syntax: LAB #1
https://edube.org/learn/python-advanced-1/lab-1-implementing-core-syntax
"""


class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    @staticmethod
    def format_time(operation: int) -> str:
        h = operation // 3600
        operation -= 3600 * h
        time_elements = ['0' + str(h) if h < 10 else str(h)]
        m = operation // 60
        operation -= 60 * m
        time_elements.append('0' + str(m)) if m < 10 else time_elements.append(str(m))
        s = operation
        time_elements.append('0' + str(s)) if s < 10 else time_elements.append(str(s))
        result = ':'.join(time_elements)
        return result

    def __add__(self, other):
        try:
            assert type(other) is TimeInterval
        except AssertionError:
            print("Wrong type of input data. Method must be invoked with TimeInterval object as an left operand"
                  " and TimeInterval object as an right operand")
            raise TypeError
        all_in_seconds_left = 3600 * self.hours + 60 * self.minutes + self.seconds
        all_in_seconds_right = 3600 * other.hours + 60 * other.minutes + other.seconds
        return self.format_time(all_in_seconds_left + all_in_seconds_right)

    def __sub__(self, other):
        try:
            assert type(other) is TimeInterval
        except AssertionError:
            print("Wrong type of input data. Method must be invoked with TimeInterval object as an left operand"
                  " and TimeInterval object as an right operand")
            raise TypeError
        all_in_seconds_left = 3600 * self.hours + 60 * self.minutes + self.seconds
        all_in_seconds_right = 3600 * other.hours + 60 * other.minutes + other.seconds
        operation = all_in_seconds_left - all_in_seconds_right
        return self.format_time(operation) if operation > 0 else '-'+self.format_time(abs(operation))

    def __mul__(self, other: int):
        try:
            assert type(other) is int
        except AssertionError:
            print("Wrong type of input data. Method must be invoked with TimeInterval object as an left operand"
                  " and Integer object as an right operand")
            raise TypeError
        all_in_seconds = 3600 * self.hours + 60 * self.minutes + self.seconds
        secs_multi = all_in_seconds * other
        return self.format_time(secs_multi) if secs_multi > 0 else '-'+self.format_time(abs(secs_multi))

    def __str__(self):
        h = '0' + str(self.hours) if self.hours < 10 else str(self.hours)
        m = '0' + str(self.minutes) if self.minutes < 10 else str(self.minutes)
        s = '0' + str(self.seconds) if self.seconds < 10 else str(self.seconds)
        return h+':'+m+':'+s


if __name__ == "__main__":
    ti_1 = TimeInterval(21, 58, 50)
    ti_2 = TimeInterval(1, 45, 22)
    ti_3 = TimeInterval()
    ti_4 = TimeInterval(4, 3, 2)
    assert ti_1 + ti_2 == "23:44:12"
    assert ti_1 - ti_2 == "20:13:28"
    assert ti_1 * 2 == "43:57:40"
    assert ti_3 - ti_4 == "-04:03:02"
