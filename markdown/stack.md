### LC 32. Longest Valid Parentheses
* use a stack, init with an element -1
* loop the str, add index to the stack if current char is '('
* pop the stack if current char is ')'
* if the stack after pop in not empty, update the res to max(res, index - stack.peek())
* else add current index to the stack

### LC 71. Simplify Path
* use a stack, and split the path by "/"
* add the spitted string to stack, if path is "." or empty, do nothing
* if string is "..", pop from the stack
* else add the string to the stack
* return "/" + "/" join the stack element

## LC 150. Evaluate Reverse Polish Notation
* use a stack
* if token is a number, add it to the stack
* if token is an operator, pop two numbers and process them with the operator, and push the result to the stack
* return stack.peek()

# Monotone Stack

### LC 85. Maximal Rectangle

## LC 1019. Next Greater Node In Linked List
* reverse the input list, and record its length as n
* init res array with length n
* loop the reversed list, use monotone decreasing stack to get the next greater node value
* decrement n and put stack top to res[n]