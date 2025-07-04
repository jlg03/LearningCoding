import random

def spin_row():
    symbols = ['1', '2', '3', '4', '5']
    results = []
    
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '1':
            return bet * 3
        elif row[0] == '2':
            return bet * 4
        elif row[0] == '3':
            return bet * 5
        elif row[0] == '4':
            return bet * 10
        elif row[0] == '5':
            return bet * 20
    return 0

def main():
    balance = 100
    
    print("Welcome to Python SLots")
    
    while balance > 0:
        print(f"Current balance: ${balance}")
        
        bet = input("Place your bet amount: ")
        
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient funds")
            continue
        if bet <= 0:
            print("That must be greater than 0")
            continue
        balance -= bet
        row = spin_row()
        print("Spinning...\n")
        
        print_row(row)
        
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost")
            
        balance += payout
        
        play_again = input("Do you want to spin again? (Y/N): ")
        if play_again != 'Y':
            break
        
        print(f"Final balace: ${balance:.2f}")
if __name__ == '__main__':
    main()