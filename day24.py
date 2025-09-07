class TreeNode:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None

def lowestCommonAncestor(root,p,q):
    if root is None or root.val==p or root.val==q:
        return root
    
    left=lowestCommonAncestor(root.left,p,q)
    right=lowestCommonAncestor(root.right,p,q)
    if left and right:
        return root
    return left if left else right

if __name__=="__main__":
    root=TreeNode(3)
    root.left=TreeNode(5)
    root.right=TreeNode(1)
    root.left.left=TreeNode(6)
    root.left.right=TreeNode(2)
    root.right.left=TreeNode(0)
    root.right.right=TreeNode(8)
    root.left.right.left=TreeNode(7)
    root.left.right.left=TreeNode(4)

    p,q=5,4
    ans=lowestCommonAncestor(root,p,q)
    print("LCA of ",p, "and",q, "is:",ans.val)

    p,q=5,1
    ans=lowestCommonAncestor(root,p,q)
    print("LCA of ",p, "and",q, "is:",ans.val)

    small_root=TreeNode(1)
    small_root.left=TreeNode(2)
    p,q=1,2
    ans=lowestCommonAncestor(small_root,p,q)
    print("LCA of ",p, "and",q, "is:",ans.val)




