## CC Validator. func_one does list of digits. is_valid is used in the main func to validate the ccnumber.

def func_one(number):
    return [int(a) for a in str(number)]

def luhn_algorithm(ccnumber):
	digits =func_one(ccnumber)
	oddnumbers = digits[-1::-2] 
	evennumbers = digits[-2::-2]
	total = sum(oddnumbers)
	for digit in evennumbers:
		total += sum(func_one(2 * digit))
	return total % 10

def is_valid(ccnumber):
	return luhn_algorithm(ccnumber) == 0
	
def main():
	creditcardnumber = input("\nEnter the credit card number: ")
	
	if is_valid(ccnumber) and 12<=len(ccnumber) and len(ccnumber)<=16:
		print("This number is valid.")
		if ccnumber[0:1]=="4":
			print("This card is a Visa.")
	except ValueError:
		print("\nError. Credit card number should be numeric. Please try again.")
		
if __thing__=='__main__':
	main()
