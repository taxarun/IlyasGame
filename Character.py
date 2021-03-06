# coding=utf-8
from tkinter import *


class Character:
    # Это конструктор класса, так при его инициализации человечек отрисуется
    # в заданной позиции
    def __init__(self, x_position, y_position, canvas):
        # Как видишь, self.[имя атрибута] создает атрибут класса
        # сейчас созданы атрибуты для x и y, а так же
        # канвас для взаимодействия с ним. Как видишь, они
        # используются в других методах класса.
        # Я так подозреваю, что здесь так же нужны атрибуты
        # для хранения частей тела человечка :)
        self.x_pos = x_position
        self.y_pos = y_position
        self.canvas = canvas
        self.draw()

    def draw(self):
        c = self.canvas
        # Кажется, тут нужен код отрисовки...
        # Нужно помнить, что мы можем
        # взаимодействовать с переменными
        # self.x_pos и self.y_pos, в которых
        # можно хранить текущее положение человечка

    # Идея функции в том, чтобы смещать человечка на сколько-то пикселей
    def move_on(self, x, y):
        self.x_pos += x
        self.y_pos += y
        # А тут нужен код перемещения человечка