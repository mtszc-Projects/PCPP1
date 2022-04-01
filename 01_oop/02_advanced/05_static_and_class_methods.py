"""
2.5.1.9 Lab
https://edube.org/learn/python-advanced-1/lab
"""


class Watch:
    __watches_created = 0

    def __init__(self):
        Watch.__watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.__watches_created

    @classmethod
    def engraving(cls, engraving):
        cls.validate(engraving)
        __watch = cls()
        __watch.engraving = engraving
        return __watch

    @staticmethod
    def validate(engraving):
        try:
            assert len(engraving) <= 40
            for i in engraving:
                assert i.isalnum()
        except AssertionError:
            print("ERROR: Engraving doesn't comply with restrictions.")
            exit()


if __name__ == "__main__":
    print(Watch.get_number_of_watches_created())
    watch_1 = Watch()
    print(Watch.get_number_of_watches_created())
    watch_2 = Watch.engraving('Love')
    print(watch_2.engraving)
    print(Watch.get_number_of_watches_created())
    watch_3 = Watch.engraving('foo @ baz.com')
    print(watch_3.engraving)
    print(Watch.get_number_of_watches_created())
