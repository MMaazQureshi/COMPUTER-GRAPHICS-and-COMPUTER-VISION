from turtle import *
import csv

color('black')
# speed(1)
listing01 = []

# begin_fill()

forward(200)
right(90)
print('1',pos())
listing01.append(pos())
forward(200)
right(90)
print('2',pos())
listing01.append(pos())
forward(200)
right(90)
print('3',pos())
listing01.append(pos())
forward(200)
right(45)
listing01.append(pos())
print('4',pos())
forward(200)
right(45)
listing01.append(pos())
print('5',pos())
forward(200)
right(90)
listing01.append(pos())
print('6',pos())
forward(200)
right(90)
listing01.append(pos())
print('7',pos())
forward(200)
right(90)
listing01.append(pos())
print('8',pos())
forward(200)
backward(200)
right(45)
backward(200)
right(45)
forward(200)
left(45)
forward(200)
left(45)
forward(200)
left(135)
forward(200)
print(listing01)

color_count = 0
with open('test.csv','w',newline='') as csvfile:
    feildnames = ['Number of Vertices','Rectangular Co-ordinates']
    thewriter = csv.DictWriter(csvfile,fieldnames=feildnames)
    thewriter.writeheader()
    for coords in listing01:
        color_count += 1
        thewriter.writerow({'Number of Vertices':color_count,'Rectangular Co-ordinates':coords})


# while True:
#     forward(20)    
#     right(10)  
#     # print(pos())
#     if abs(pos()) < 1:
#         break
# end_fill()

done()
