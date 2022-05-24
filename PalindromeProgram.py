def isPalidrome(text):
	revText = text[::-1]
	if text == revText:
		print("Entered text is Palindrome!!")
	else:
		print("Entered text is NOT Palindrome!!")


k=True
while k:
	text = input("Enter the text or 'exit' to quit the program : ")

	if text == 'exit':
		k = False
		break
	else:
		text = text.lower()
		newText = ""

		for i in text:
			if i.isalnum():
				newText += i
	
	isPalidrome(newText)