PyGoCha is a python library for generating Google Charts url's.

# Some Examples #
![http://chart.apis.google.com/chart?cht=p&chtt=Pacman&chs=700x300&chd=t:80.0,20.0&chl=Percentage%20of%20pie%20that%20is%20Pacman|Percentage%20of%20pie%20that%20is%20not%20Pacman&chp=0.628&something=.png](http://chart.apis.google.com/chart?cht=p&chtt=Pacman&chs=700x300&chd=t:80.0,20.0&chl=Percentage%20of%20pie%20that%20is%20Pacman|Percentage%20of%20pie%20that%20is%20not%20Pacman&chp=0.628&something=.png)
```
two = TwoDPie()
two.title("Pacman")
two.slice(80, "Percentage of pie that is Pacman")
two.slice(20, "Percentage of pie that is not Pacman")
two.rotate(0.628)
print two.getURL(700,300)
```

---


![http://chart.apis.google.com/chart?cht=p3&chtt=A%20Pie%20Chart%20of%20My%20Favorite%20Bars&chs=700x300&chd=t:28.0,30.0,12.0,3.0,27.0&chl=McGees|MacLaurens|White%20Horse%20Tavern|King%20Cole%20Bar|P%20and%20G&something=.png](http://chart.apis.google.com/chart?cht=p3&chtt=A%20Pie%20Chart%20of%20My%20Favorite%20Bars&chs=700x300&chd=t:28.0,30.0,12.0,3.0,27.0&chl=McGees|MacLaurens|White%20Horse%20Tavern|King%20Cole%20Bar|P%20and%20G&something=.png)

```
pgc = ThreeDPie()
pgc.title('A Pie Chart of My Favorite Bars')
pgc.slice(28, "McGee's")
pgc.slice(30, "MacLauren's")
pgc.slice(12, "White Horse Tavern")
pgc.slice(3, "King Cole Bar")
pgc.slice(27, "P and G")
print pgc.getURL(700,300)
```

---


![http://chart.apis.google.com/chart?cht=bvg&chtt=Population%20of%20Countries%20in%20the%20Benelux&chma=100,100,50,0&chs=500x200&chd=t:60.8050589809,100.0,3.04025294905&chxt=y&chxr=0,0,16446000,2000000&chdl=Belgium|The%20Netherlands|Luxembourg&chco=FFC6A5|FFFF42|00A5C6&something=.png](http://chart.apis.google.com/chart?cht=bvg&chtt=Population%20of%20Countries%20in%20the%20Benelux&chma=100,100,50,0&chs=500x200&chd=t:60.8050589809,100.0,3.04025294905&chxt=y&chxr=0,0,16446000,2000000&chdl=Belgium|The%20Netherlands|Luxembourg&chco=FFC6A5|FFFF42|00A5C6&something=.png)

```
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
```

---

![http://chart.apis.google.com/chart?cht=bvg&chtt=Temperature%20in%20Belgium&chs=500x200&chd=t:62.5,62.5,62.5,62.5,62.5,78.125,87.5,100.0,93.75,87.5,78.125,68.75,65.625&chxt=y&chxr=0,0,32,5&chl=0h|2h|4h|6h|8h|10h|12h|14h|16h|18h|20h|22h|24h&something=.png](http://chart.apis.google.com/chart?cht=bvg&chtt=Temperature%20in%20Belgium&chs=500x200&chd=t:62.5,62.5,62.5,62.5,62.5,78.125,87.5,100.0,93.75,87.5,78.125,68.75,65.625&chxt=y&chxr=0,0,32,5&chl=0h|2h|4h|6h|8h|10h|12h|14h|16h|18h|20h|22h|24h&something=.png)
```
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
```

---


# FAQ #
## How do you pronounce it? ##
There are two official ways to pronounce it.
  1. Sounding like Pikachu
  1. Sounding like I Gotcha (PyGotcha)

## Why the name? ##
PyGoCha stands for "a PYthon script for generating GOogle CHArts urls". After hearing that, PyGoCha sounds snappy doesn't it?

## Will you stop talking about names and start talking about the script? ##
Sure, no problem. Although there is an interesting story behind the name...

