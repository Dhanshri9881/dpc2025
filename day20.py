def insert_sorted(stack,element):
    if not stack or element>=stack[-1]:
        stack.append(element)
        return 
    temp=stack.pop()
    insert_sorted(stack,element)
    stack.append(temp)
def sort_stack(stack):
    if len(stack)<=1:
        return
    temp=stack.pop()
    sort_stack(stack)
    insert_sorted(stack,temp)

if __name__=="__main__":
    stacks=[
        [3,1,4,2],[7,1,5],[5],[-3,14,8,2],[],[3,3,3]
        ]
    for s in stacks:
        stack=s[:]
        sort_stack(stack)
        print("Input:",s,"=>Sorted:",stack)
