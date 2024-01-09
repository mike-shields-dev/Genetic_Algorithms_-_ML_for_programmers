# Chapter 1 Escape

## About

This chapter introduces the Python library [turtle](https://docs.python.org/3/library/turtle.html), which is inspired by the programming language [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)).

The library can be used to direct a cursor (turtle) to draw geometric shapes on a canvas using a set of rudimentary instructions.

Firstly, a "brown paper bag" is drawn on the screen and then various algorithms position the cursor in the center of the bag and proceed to move the cursor in different ways to "escape" from the "bag". 

Each algorithm uses looping structures such as `for` and `while` to implement repetitive behaviour and also observe the position of the turtle at regular intervals, to confirm that the turtle has or has not escaped from the bag. 

The turtle has escaped when its position is outside the bounding rectangle of the bag. If this condition is met, this is the terminating condition of each algorithm. 

In addition, the turtles' positional history is stored and dumped as data files to be used in later chapters....

## How to run 

To run the `draw_line` algorithm:
```bash
> python3 -m Chapter1_Escape.main --function=line
> python3 -m Chapter1_Escape.main -f=line
```

To run the `draw_squares` algorithm:
```bash
> python3 -m Chapter1_Escape.main --function=squares
> python3 -m Chapter1_Escape.main -f=squares
```

To run the `draw_spirals` algorithm:
```bash
> python3 -m Chapter1_Escape.main --function=spirals
> python3 -m Chapter1_Escape.main -f=spirals
```

In addition, a `-n` or `--number` flag can be used to determine the number of repetitions of the `squares` and `spirals` algorithms. 

For example:

To run the `draw_spirals` algorithm 5 times:
```bash
> python3 -m Chapter1_Escape.main --function=spirals -n=5
```

```bash
> python3 -m Chapter1_Escape.main -f=spirals --number=5
```