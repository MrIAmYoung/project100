class atm:
    def __init__(self, card_no,pin_no):
        self.card_no=card_no
        self.pin_no=pin_no
    def CashWithdrawl(self):
        print("Cash Withdrawl")
    def BalanceEnquiry(self):
        print("Balance Enquiry: ")
atm1=atm("001001","1234")
atm2=atm("100100","4321")
atm1.CashWithdrawl()
atm2.BalanceEnquiry()