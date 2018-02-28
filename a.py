from urllib.request import urlopen

response = urlopen("http://cs1110.cs.cornell.edu/2015fa/a1server.php?from=USD&to=INR&amt=2.5")
a = response.read()
print(a)


def currency_response(currency_from, currency_to, amount_from):
	response = urlopen("http://cs1110.cs.cornell.edu/2015fa/a1server.php?from="+currency_from+"&to="+currency_to+"&amt="+str(amount_from))
	a = response.read().decode()
	return a



def has_error(json):
	
	if json.find("\"error\" : \"\" ") == -1 :

		return True
	else:
		return False

def before_space(s):

	pos1 = json.find("\"",7)
	print(pos1)
	pos2 = json.find("\"",pos1+1)
	print(pos2)
	substring1 = json[pos1+1:pos2]
	print(substring1)
	spacepos1 = substring1.find(' ')
	fromcurrencycode = substring1[spacepos1+1:]
	fromamount = substring1[:spacepos1]
	print(fromcurrencycode)
	print(fromamount)
	return substring1



def after_space(s):
	pos3 = json.find("\"",47)
	print(pos3)
	pos4 = json.find("\"",pos3+1)
	print(pos4)
	substring2 = json[pos3+1:pos4]
	print(substring2)
	spacepos2 = substring2.find(' ')
	tocurrencycode = substring2[spacepos2+1:]
	toamount = substring2[:spacepos2]
	print(tocurrencycode)
	print(toamount)
	return substring2



json = currency_response("USD", "INR", "2.5")
print(json)

print(has_error(json))
before_space(json)
after_space(json)

