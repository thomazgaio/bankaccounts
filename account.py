class Account:
	def __init__(self, accountId, balance):
		self._id = accountId
		self._balance = balance
	
	def deposit(self, value):
		self._balance += value
		return self._balance
	
	def withdraw(self, value):
		self._balance -= value
		if self._balance < 0:
			self._balance -= 500
		return self._balance

	@property
	def balance(self):
		return self._balance

	@property
	def id(self):
		return self._id