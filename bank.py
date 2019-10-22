import sys
import csv
from account import Account

if __name__ == "__main__":	
	
	if len(sys.argv) < 3:
		print("ERROR: missing arguments");

	with open(sys.argv[1]) as csv_savings:
	    savings_reader = csv.reader(csv_savings, delimiter=',')
	    accounts = dict((int(x[0]), Account(int(x[0]),int(x[1]))) for x in savings_reader)

	with open(sys.argv[2]) as csv_transactions:
		transactions_reader = csv.reader(csv_transactions, delimiter=',')
		for transaction in transactions_reader:
			value = int(transaction[1])
			account = accounts.get(int(transaction[0]));
			if account is not None:
				if value < 0:
					account.withdraw(value*-1);
				else:
					account.deposit(value);
			else:
				print("ERROR: inexistent account ["+transaction[0]+"]");

	for keys,account in accounts.items():
		print(account.id,account.balance)