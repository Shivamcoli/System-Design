from account import Account
from card import Card
class Atm:
    
    def __init__(self):
        self.accounts=[]
        self.cards={}
    
    def create_account(self, account_number, initial_balance):
        account= Account(account_number, initial_balance)
        self.accounts.append(account)
        print(f"Account {account_number} created with balance {initial_balance}")
        
    def link_card(self, card_number, pin, account_number):
        card = Card(card_number, pin)
        for account in self.accounts:
            if account.account_number == account_number:
                self.cards[card_number] = (card, account_number)
                print(f"Card {card_number} linked to account {account_number}")
                return
            
            raise ValueError("Account does not exist")
        self.cards[card_number] = (card, account_number)
        print(f"Card {card_number} linked to account {account_number}")
        
        
    def check_balance(self, card_number, pin):
        if card_number not in self.cards:
            raise ValueError("Card not linked")
        card, account_number = self.cards[card_number]
        if card.pin != pin:
            raise ValueError("Invalid PIN")
        for account in self.accounts:
            if account.account_number == account_number:
                return account.check_balance()
        raise ValueError("Account not found")
    
    def withdraw(self, card_number, pin, amount):
        if card_number not in self.cards:
            raise ValueError("Card not linked")
        card, account_number = self.cards[card_number]
        if card.pin != pin:
            raise ValueError("Invalid PIN")
        for account in self.accounts:
            if account.account_number == account_number:
                return account.withdraw(amount)
        raise ValueError("Account not found")
        
        
if __name__ == "__main__":   
    atm = Atm()
    atm.create_account("123456", 1000)
    atm.link_card("1111-2222-3333-4444", "1234", "123456")
    balance = atm.check_balance("1111-2222-3333-4444", "1234")
    print(f"Balance: {balance}")
    new_balance = atm.withdraw("1111-2222-3333-4444", "1234", 200)
    print(f"New Balance after withdrawal 200: {new_balance}")

    
    