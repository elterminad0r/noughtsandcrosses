# noughtsandcrosses

A CLI noughts and crosses framework in Python. It looks something like this:

	   0  1  2 
	0   |   |   
	 ---+---+---
	1   |   |   
	 ---+---+---
	2   |   |   
	You are playing as noughts
	Enter the position you want to play in > 1 1
	   0  1  2 
	0   |   |   
	 ---+---+---
	1   | O |   
	 ---+---+---
	2   |   |   

Minmax is also implemented - see `writeup`. The version I handed in can be
seen at the
[hand-in tag](https://github.com/goedel-gang/noughtsandcrosses/tree/hand-in).

The serious source code is in `src`. Use `python3 src/play.py -c` to play
against a computer. I also tacked on a ""minimalist"" UI in Processing. The
source code for this is at the top level because of the way Processing like
folders to be. It's generally a little botched because I had to translate things
to Python 2.

![screenshot](https://github.com/goedel-gang/noughtsandcrosses/blob/master/win_screenshot_20180712_110639.png)
