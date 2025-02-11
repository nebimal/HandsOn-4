### HandsOn-4

## Problem 0


Fib(5) -> Fib(4) + Fib(3) -> 3 + 2 = 5
- Fib(4) -> Fib(3) + Fib(2) -> 2 + 1 = 3
- Fib(3) -> Fib(2) + Fib(1) -> 1 + 1 = 2
- Fib(2) -> Fib(1) + Fib(0) -> 1 + 0 = 1
- Fib(1) -> 1
- Fib(0) -> 0

Fib(5) -> Fib(4) -> Fib(3) -> Fib(2) -> Fib(1) -> Fib(0) -> Fib(1) -> Fib(2) -> Fib(1) -> Fib(0) -> Fib(3) -> Fib(2) -> Fib(1) -> Fib(0) -> Fib(1)

## Problem 1

# Time Complexity

- The while loop runs O(NK) times.

- The for loop runs O(K) times per iteration.

- Final time complexity: O(NK²)

# Ways to Improve

- Using a Min-Heap would reduce the time complexity.

## Problem 2

# Time Complexity

- The for loop runs O(N).

- Each append() operation runs in O(1).

- Final time complexity: O(N)

# Ways to Improve

- Already time optimal. Not much improvement can be made since we need to loop through the array.
