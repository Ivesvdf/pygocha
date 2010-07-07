class PyGoCha:
	thisSeries = list()
	__title = ''

	def __init__(self):
		self.__title = ''
		self.thisSeries = list()

	def title(self, newTitle):
		self.__title = newTitle

	def getURL(self, width, height):
		url = "http://chart.apis.google.com/chart?cht="
		url += self.graphName()

		if self.__title != '':
			url += '&chtt=' + self.__title

		url += "&chs=" + str(width) + "x" + str(height)
		url += "&chd=t:"

		total = 0

		for point in self.thisSeries:
			total += point[0]

		rescaled = list()

		for point in self.thisSeries:
			rescaled.append((100.0*point[0]/total, point[1]))
		
		points = map(lambda x: str(x[0]), rescaled)
		
		url += ','.join(points)

		labels = map(lambda x: x[1], rescaled)

		url += '&chl=' + '|'.join(labels)
		url += self._afterURL()

		return url
		

	def datapoint(self, value, label):
		self.thisSeries.append((value, label))

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

pgc = ThreeDPie()
pgc.title('My Favorite Bars')
pgc.datapoint(28, "McGee's")
pgc.datapoint(30, "MacLauren's")
pgc.datapoint(12, "White Horse Tavern")
pgc.datapoint(3, "King Cole Bar")
pgc.datapoint(27, "P&amp;G")
print pgc.getURL(600,300)

print ''

two = TwoDPie()
two.title("Pacman")
two.datapoint(80, "Percentage of pie that is Pacman")
two.datapoint(20, "Percentage of pie that is not Pacman")
two.rotate(0.628)
print two.getURL(700,300)


