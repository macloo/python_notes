Python Grid Game
================

This code comes from a tutorial I found at Udemy: [Game Development Fundamentals with Python](https://www.udemy.com/game-development-fundamentals-with-python#/). I found it to be very useful. However, judging from the comments posted, some people who tried it who are very much beginners could not really follow it.

The game is coded in Python 3.x, but I didn't have much trouble changing it to work under Python 2.7.

## Objective of the game

The player (represented by P) moves one square at a time. If player finds flask, player wins. If player finds trap, monster (M) wakes up and chases player. If monster finds player, player loses. The number of moves given to the monster can be changed.

## Things I learned from the tutorial

* How to make a menu so the player can choose things, like "Start a new game." This was not complex at all, but I had not done it before, so it was a nice way to start out with this tutorial. The menu_choice() function is sort of like a switch-statement.

* How to make a grid and redraw it every time the player moves.

* How to code collision detection (although I suspect there are more elegant ways to do this). This was not the "bullet hits character" type of collision detection but rather the "two characters cannot share the same space" type. So we had to test for all characters every time. It's chessboard logic.

* How to move a player on a grid with keystrokes; also, how to test whether the player's attempted move would take the character off the grid, and prevent that happening. This was very good to learn.

* Recursion: Our tutor is using recursive functions, where I think I would have tried to use a while-loop instead. But it's interesting to see how the [recursion](http://interactivepython.org/courselib/static/pythonds/Recursion/recursionsimple.html) is actually safe to use in these cases. In the "place" functions, I think recursion makes more sense than in the draw_grid() function.

* I like the way our tutor's functions often return only True or False. I don't usually think that way when I'm trying to write code. It makes sense. I learned to appreciate this technique through his step-by-step approach.

* I also like how the x, y for each position was saved as a list. That was new to me. In many places, this saves you one line of code.

