## LC 150. Evaluate Reverse Polish Notation
* use a stack
* if token is a number, add it to the stack
* if token is an operator, pop two numbers and process them with the operator, and push the result to the stack
* return stack.peek()