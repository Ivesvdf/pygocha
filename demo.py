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

pop = GroupedBarChart()
pop.title("Population of Countries in the Benelux")
pop.margins(100,100,50,0)
pop.legendOnly()
pop.showYAxis(2000000)

pop.bar(10000000, "Belgium")
pop.setBarColor('FFC6A5')
pop.bar(16446000, "The Netherlands")
pop.setBarColor('FFFF42')
pop.bar(500000, "Luxembourg")
pop.setBarColor('00A5C6')
print pop.getURL(500,200)
print ''

temp = GroupedBarChart()
temp.title("Temperature in Belgium")
temp.showYAxis(5)

temp.bar(20, '0h')
temp.bar(20, '2h')
temp.bar(20, '4h')
temp.bar(20, '6h')
temp.bar(20, '8h')
temp.bar(25, '10h')
temp.bar(28, '12h')
temp.bar(32, '14h')
temp.bar(30, '16h')
temp.bar(28, '18h')
temp.bar(25, '20h')
temp.bar(22, '22h')
temp.bar(21, '24h')

print temp.getURL(500,200)
