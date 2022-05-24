#Multi Level Inheritence

class A:
	def show(self):
		print("Parent class A")

class B(A):
	def show(self):
		super().show()
		print("Child class B")

class C(B):
	def show(self):
		super().show()
		print("Child class C")


c=C()
c.show()