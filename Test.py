# a testing file for a new stack-like array implementation.

# initialize my stack array implementation
stack = ["a", "b", "c"]
print(stack)

# add a new element and make sure it's at the end.
stack.append("d")
print(stack)

# pop off the last element and make sure that the list is now [a, b, c].
stack.pop()
print(stack)

# pop off any of the elements. Tried: out-of-bounds indices. Got: IndexError.
# Negative indices are 1-indexed.
stack.pop(-3)
print(stack)
