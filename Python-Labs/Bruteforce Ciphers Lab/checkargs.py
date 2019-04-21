import sys

if((len(sys.argv) !=4)):
    print('The number of arguments has to be 4, any more or less will print these instructions! :)')
else:
    print("Nicely done. I'm very impressed. You can follow instructions." + ' These are the arguments passed: ' + str(sys.argv))

