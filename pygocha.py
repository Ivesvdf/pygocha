class PyGoCha:
	def __init__(self):
		self.__title = ''
		self.__thisSeries = list()
		self.__legendOnly = False
		self.__data = list() 
		self.__labels = list() 

	def title(self, newTitle):
		self.__title = newTitle

	def legendOnly(self):
		self.__legendOnly = True

	def data(self, value):
		self.__thisSeries.append(value)

	def label(self, label):
		self.__labels.append(label)

	def getURL(self, width, height):
		# Place the contents of the working series in 
		# data
		self.newSeries()

		url = "http://chart.apis.google.com/chart?cht="
		url += self.graphName()

		if self.__title != '':
			url += '&chtt=' + self.__title

		url += "&chs=" + str(width) + "x" + str(height)
		url += "&chd=t:"

		total = 0

		pointStrings = list()

		for series in self.__data:
			for point in series:
				total += point

			rescaled = list()

			for point in series:
				rescaled.append(str(100.0*point/total))
			
			pointStrings.append(','.join(rescaled))

		url += '|'.join(pointStrings)

		if self.__legendOnly:
			url += '&chdl='
		else:
			url += '&chl='

		url += '|'.join(self.__labels)
		url += self._afterURL()

		return url
		
	def newSeries(self):
		self.__data.append(self.__thisSeries)

	def _afterURL(self):
		return ''

class Pie(PyGoCha):
	__rotate = 0.0

	def rotate(self,radians):
		self.__rotate = radians

	def _afterURL(self):
		plus = ''

		if self.__rotate != 0.0:
			plus += '&chp=' + str(self.__rotate)

		return plus

	def slice(self, percentage, label):
		self.data(percentage)
		self.label(label)

class ThreeDPie(Pie):
	def graphName(self):
		return "p3"

class TwoDPie(Pie):
	def graphName(self):
		return "p"

class GroupedBarChart(PyGoCha):
	def graphName(self):
		return "bvg"

class StackedBarChart(PyGoCha):
	def graphName(self):
		return "bvs"

class OverlappedBarChart(PyGoCha):
	def graphName(self):
		return "bvo"




