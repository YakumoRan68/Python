class stack:
	def __init__(self) :
		self.memory = list()
		self.top = -1

	def __call__(self) : #top 출력
		return self.memory[self.top]

	def push(self, x) :
		self.memory.append(x)
		self.top += 1

	def pop(self) :
		if self.top > -1 :
			self.top -= 1
			return self.memory.pop()
		else:
			print("stack underflow")

	def viewtop(self) :
		return self.memory

x = stack()
x.push(3)
x.push(4)

print(x(), x.pop(), x.pop())
