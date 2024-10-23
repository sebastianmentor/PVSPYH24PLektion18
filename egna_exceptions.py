############# Exception example 1 ################
class InvalidAgeError(Exception):
    """Ett undantag som kastas om åldern inte är giltig"""
    pass

def set_age(age:int):
    if age < 0:
        raise InvalidAgeError("Ålder kan inte vara negativ.")
    print(f"Ålder är satt till {age}")

try:
    set_age(-1)
except InvalidAgeError as e:
    print(e)


############# Exception example 2 ################
class FileFormatError(Exception):
    """Ett undantag som kastas om filformatet är ogiltigt"""
    pass

def process_file(file_name:str):
    if not file_name.endswith(".txt"):
        raise FileFormatError(f"Filformatet för {file_name} är ogiltigt. Endast .txt filer tillåts.")
    print("Fil bearbetas...")

try:
    process_file("data.csv")
except FileFormatError as e:
    print(e)


############# Exception example 3 ################
class InsufficientFundsError(Exception):
    """Ett undantag som kastas om det saknas tillräckligt med pengar på kontot"""
    pass

class BankAccount:
    def __init__(self, balance:int):
        self.balance = balance

    def withdraw(self, amount:int):
        if amount > self.balance:
            raise InsufficientFundsError("Otillräckligt med pengar på kontot.")
        self.balance -= amount
        print(f"{amount} kr har tagits ut. Ny balans är {self.balance} kr.")

try:
    account = BankAccount(100)
    account.withdraw(150)

except InsufficientFundsError as e:
    print(e)
