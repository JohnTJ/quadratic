import argparse
import math

def quad(a,b,c):
	try:
		x1 = ((b*-1)+((b**2)-(4*a*c))**(.5))/(2*a)
		x2 = ((b*-1)-((b**2)-(4*a*c))**(.5))/(2*a)
		answer = "x = " + str(x1) + "\nx = " + str(x2)
	except:
		return "Imaginary Number :("

	return answer

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("a",help="a value")
	parser.add_argument("b",help ="b value")
	parser.add_argument("c",help="c value")

	args = parser.parse_args()

	a = float(args.a)
	b = float(args.b)
	c = float(args.c)

	answer = quad(a,b,c)

	print(answer)

if __name__=="__main__":
	main()