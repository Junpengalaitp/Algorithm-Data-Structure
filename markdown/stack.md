## LC 150. Evaluate Reverse Polish Notation
* use a stack
* if token is a number, add it to the stack
* if token is an operator, pop two numbers and process them with the operator, and push the result to the stack
* return stack.peek()

# Monotone Stack
## LC 1019. Next Greater Node In Linked List
* reverse the input list, and record its length as n
* init res array with length n
* loop the reversed list, use monotone decreasing stack to get the next greater node value
* decrement n and put stack top to res[n]