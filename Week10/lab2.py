class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def preorder_traversal(root):
    
    #如果根节点为空
    if root is None:
        return 
    print(root.val,end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def inorder_traversal(root):
    
    #如果根节点为空
    if root is None:
        return 
    inorder_traversal(root.left)
    print(root.val,end=' ')
    inorder_traversal(root.right)

#层次遍历
def level_order_traversal(root):
    queue = []
    queue.append(root)
    #根节点先入队列
    while queue:
        current = queue.pop(0)
        print(current.val, end=' ')
        if current.right:
            queue.append(current.right)
        if current.left:
            queue.append(current.left)

        
        

if __name__ == "__main__":
    #创建一个简单的二叉树
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("前序遍历:")
    preorder_traversal(root)  # 输出: 1 2 4 5 3
    print("\n中序遍历:")
    inorder_traversal(root)   # 输出: 4 2 5 1 3
    print("\n层次遍历:")
    level_order_traversal(root)  # 输出: 1 2 3 4 5
        