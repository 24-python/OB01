class Contact:
    def __init__(self):
        self.contact_list = []

    def add_contact(self, first_name, last_name, phone, email):
        if not self._is_valid_email(email):
            print("Invalid email address.")
            return
        if not self._is_valid_phone(phone):
            print("Invalid phone number.")
            return

        new_contact = {
            'Имя': first_name,
            'Фамилия': last_name,
            'Телефон': phone,
            'Email': email
        }
        self.contact_list.append(new_contact)
        print(f"Contact {first_name} {last_name} added.")

    def remove_contact(self, first_name, last_name):
        initial_length = len(self.contact_list)
        self.contact_list = [
            contact for contact in self.contact_list
            if not (contact['Имя'] == first_name and contact['Фамилия'] == last_name)
        ]
        if len(self.contact_list) < initial_length:
            print(f"Contact {first_name} {last_name} removed.")
        else:
            print(f"Contact {first_name} {last_name} not found.")

    def view_contacts(self, first_name=None, last_name=None):
        filtered_contacts = self.contact_list

        if first_name:
            filtered_contacts = [
                contact for contact in filtered_contacts
                if contact['Имя'] == first_name
            ]
        if last_name:
            filtered_contacts = [
                contact for contact in filtered_contacts
                if contact['Фамилия'] == last_name
            ]

        if filtered_contacts:
            for contact in filtered_contacts:
                print(contact)
        else:
            print("No contacts found.")

    def view_all_contacts(self):
        if self.contact_list:
            for contact in self.contact_list:
                print(contact)
        else:
            print("No contacts available.")

    def _is_valid_email(self, email):
        import re
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def _is_valid_phone(self, phone):
        import re
        pattern = r'^\+?[0-9\s\-]{7,15}$'
        return re.match(pattern, phone) is not None

# Пример использования
c = Contact()
c.add_contact('John', 'Doe', '555-555-5555', 'tqK1v@example.com')
c.add_contact('Jane', 'Jo', '555-555-5555', 'tqK2v@example.com')
c.add_contact('Joe', 'Due', '555-555-5555', 'tqK23@example.com')

print("Viewing specific contacts:")
c.view_contacts('John', 'Doe')

print("\nRemoving a contact:")
c.remove_contact('John', 'Doe')
c.view_contacts('John', 'Doe')

print("\nViewing all contacts:")
c.view_all_contacts()