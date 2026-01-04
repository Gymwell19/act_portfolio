def infix_to_postfix(expression):
    """
    Converts an infix expression to a postfix expression using the Shunting Yard algorithm.
    """
    prec = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    op_stack = []
    postfix_list = []
    
    # Simple tokenization: handle spaces and parentheses
    # This puts spaces around parens so split() works nicely
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token.isalnum():
            # Operand (A, B, 1, 2, etc.)
            postfix_list.append(token)
        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            # Pop until matching '('
            while op_stack and op_stack[-1] != '(':
                postfix_list.append(op_stack.pop())
            if op_stack and op_stack[-1] == '(':
                op_stack.pop() # Discard '('
        elif token in prec:
            # Operator
            # While (stack not empty) and (top is not '(') and
            # (top has greater precedence OR (equal precedence AND left-associative))
            # Note: ^ is right-associative, others are left-associative.
            
            while op_stack and op_stack[-1] != '(':
                top_prec = prec.get(op_stack[-1], 0)
                curr_prec = prec.get(token, 0)
                
                if (top_prec > curr_prec) or \
                   (top_prec == curr_prec and token != '^'):
                    postfix_list.append(op_stack.pop())
                else:
                    break
            op_stack.append(token)
        else:
            # Unknown token (maybe just ignore or treat as operand? safest to treat as operand)
            # But the requirement says "infix expression (string)". 
            # If it's a symbol not in prec, assume operand.
            postfix_list.append(token)

    while op_stack:
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)
