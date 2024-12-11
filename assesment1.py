


class BankTransactionAnalyzer:
    def __init__(self,id,name,transactionDate,transationType,amount):

        self.id=id
        self.name=name
        self.transactionDate=transactionDate
        self.transactionType=transationType
        self.amount=amount
    transactions=[]
    def load_data(path):
        file=open(path,'w')

    def total_amount_by_type(id,transactionType):
        return [transactionType,amount]
    def flag_large_transactions(threshold):
        for amount in transactions:
            if(amount>threshold):
             return [amount]
    def __str__(self):
        return f'{}'



student=BankTransactionAnalyzer('t1')
student.load_data('input.txt')
student.total_amount_by_total(001,'Withdrawal')
