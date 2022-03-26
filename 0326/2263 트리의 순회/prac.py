def inorder(V):
    if V:
        inorder(ch1[V])
        print(V, end="-> ")
        inorder(ch2[V])


def postorder(V):
    if V:
        postorder(ch1[V])
        postorder(ch2[V])
        print(V, end="-> ")
        
tree = [0, 1, 2, 3, 4, 5, 6, 7, 0, 8]
ch1 = [0, 2, 4, 6, 0, 0, 0, 0, 0, 0]
ch2 = [0, 3, 5, 7, 0, 8, 0, 0, 0, 0]
inorder(1)
print()
postorder(1)
