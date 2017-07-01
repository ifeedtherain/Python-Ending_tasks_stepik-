class ExtendedStack(list):
	def sum(self):
		self.top1 = self.pop()
		self.top2 = self.pop()
		self.append(self.top1+self.top2)

	def sub(self):
		self.top1 = self.pop()
		self.top2 = self.pop()
		self.append(self.top1-self.top2)

	def mul(self):
			self.top1 = self.pop()
			self.top2 = self.pop()
			self.append(self.top1*self.top2)

	def div(self):
		self.top1 = self.pop()
		self.top2 = self.pop()
		self.append(self.top1//self.top2)

x = ExtendedStack([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(x)
x.sum()
print(x)
x.sub()
print(x)
x.mul()
print(x)
x.div()
print(x)
