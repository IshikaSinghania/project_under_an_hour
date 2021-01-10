from barcode import EAN13
from barcode.writer import ImageWriter
def generator(n):
	my_code = EAN13(n , writer=ImageWriter)
	my_code.save("bar_code")
	return my_code
if __name__=='__main__':
	generator(input("Enter a 12 digit number to generate bar_code"))