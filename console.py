# TODO refactor
class C:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	LIME = '\x1b[6;30;42m'

	@classmethod
	def echo(cls, str, beginColor, endColor = '\033[0m'):
		return beginColor + str + endColor	
	# prints table of formated text format options	
	@classmethod
	def print_format_table(cls):
		for style in range(8):
			for fg in range(30,38):
				s1 = ''
				for bg in range(40,48):
					format = ';'.join([str(style), str(fg), str(bg)])
					s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
				print(s1)
			print('\n')
