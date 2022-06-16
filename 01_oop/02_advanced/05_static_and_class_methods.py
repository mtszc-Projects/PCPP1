"""
2.5.1.9 Lab
https://edube.org/learn/python-advanced-1/lab
Create a class representing a luxury watch;
The class should allow you to hold a number of watches created in the watches_created class variable. The number could
be fetched using a class method named get_number_of_watches_created;
the class may allow you to create a watch with a dedicated engraving (text). As this is an extra option, the watch with
the engraving should be created using an alternative constructor (a class method), as a regular __init__ method should
not allow ordering engravings;
the regular __init__ method should only increase the value of the appropriate class variable;
The text intended to be engraved should follow some restrictions:
it should not be longer than 40 characters;
it should consist of alphanumerical characters, so no space characters are allowed;
if the text does not comply with restrictions, an exception should be raised;
before engraving the desired text, the text should be validated against restrictions using a dedicated static method.
Create a watch with no engraving
Create a watch with correct text for engraving
Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
After each watch is created, call class method to see if the counter variable was increased
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
