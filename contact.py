class Contact():
    def __init__(self):
        self.contact_list = []

    def add_contact(self, first_name, last_name, phone, email):
        new_contact = {
            'Имя': first_name,
            'Фамилия': last_name,
            'Телефон': phone,
            'Email': email
        }
        self.contact_list.append(new_contact)

    def remove_contact(self, first_name, last_name):
        for contact in self.contact_list:
            if contact['Имя'] == first_name and contact['Фамилия'] == last_name:
                self.contact_list.remove(contact)

    def view_contacts(self, first_name, last_name):
        for contact in self.contact_list:
            if contact['Имя'] == first_name and contact['Фамилия'] == last_name:
                print(contact)

c = Contact()
c.add_contact('John', 'Doe', '555-555-5555', 'tqK1v@example.com')
c.add_contact('Jane', 'Jo', '555-555-5555', 'tqK2v@example.com')
c.add_contact('Joe', 'Due', '555-555-5555', 'tqK23@example.com')



c.view_contacts('John', 'Doe')

