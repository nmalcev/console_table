# Table kit v2 2017/01/04
import os
import sys

class Table:
	def __init__(self, width = 0):
		# read number of terminal rows and columns
		buf = os.popen('stty size', 'r').read().split()
		self.rows = int(buf[0])
		self.columns = int(buf[1])

		if width == 0:
			self.width = self.columns
			
	def calc_cell_dimensions(self, columns):
		i = len(columns)
		free_space = self.columns - i - 1
		widths = []
		heights = []

		while i > 0:
			width = int(free_space / i)
			# print('Loop %s %s' % (i, columns[i-1]))
			height = int(len(columns[i-1]) / width) + 1
			free_space -= width
			widths.append(width)
			heights.append(height)
			i -= 1

		return (widths, heights)
	def add_topline(self):
		return '-' * (self.columns - 1)
	# @param {Array} columns
	'''
	TODO create proportional properties for column widths (with sizes at chars )
	'''	
	# TODO widths [0, 1, 1,] - proportial weight, when 0 - auto size, 1..n  is proportial 
	def add_row(self, columns, withHeader = False):
		(columnWidths, colDimensions) = self.calc_cell_dimensions(columns)
		data_table = self.create_matrix(len(columns), max(colDimensions))
		out = ''
		
		if withHeader:
			out += '+'	
			for w in columnWidths:
				out += '-' * w + '+' 
			out += '\n'

		for i, cell in enumerate(columns):
			colSize = columnWidths[i]
			rows = int(len(cell) / colSize) + 1

			for j in range(rows):
				start = j * colSize
				end = (j + 1) * colSize - 1
				data_table[j][i] = self.spread_by_zeros(cell[start:end], colSize)

		for rows in data_table:
			out += '|'

			for i, cell in enumerate(rows):
				colSize = columnWidths[i]
				# cell can be empty (0) or list of chars
				# If cells can out += (cell if cell != 0 else ' ' * colSize) + '|'
				if cell == 0:
					out += ' ' * colSize
				elif type(cell) is list: # Check if array
					out += ''.join(cell)
				else: # else work with string
					out += cell 
				out += '|'
			out += '\n'	
		out += '+'
		
		for w in columnWidths:
			out += '-' * w + '+'
		return out
	def create_matrix(self, w, h):
		return [[0 for x in range(w)] for y in range(h)]
	def spread_by_zeros(self, str, maxWidth):
		out = str
		diff = maxWidth - len(str)
	
		if diff > 0:
			while diff > 0:
				out += ' '
				diff -= 1
		return out

