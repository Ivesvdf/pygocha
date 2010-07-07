class PyGoCha:
	thisSeries = list()

	def __init__(self):
		pass

	def getURL(self, width, height):
		url = "http://chart.apis.google.com/chart?cht="
		url += self.graphName()
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

		return url
		

	def datapoint(self, value, label):
		self.thisSeries.append((value, label))


class ThreeDPie(PyGoCha):
	def graphName(self):
		return "p3"

pgc = ThreeDPie()
pgc.datapoint(10, "Haat voor x")
pgc.datapoint(90, "Liefde voor x")
print pgc.getURL(400,200)


