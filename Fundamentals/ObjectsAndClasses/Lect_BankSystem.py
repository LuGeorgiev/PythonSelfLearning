class BankAccount:
    def __init__(self, name, bank, balance):
        self.name = name
        self.bank = bank
        self.balance = balance


data_list = input().split(' | ')
accounts_list = []
while data_list[0] != "end":
    bank = data_list[0]
    name = data_list[1]
    balance = float(data_list[2])

    bank_account = BankAccount(name, bank, balance)
    accounts_list.append(bank_account)
    data_list = input().split(' | ')
# - means descending it it is INT
# sort balance descending and bank.name length ascending
for acc in sorted(accounts_list, key=lambda x: (-x.balance, len(x.bank))):
    print(f'{acc.name} -> {acc.balance:.2f} ({acc.bank})')
