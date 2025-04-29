from collections import defaultdict

FIZZ_BUZZ_COUNT = 100

# Empty function used for code readability
NO_FUZZBUZZ = lambda n: print(n)

# Initialize implicit "fizz" and "buzz" function table as no conditional branch is allowed by specification

fizz_buzz_function_table = (
    # implicit no action
    defaultdict(lambda: NO_FUZZBUZZ, {
    # all fizz conditions
    (0,4): lambda n: print('A'),
    (0,3): lambda n: print('A'),
    (0,2): lambda n: print('A'),
    (0,1): lambda n: print('A'),
    # all buzz conditions
    (1, 0): lambda n: print('B'),
    (2, 0): lambda n: print('B'),
    # fizz buzz condition
    (0, 0): lambda n: print('AB')
}))

def conditionless_and_loopless_fizzbuzz_print(n=1):
    modulo_3, modulo_5 = n % 3, n % 5
    # As no conditional operators are allowed perform required action by table search
    fizz_buzz_function_table[(modulo_3,modulo_5)](n)
    # Tail recursion fizz buzz enumeration
    tail_recursion_decision_table[n](n + 1)
    return n

# Initialise implicit decision table to stop tail recursion
stop_condition = {FIZZ_BUZZ_COUNT: lambda n: None}
tail_recursion_decision_table = defaultdict(lambda: conditionless_and_loopless_fizzbuzz_print, stop_condition)

# Perform fizz buzz recursive enumeration
conditionless_and_loopless_fizzbuzz_print()
