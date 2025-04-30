# Description
As the specification forbids the use of conditional statements, explicit branching instructions and loops the program contains the following workarounds:
* Loop from 1 to 100 is replaced with **tail recursion**.
* Conditional statements and branch instructions are replaced with **implicit exhaustive table** containing lambda functions. `defaultdict` is used for the sake of code clarity.

# Requirements
* Python (any decent version)

