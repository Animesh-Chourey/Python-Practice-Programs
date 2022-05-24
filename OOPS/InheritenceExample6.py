#Multiple Level Inheritence

class A:
	def m1(self):
		print("Parent Class A")

class B:
	def m1(self):
		print("Parent Class B")

class C(B,A):
	pass

c=C()
c.m1()