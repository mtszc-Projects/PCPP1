"""
3.2.1.1 LAB: CSV – Lab 1
https://edube.org/learn/pcpp1-5/lab-csv-lab-1
When we buy a new phone, it's necessary to import old contacts. Why not import them from a CSV file? Look again at the
familiar contacts.csv file, and then design your new phone as follows:
create a class called PhoneContact representing a single contact. The PhoneContact class should contain the name and
phone properties;
create a class called Phone that will store your contacts. First, implement the method called load_contacts_from_csv,
responsible for reading data from the CSV file into the class property called contacts. The contacts property should
contain a list of PhoneContact objects;
add to the Phone class a method called search_contacts, which accepts any phrase entered by the user from the keyboard,
and then based on it perform a search for all matching contacts (case insensitive). If there are no results, print the
message: "No contacts found".
Example input:
Search contacts: mother
Example output:
mother (222-555-101)
mother-in-law (222-555-104)
Example input:
Search contacts: 103
Example output:
wife (222-555-103)
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
