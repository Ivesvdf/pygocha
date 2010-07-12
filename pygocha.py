# Copyright (c) 2010 Ives van der Flaas
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

class PyGoCha:
	def __init__(self):
		self.__title = ''
		self.__thisSeries = list()
		self.__legendOnly = False
		self.__data = list() 
		self.__labels = list() 
		self.__margins = (0,0,0,0)
		self.__visibleAxes = list()
		self.__xStep = None
		self.__yStep = None
		self.__customAxes = dict()

	def title(self, newTitle):
		""" Sets the graph title"""
		self.__title = newTitle

	def legendOnly(self):
		""" Disables lables on the x-axis and enables the graph
		legend"""
		self.__legendOnly = True

	def data(self, value):
		""" Adds a data point to the current graph """
		self.__thisSeries.append(value)

	def label(self, label):
		""" Adds a x-axis label"""
		self.__labels.append(label)

	def margins(self, left, right, top, bottom):
		""" Sets margins of the graph for respectively left, right,
		top and bottom edges """
		self.__margins = (left, right, top, bottom)

	def getURL(self, width, height):
		""" Returns the url that is to be GET'ed in order to view the
		resulting graph"""
		# Place the contents of the working series in 
		# data
		self.newSeries()

		url = "http://chart.apis.google.com/chart?cht="
		url += self.graphName()

		if self.__title != '':
			url += '&chtt=' + self.__title

		if self.__margins != (0,0,0,0):
			marginStrs =  a = map(lambda x:str(x), self.__margins)
			url += '&chma=' + ','.join(marginStrs)

		url += "&chs=" + str(width) + "x" + str(height)
		url += "&chd=t:"


		pointStrings = list()

		maxima = map(max, self.__data)
		minima = map(min, self.__data)
		maxVal = max(maxima)
		minVal = min(minima)

		# Rescale values
		for series in self.__data:
			rescaled = list()

			for point in series:
				rescaled.append(str(100.0*point/maxVal))
			
			pointStrings.append(','.join(rescaled))

		url += '|'.join(pointStrings)
		
		# Correct & show axis labels
		if len(self.__visibleAxes) > 0:
			if minVal < 0:
				zero = minVal
			else:
				zero = 0
			url += '&chxt=' + ','.join(self.__visibleAxes)

		# If the user enters a step value, we change range for that
		# axis
		if self.__yStep != None:
			url += '&chxr=' + str(self.__visibleAxes.index('y')) \
					+ ',' + str(zero) + ',' + str(maxVal)  \
					+ ',' + str(self.__yStep)


		# Pass trough axis values if the user enters custom labels
		# for each point on some axis
		if len(self.__customAxes) > 0:
			url += '&chxl='

			s = ''

			for axis, labels in self.__customAxes.items():
				s += str(self.__visibleAxes.index(axis)) \
						+ ':|' \
						+ '|'.join(labels) \
						+ '|'

			url += s[0:-1]


		if self.__legendOnly:
			url += '&chdl='
		elif len(self.__labels) > 0:
			url += '&chl='

		url += '|'.join(self.__labels)

		url += self._afterURL()

		return url
		
	def newSeries(self):
		""" Starts a new data series. """
		self.__data.append(self.__thisSeries)
		self.__thisSeries = list()

	def _afterURL(self):
		return ''

#	def showXAxis(self, step):
#		self.__visibleAxes.append('x')
#		self.__xStep = step

	def showYAxis(self, step):
		""" Makes the y axis visible and sets the step (distance
		between marks) """
		self.__visibleAxes.append('y')
		self.__yStep = step


	def addCustomAxisLabel(self, axis, label):
		if axis not in self.__visibleAxes:
			self.__visibleAxes.append(axis)

		if not self.__customAxes.has_key(axis):
			self.__customAxes[axis] = list()

		self.__customAxes[axis].append(label)


class Pie(PyGoCha):
	__rotate = 0.0

	def rotate(self,radians):
		""" Rotates the pie clockwise for "radians" radians. """
		self.__rotate = radians

	def _afterURL(self):
		plus = ''

		if self.__rotate != 0.0:
			plus += '&chp=' + str(self.__rotate)

		return plus

	def slice(self, percentage, label):
		""" Puts the label "label" on "percentage" percent of the pie.
		"""
		self.data(percentage)
		self.label(label)

class ThreeDPie(Pie):
	def graphName(self):
		return "p3"

class TwoDPie(Pie):
	def graphName(self):
		return "p"

class BarChart(PyGoCha):
	def __init__(self):
		PyGoCha.__init__(self)
		self.__seriesColors = list()
		self.__barColors = list()

	def setSeriesColor(self, color):
		""" Call this function for every series and the bars for that
		series will have the color "color". Send color in string
		format in HHHHHH format, H being a hexadecimal number, for
		example '0000FF' for blue. """
		self.__seriesColors.append(color)

	def setBarColor(self, color):
		""" Call this function for every bar and the respective bar
		will have the color you choose for it (same format as
		setSeriesColor). This will probably act weirdly if you're
		using multiple series. Sorry."""
		self.__barColors.append(color)

	def bar(self, data, label):
		""" Adds a new bar to the graph with height "data" and x-axis
		label "label" """
		self.data(data)
		self.label(label)

	def _afterURL(self):
		extra = ''

		if len(self.__seriesColors) > 0:
			extra += '&chco=' + ','.join(self.__seriesColors)

		if len(self.__barColors) > 0:
			extra += '&chco=' + '|'.join(self.__barColors)

		return extra



class GroupedBarChart(BarChart):
	def graphName(self):
		return "bvg"

class StackedBarChart(BarChart):
	def graphName(self):
		return "bvs"

class OverlappedBarChart(BarChart):
	def graphName(self):
		return "bvo"




