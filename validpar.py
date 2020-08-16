def validation(string):
    stack = []
    for i in string:
        if(i == '('):
            stack.append(i)
        elif(i == ')'):
            if(len(stack) == 0):
                return False
            else: 
                stack.pop()
    if(len(stack) == 0):
        return True
    return False

print(validation(")(()))"))
