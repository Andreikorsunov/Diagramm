import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fail=open("TextFile1.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()

title = "Данные о ИТ безопасности"
plt.grid(True)

color_rectangle = np.random.rand(7, 3)
plt.bar(mas1, mas2, color=color_rectangle)

plt.show()

#Формирование данных и построение диаграммы
x1=np.arange(0,10)
y1=(2/27)*(x1**2)-3

x2=np.arange(-10,1)
y2=(0.04)*(x2**2)-3

x3=np.arange(-9,-2)
y3=(2/9)*((x3+6)**2)+1

x4=np.arange(-3,9)
y4=-1*(1/12)*((x4-3)**2)+6

x5=np.arange(5,9.3)
y5=(1/9)*((x5-5)**2)+2

x6=np.arange(5,9.5)
y6=(1/8)*((x6-7)**2)+1.5

x7=np.arange(-13,-8)
y7=-0.75*((x7+11)**2)+6

x8=np.arange(-15,-12)
y8=-0.5*((x8+13)**2)+3

x9=np.arange(-15,-9)
y9=[1]*len(x9)

x10=np.arange(3,5)
y10=[3]*len(x10)

plt.subplots()
plt.title("Кит")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")

plt.grid(axis="x", color="k")

plt.xticks(np.arange(-8, 8, 1))
plt.yticks(np.arange(-8, 8, 1))

plt.grid(True)# Отображение сетки на координатной плоскости

plt.plot(x1,y1,'b',linewidth=5)
plt.plot(x2,y2,'b',linewidth=5)
plt.plot(x3,y3,'b',linewidth=5)
plt.plot(x4,y4,'b',linewidth=5)
plt.plot(x5,y5,'b',linewidth=5)
plt.plot(x6,y6,'b',linewidth=5)
plt.plot(x7,y7,'b',linewidth=5)
plt.plot(x8,y8,'b',linewidth=5)
plt.plot(x9,y9,'b',linewidth=5)
plt.plot(x10,y10,'b',linewidth=5)

plt.savefig("my_image.png")  # Сохранение изображения или
plt.show()  # Вывод изображения на экран


x1=np.arange(-12,13)
y1=-1*(1/18)*(x1**2)+12

x2=np.arange(-4,5)
y2=-1*(1/8)*(x2**2)+6

x3=np.arange(-12,-3)
y3=-1*(1/8)*((x3+8)**2)+6

x4=np.arange(4,13)
y4=-1*(1/8)*((x4-8)**2)+6

x5=np.arange(-4,0.7)
y5=2*((x5+3)**2)-9

x6=np.arange(-4,1.2)
y6=1.5*((x6+3)**2)-10

plt.subplots()
plt.title("Зонтик")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")

plt.grid(axis="x", color="k")

plt.xticks(np.arange(-8, 8, 1))
plt.yticks(np.arange(-8, 8, 1))

plt.grid(True)# Отображение сетки на координатной плоскости

plt.plot(x1,y1,'b',linewidth=5)
plt.plot(x2,y2,'b',linewidth=5)
plt.plot(x3,y3,'b',linewidth=5)
plt.plot(x4,y4,'b',linewidth=5)
plt.plot(x5,y5,'b',linewidth=5)
plt.plot(x6,y6,'b',linewidth=5)

plt.savefig("my_image.png")  # Сохранение изображения или
plt.show()  # Вывод изображения на экран


x1=np.arange(-9,0)
y1=-1*(1/16)*((x1+5)**2)+2

x2=np.arange(1,10)
y2=-1*(1/16)*((x2-5)**2)+2

x3=np.arange(-9,0)
y3=1/4*((x3+5)**2)-3

x4=np.arange(1,10)
y4=1/4*((x4-5)**2)-3

x5=np.arange(-9,-5)
y5=-1*((x5+7)**2)+5

x6=np.arange(6,10)
y6=-1*((x6-7)**2)+5

x7=np.arange(-1,2)
y7=-0.5*(x7**2)+1.5

plt.subplots()
plt.title("Очки")
plt.xlabel("Ось абсцисс")
plt.ylabel("Ось ординат")

plt.grid(axis="x", color="k")

plt.xticks(np.arange(-8, 8, 1))
plt.yticks(np.arange(-8, 8, 1))

plt.grid(True)# Отображение сетки на координатной плоскости

plt.plot(x1,y1,'b',linewidth=5)
plt.plot(x2,y2,'b',linewidth=5)
plt.plot(x3,y3,'b',linewidth=5)
plt.plot(x4,y4,'b',linewidth=5)
plt.plot(x5,y5,'b',linewidth=5)
plt.plot(x6,y6,'b',linewidth=5)
plt.plot(x7,y7,'b',linewidth=5)

plt.savefig("my_image.png")  # Сохранение изображения или
plt.show()  # Вывод изображения на экран

