from account import Account
from bank import Bank

def main():
    a1 = Account()
    a2 = Account()
    a3 = Account()
    a1.init(1, 1000, "alex")
    a2.init(2, 2500, "kate")
    a3.init(3, 500, "vova")

    tpl = (a1, a2, a3)

    print(Bank.show_all_account(tpl))
    print(f"Total balance is {Bank.sum_all_balance(tpl)}")
    print(f"After month:{Bank.calc_sum_after_month(tpl)}")

if __name__ == "__main__":
    main()