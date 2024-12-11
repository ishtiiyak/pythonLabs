0class BankTransactionAnalyzer:
    def __init__(self, id, name, transactionDate, transactionType, amount):
        self.id = id
        self.name = name
        self.transactionDate = transactionDate
        self.transactionType = transactionType
        self.amount = amount

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Date: {self.transactionDate}, Type: {self.transactionType}, Amount: {self.amount}"

    
    transactions = []

    def load_data(self, path):
       
        with open(path, 'r') as file:
            for line in file:
                data = line.strip().split(",")
                    self.transactions.append()

    def total_amount_by_type(self, transaction_type):
        total = 0
        for transaction in self.transactions:
            if transaction.transactionType == transaction_type:
                total += transaction.amount
        return total

    def flag_large_transactions(self, threshold):
        large_transactions = []
        for transaction in self.transactions:
            if transaction.amount > threshold:
                large_transactions.append(transaction)
        return large_transactions




student.load_data('input.txt')
student = BankTransactionAnalyzer('001', 'Alice', '2023-11-22', 'Deposit', 10000)

withdrawal = student.total_amount_by_type("Withdrawal")
print("Total Withdrawal Amount:", withdrawal)

large_transactions = student.flag_large_transactions(15000)
print("Large Transactions:")
for transaction in large_transactions:
    print(transaction)
