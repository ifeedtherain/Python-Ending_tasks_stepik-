
class NonPositiveError(Exception):
	pass

class PositiveList(list):
	def append(self, x):
		if x <= 0:
			raise NonPositiveError("Nope")
		else:
			super(PositiveList, self).append(x)
			self.append(x)

x = PositiveList([1,2])

try:
	x.append(3)

except NonPositiveError:
	print('Fuck')
print(x)
