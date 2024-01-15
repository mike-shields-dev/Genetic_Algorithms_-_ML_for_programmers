from turtle import *


def X(count):
    if count > 0:
        draw_line("X+YF+", count)

def Y(count):
    if count > 0:
        draw_line("-FX-Y", count)
        
def draw_line(instructions, count):
    for instruction in instructions:
        match instruction:
            case '-':
                lt(90)
            case '+':
                rt(90)
            case 'X':
                X(count-1)
            case 'Y':
                Y(count-1)
            case 'F':
                fd(2)
                
X(491)

done()