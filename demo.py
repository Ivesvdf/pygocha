from pygocha import *

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
