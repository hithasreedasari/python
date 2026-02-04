# python
experience with python

#TODO implement my own project

Firstly, for developing a huge project we need to get comfortable with python syntax, usage of functions, file handling. 
So we need to implement small projects like greeting, number guessing game, TODO list, Rock paper scissors game.

# Greet_by_time
## What I used
- Python 3
- `datetime` module from the standard library
- A single helper function (`greet_by_time`) with an optional `datetime` parameter

## What I did
- Implemented a function that returns an appropriate greeting based on the current time
- Added a small runnable example that prints the greeting when the file is executed

## How I did it
- Read the current time with `datetime.now()` when no argument is provided
- Mapped hour ranges to greetings (morning, afternoon, evening, night)
- Returned the greeting string and printed it in the `__main__` block

## What I learnt
- How to use `datetime` to access the current system time
- How to design a small, testable function with an optional parameter
- How to structure a simple Python script with a clean entry point



