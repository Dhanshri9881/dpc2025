def insert_bottom(stack,x):
    if len(stack)==0:
        stack.append(x)
        return
    temp=stack.pop()
    insert_bottom(stack,x)
    stack.append(temp)
def reverse_stack(stack):
    if len(stack)==0:
        return
    temp=stack.pop()
    reverse_stack(stack)
    insert_bottom(stack,temp)
stack=[1,2,3,4]
reverse_stack(stack)
print(stack)
        
