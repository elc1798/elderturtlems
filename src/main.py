import os

def textHandler():
	f = open('MESSAGE.txt' , 'a')
	complaint = str(raw_input('The Elder Turtle Shalt Now Hear Your Complaint:\n'))
	#Format the text: every 65 or more characters = new line
	characterCount = 0
	L = complaint.split()
	complaint = "\n"
	while len(L) > 0:
		if characterCount >= 65:
			complaint += L[0] + "\n"
			characterCount = 0
		else:
			complaint += L[0] + ' '
			characterCount += len(L[0])
		L.pop(0)
	#Debug: Check the format via displaying message in Terminal:
	#print(complaint)
	f.write(complaint)
	print("Message saved successfully in src/MESSAGE.txt")
	return 0

def main():
	print("Starting TheElderTurtle Complaint Service...")
	textHandler()
	return 0

main()
