class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def insertion(self,value):
        if self.value:
            if value < self.value:
                if self.left == None:
                    self.left = Node(value)
                else:
                    self.left.insertion(value)
            elif value > self.value:
                if self.right == None:
                    self.right=Node(value)
                else:
                    self.right.insertion(value)
        else:
            self.value=value

    def treeDisplay(self):
        if self.left:
            self.left.treeDisplay()
            print(self.data)
        if self.right:
            self.right.treeDisplay()
            print(self.data)
    def postOrderTraversal(self,root):
        treeResult=[]
        if root:
            treeResult = self.postOrderTraversal(root.left)
            treeResult += self.postOrderTraversal(root.right)
            treeResult.append(root.value)
        return treeResult

'''
To test the tree, you have to put a root node, and also you need to
use the insertion method, and finally print the root in the post-order-tr
'''
# print(root.postOrderTraversal(root))
