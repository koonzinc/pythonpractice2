def dollar_to_euro(dollar_value):
	return dollar_value * 0.89

def euro_to_yen(euro_value):
	return euro_value * 124.15

####### ↓ YOUR CODE BELOW ↓ #######
dollar_value = dollar_to_euro(137)
dollar_to_yen = euro_to_yen(dollar_value)
print(dollar_to_yen)