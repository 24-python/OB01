class Contact():
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    def info(self):
        print("First name: " + self.first_name)
        print("Last name: " + self.last_name)
        print("Phone: " + self.phone)
        print("Email: " + self.email)
