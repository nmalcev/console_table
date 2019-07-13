# python -c "from src.console import C; print(C.split(C.echo('abc', C.UNDERLINE, C.HEADER, end=C.BOLD)))"
# python -c "from src.console import C; print(C.echo('abc', C.bg.white, C.color.black))"
# https://docs.python.org/3/howto/curses.html
# https://gist.github.com/Sheljohn/68ca3be74139f66dbc6127784f638920

class C:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	
	BOLD = '\033[1m'
	ITALIC = '\33[3m'	
	UNDERLINE = '\033[4m'
	BLINK = '\33[5m'
	BLINK2   = '\33[6m'
	SELECTED = '\33[7m'

	LIME = '\x1b[6;30;42m'
	
	class bg:
		black  = '\33[40m'
		red = '\33[41m'
		green  = '\33[42m'
		yellow = '\33[43m'
		blue   = '\33[44m'
		violet = '\33[45m'
		beige  = '\33[46m'
		white  = '\33[47m'
		grey = '\33[100m'
		red2    = '\33[101m'
		green2  = '\33[102m'
		yellow2 = '\33[103m'
		blue2   = '\33[104m'
		violet2 = '\33[105m'
		beige2  = '\33[106m'
		white2  = '\33[107m'
	class color:
		black = '\33[30m'
		red = '\33[31m'
		green = '\33[32m'
		yellow = '\33[33m'
		blue = '\33[34m'
		violet = '\33[35m'
		beige = '\33[36m'
		white = '\33[37m'
		grey = '\33[90m'
		red2 = '\33[91m'
		green2 = '\33[92m'
		yellow2 = '\33[93m'
		blue2 = '\33[94m'
		violet2 = '\33[95m'
		beige2 = '\33[96m'
		white2 = '\33[97m'

	@classmethod
	def echo(cls, str, *styles, **kw):
		return ''.join(styles) + str + (kw['end'] if hasattr(kw, 'end') else '\033[0m')
	
	@classmethod	
	def test(cls):
		return chr(27) + "[2J"
	
	@classmethod
	def clear(cls):
		import sys
		sys.stderr.write("\x1b[2J\x1b[H")
	
	@classmethod
	def print_format_table():
		# prints table of formatted text format options
		for style in range(8):
			for fg in range(30,38):
				s1 = ''
				for bg in range(40,48):
					format = ';'.join([str(style), str(fg), str(bg)])
					s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
				print(s1)
			print('\n')
	
	@classmethod
	def split(cls, str):
		import re
		return re.split(r'(\033[^m]+m)', str)
