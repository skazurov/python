from graph import *

penColor("black")
penSize(1)
#### Овал головы
brushColor("yellow")
circle(250, 300, 100)
#### Левый глаз
brushColor("red")
circle(200, 270, 20)
#### Правый глаз
circle(295, 270, 15)
brushColor("black")
circle(200, 270, 8)
circle(295, 270, 7)
#### Рот
brushColor("black")
polygon([(200,350), (300,350),
         (300,370), (200,370)])
#### Левая бровь
brushColor("black")
polygon([(164,215), (240,262),
         (235,268), (160,221)])
#### Правяя бровь
brushColor("black")
polygon([(265,258), (342,226),
          (345,233), (268,265)])

run()
