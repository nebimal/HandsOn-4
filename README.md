# HandsOn-4

## Problem 0

Fib(5) -> Fib(4) + Fib(3) -> 3 + 2 = 5
- Fib(4) -> Fib(3) + Fib(2) -> 2 + 1 = 3
- Fib(3) -> Fib(2) + Fib(1) -> 1 + 1 = 2
- Fib(2) -> Fib(1) + Fib(0) -> 1 + 0 = 1
- Fib(1) -> 1
- Fib(0) -> 0

- Fib(5) -> Fib(4) -> Fib(3) -> Fib(2) -> Fib(1) -> Fib(0) -> Fib(1) -> Fib(2) -> Fib(1) -> Fib(0) -> Fib(3) -> Fib(2) -> Fib(1) -> Fib(0) -> Fib(1)

## Problem 1
In the while loop, it runs for O(NK).
In the for loop, it runs for O(k).
Final time complexity would be O(NK^2)
