from picture import *
from turtle import *
ans = input('Сейчас день/ночь?')
if ans == 'день':
    background('green','skyblue')
    sun()
    house_light('darkgrey')
    window_light(-140, -120)
    window_light(-60, -120)
    window_light(-140, -50)
    window_light(-60, -50)
    window_light(-140, 30)
    window_light(-60, 30)
if ans == 'ночь':
    background('darkgreen','midnightblue')
    moon()
    house_dark('grey')
    window_dark(-140, -120)
    window_dark(-60, -120)
    window_dark(-140, -50)
    window_dark(-60, -50)
    window_dark(-140, 30)
    window_dark(-60, 30)
exitonclick()
