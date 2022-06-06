class ContactList():
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, number):
        self.name = name
        self.number = number

        self.contacts.append({"name": name, "number": number})

    def remove_contact(self, name):
        self.name = name

        for i in self.contacts:
            if i["name"] == name:
                self.contacts.remove(i)

    def find_shared_contacts(self, contact_list):
        self.contact_list = contact_list
        common = []

        for i in contact_list.contacts:
            if i in self.contacts:
                common.append(i)

        return common





friends = ContactList()
friends.add_contact("Evan", "5027152210")
friends.add_contact("Anabelle", "5027623075")

coworkers = ContactList()
coworkers.add_contact("Evan", "5027152210")
coworkers.add_contact("Birdie", "8055550123")

print(coworkers.find_shared_contacts(friends))
