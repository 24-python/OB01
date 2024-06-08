class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
        print(f"Вы успешно пополнили счет на {money} рублей. Сумма на счету составляет {self.balance} рублей.")

    def withdraw(self, money):
        if money > 0 and self.balance >= money:
            self.balance -= money
            print(f"Вы сняли {money} рублей. Сумма на счету составляет {self.balance} рублей.")

        elif money > 0 and self.balance < money:
            print("Недостаточно средств.")

    def info(self):
        print(f"Ваш баланс составляет {self.balance} рублей.")

man = Account(1,1000)

man.info()
man.deposit(1000)
man.withdraw(500)
man.withdraw(5000)
man.deposit(10000)

man.info()


