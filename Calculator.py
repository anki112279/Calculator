import re

def calculator(exp):
	
	if check_float(exp):
		return float(exp)
	operators = ['+', '-', '*', '/']
	for c in operators:
		left, opt, right = exp.partition(c)
		if opt == '+':
			return calculator(left) + calculator(right)
		elif opt == '-':
			return calculator(left) - calculator(right)
		elif opt == '*':
			return calculator(left) * calculator(right)
		elif opt == '/':
			return calculator(left) / calculator(right)


def check_float(exp):
    try:
        float(exp.strip())
        return True
    except ValueError:
        return False


def resolving_brackets(s):
	
	org_s = s
	k = re.search(r"\(.+\)", s)
	if not k:
		return s
	start = k.span()[0]
	stop = k.span()[1]
	sub_exp = k[0][1:-1]
	
	new_exp = resolving_brackets(sub_exp)
	num = calculator(new_exp)
	new_exp = org_s[0:start]+str(num)+org_s[stop:]
	return new_exp
	

if __name__ == '__main__':
	
	expression =  '8+9/6'
	res = resolving_brackets(expression)
	print(calculator(res))

	