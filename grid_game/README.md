Python Grid Game
================

This code comes from a tutorial I found at Udemy: [Game Development Fundamentals with Python](https://www.udemy.com/game-development-fundamentals-with-python#/). I found it to be very useful. However, judging from the comments posted, some people who tried it who are very much beginners could not really follow it.

The game is coded in Python 3.x, but I didn't have much trouble changing it to work under Python 2.7.

## Things I learned from the tutorial

* How to make a menu so the player can choose things, like "Start a new game." This was not complex at all, but I had not done it before, so it was a nice way to start out with this tutorial. The menu_choice() function is sort of like a switch-statement.

* How to make a grid and redraw it every time the player moves.

* How to code collision detection (although I suspect there are more elegant ways to do this). Actually this was not the "bullet hits character" type of collision detection but rather the "two characters cannot share the same space" type. So we had to test for all characters every time. It's chessboard logic.

* How to move a player on a grid with keystrokes; also, how to test whether the player's attempted move would take the character off the grid, and prevent that happening. This was very good to learn.

* Recursion: Our tutor is using recursive functions, where I think I would have tried to use a while-loop instead. But it's interesting to see how the [recursion](http://interactivepython.org/courselib/static/pythonds/Recursion/recursionsimple.html) is actually safe to use in these cases.

