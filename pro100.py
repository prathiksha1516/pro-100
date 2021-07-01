class ATM(object):
    def __init__(self, CashWithdrawl,cardnumber,pinnumber,BalanceEnquiry,colour):
        self.colour="colour"
        self.BalanceEnquiry="BalanceEnquiry"
        self.pinnumber="pinnumber"
        self.cardnumber="cardnumber"
        self. CashWithdrawl= "CashWithdrawl"
    def  CashWithdrawl(self):
        print(self.colour)    
    def shapes(self):
        print(self.pinnumber)

money=ATM("2435","3456","5647","10,000","grey")

money.CashWithdrawl()
money.BalanceEnquiry()
        
 