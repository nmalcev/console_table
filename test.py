import re
from console import C 
from table import Table



def string_to_list(str):
	return list(filter(None, re.split('(..\[[^m]+m$|.\[[^m]+m.|.)', str)))

def drawDict(dic):
	table = Table()
	colNumber = 0

	for key in dic:
		print(table.add_row([key, str(dic[key])], colNumber == 0))
		colNumber += 1


#========================================
# Some waste code
#========================================
print('[Example: colored output]')
buf = C.echo('Hello', C.LIME)
print(buf)
print('SIZE %s %s %s' % (len(buf), len(C.LIME), len('Hello')))
print(string_to_list(buf))
# print(C.print_format_table())
# TODO split on chars
# '\x1b[6;30;42m___c\033[95m'.split(/(.?\033[^m]+m)/g)

# list(map(chr,[66,53,0,94]))

#========================================
# Example of printing table rows
#========================================
print('\n[Example: simple table]')
table = Table()
print(table.add_topline())

print(table.add_row(
	['1111abcdfghjklmnasdfghjkqwertuioaasssasdqdewwedwecwe', '222dxsdssdxxadsxsasxasxsasxsxsxasxs2', '3333333']
))
print(table.add_row(
	list(map(string_to_list, ['1111abcdfghjklmnasdfghjkqwertuioaasssasdqdewwedwecwe', '222dxsdssdxxadsxsasxasxsasxsxsxasxs2', '3333333']))
))
print(table.add_row(
	list(map(string_to_list, [C.echo('Hello', C.OKGREEN), C.echo('World!', C.WARNING)]))
))
#========================================
# Print dictionary object in table
#========================================
print('\n[Example: print dictionary at table]')
data1 = {
	'fetch': 'http://rb-validation.virool.com/event?type=page_load&browser=Chrome--51.0&domain=folha.uol.com.br&site_id=108008&embed_key=07ynlh2kpfl9', 
	'httpStatus': 0, 
	'httpReason': '[Errno 116] Connection timed out'
}

data2 = {
	'httpStatus': 200, 
	'contentType': 'text/html', 
	'setLocation': None, 
	'httpReason': 'OK', 
	'fetch': 'https://eu-u.openx.net/w/1.0/sd?cc=1&id=536872786&val=8bf4583c-2a9b-4800-b230-53b142ce493c', 
	'setCookie': []
}

def drawDict(dic):
	table = Table()
	colNumber = 0

	for key in dic:
		print(table.add_row([key, str(dic[key])], colNumber == 0))
		colNumber += 1

drawDict(data1)
print('\n')
drawDict(data2)







