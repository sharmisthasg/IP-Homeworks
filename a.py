"""
This program extracts data from the given URL and checks the conversion rates between different currencies
"""

#importing the function urlopen fron the library urllib
from urllib.request import urlopen

response = urlopen("http://cs1110.cs.cornell.edu/2015fa/a1server.php?from=USD&to=INR&amt=2.5")
a = response.read()
print(a)

"""
The currency_response function takes as input the currencies
to be converted between and calls an API that supplies the 
converted amount
"""
def currency_response(currency_from, currency_to, amount_from):
	response = urlopen("http://cs1110.cs.cornell.edu/2015fa/a1server.php?from="+currency_from+"&to="+currency_to+"&amt="+str(amount_from))
	a = response.read().decode()
	return a

"""
The has_error function checks for any errors in the 
JSON response from the API
"""
def has_error(json):
	if json.find("\"error\" : \"\" ") == -1 :

		return True
	else:
		return False
	
"""
The before_space function takes as input the
JSON string and parses for the currency and amount being
converted from
"""
def before_space(s):
	pos1 = json.find("\"",7)
	pos2 = json.find("\"",pos1+1)
	substring1 = json[pos1+1:pos2]
	spacepos1 = substring1.find(' ')
	fromcurrencycode = substring1[spacepos1+1:]
	fromamount = substring1[:spacepos1]
	return substring1
  
"""
The after_space function takes as input the
JSON string and parses for the cuurency and amount being
converted to
"""  

def after_space(s):
	pos3 = json.find("\"",47)
	pos4 = json.find("\"",pos3+1)
	substring2 = json[pos3+1:pos4]
	spacepos2 = substring2.find(' ')
	tocurrencycode = substring2[spacepos2+1:]
	toamount = substring2[:spacepos2]
	return substring2

json = currency_response("USD", "INR", "2.5")
print(json)

print(has_error(json))
before_space(json)
after_space(json)

