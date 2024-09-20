# Python 101
This is sample code for teaching clean code 101.

# Hands-On

## Implementing Simple Functions and Test Code
This tasks is first hands on with [pytest][pytest].

1. Clone this repository
2. Create a branch named `calculator`.
3. Write two stub functions in [`src/calculator.py`](src/calculator.py), one for summation and one for division.
   These functions should raise an `NotImplementedError`.
4. Write tests for both functions in [`src/test/test_calculator.py`](src/test/test_calculator.py)
5. Push your changes
	- Fork the repository in the GitHub UI
	- Add your new remote to your local git repositors (see `man git-remote`)
	- Open a Pull-Request against this repository

## Refactoring a CSV-Parser
The file [`src/parser.py`](src/parser.py) implements a CVS parser.
Importantly, the parser is still a prototype and does not follow clean coding practices.
Refactor the code with the following bullet points in mind:
- Use functions where appropiate
- Use builtin python libaries (i.e. `pathlib` and `argparse`) where appropiate
    - Optionally use `click` instead of `argparse`
- Use list comprehensions for simple list modifications
- Use _f-strings_ for string formatting



[pytest]: https://docs.pytest.org/en/stable/
