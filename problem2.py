#Uhhh, DAT WAY
from random import randrange
low=1
high=1001
secret=int(raw_input("We are going to play high or lower again but this time the computer is guessing!\nInput a secret number from 1 to 1000\n>"))
numberguess=randrange(1,1000)
if(secret<1 or secret>1000):
secret=int(raw_input("Error 403: Enter a number between 1 and 1000!!!\n>"))
while(secret!=numberguess):
	highNlow=raw_input("The computer guessed {}, is that too high or too low?\n>".format(numberguess))
	if(highNlow=="high"):
		high=numberguess-1
		numberguess=randrange(numlow,numhigh)
	elif(highNlow=="low"):
		low=numberguess+1
		numberguess=randrange(numlow,numhigh)
print("Congrats the computer got it!\nComputer - The number is (Machine clinking) {}.".format(secret)
