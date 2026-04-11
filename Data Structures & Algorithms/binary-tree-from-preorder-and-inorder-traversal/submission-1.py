# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Step 1: Build hashmap of inorder value -> index
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(pre_start: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            if pre_start >= len(preorder) or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # Step 2: Get root index in inorder using hashmap
            in_index = inorder_map[root_val]

            # Step 3: Number of nodes in the left subtree
            left_size = in_index - in_start

            # Step 4: Recurse for left and right subtrees
            root.left = helper(pre_start + 1, in_start, in_index - 1)
            root.right = helper(pre_start + 1 + left_size, in_index + 1, in_end)

            return root

        return helper(0, 0, len(inorder) - 1)

