"""
3.2.1.1 LAB: CSV – Lab 1
https://edube.org/learn/pcpp1-5/lab-csv-lab-1
"""
import csv


class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Phone:
    __contacts = []

    @classmethod
    def load_contacts_from_csv(cls, file):
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls.__contacts.append(PhoneContact(row['Name'], row['Phone']))

    @classmethod
    def search_contacts(cls):
        search = input("Search contacts: ")
        finds = 0
        for phone_contact in cls.__contacts:
            if search.casefold() in phone_contact.name.casefold() or search.casefold() in phone_contact.phone:
                finds += 1
                print(f"{phone_contact.name}: {phone_contact.phone}")
        if finds == 0:
            print("No contacts found")


phone_1 = Phone()
phone_1.load_contacts_from_csv('contacts.csv')
phone_1.search_contacts()
