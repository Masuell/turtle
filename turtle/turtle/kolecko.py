import turtle
from turtle import *

def nakresli_kruh(tvar,velkost,farba,stupanie,polomer):
    """
        Popis tejto funkcie
        Param: ksjfh kdlf
    """
    tess=turtle.Turtle()
    tess.shape(tvar)
    tess.color(farba)
    tess.penup()

    for x in range(int(360/stupanie)):
        tess.forward(polomer)
        tess.stamp()
        tess.left(180)
        tess.forward(polomer)
        tess.left(180)
        tess.left(stupanie)
    tess.penup()
    tess.forward(polomer)

nakresli_kruh('turtle',5,'red',20,100)
