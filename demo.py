from pygocha import *

pgc = ThreeDPie()
pgc.title('A Pie Chart of My Favorite Bars')
pgc.slice(28, "McGee's")
pgc.slice(30, "MacLauren's")
pgc.slice(12, "White Horse Tavern")
pgc.slice(3, "King Cole Bar")
pgc.slice(27, "P and G")
print pgc.getURL(700,300)

print ''

two = TwoDPie()
two.title("Pacman")
two.slice(80, "Percentage of pie that is Pacman")
two.slice(20, "Percentage of pie that is not Pacman")
two.rotate(0.628)
print two.getURL(700,300)
print ''

#pop = GroupedBarChart()
#pop.title("Population of Countries in the Benelux")
#pop.legendOnly()
#pop.datapoint(10000000, "Belgium")
#pop.datapoint(16446000, "The Netherlands")
#pop.datapoint(500000, "Luxembourg")
#print pop.getURL(500,500)
