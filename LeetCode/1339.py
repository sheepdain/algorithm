class Solution:
    def maxProduct(self, root):
        MOD = 10**9 +7

        def get_total_sum(node):
            if not node:
                return 0
            return (node.val + get_total_sum(node.left) + get_total_sum(node.right))
        total = get_total_sum(root)

        # 최대 곱을 저장할 변수(DFS 전체에서 공유해야 하므로 self 사용)
        self.max_product =0

        def dfs(node):
            if not node:
                return 0
            
            # 좌우 서브트리 합
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # 현재 노드를 루트로 하는 서브트리 합
            subtree_sum = node.val +left_sum + right_sum

            ans=subtree_sum * (total - subtree_sum)
            self.max_product = max(self.max_product, ans)

            #부모 노드를 위해 서브트리 반환
            return subtree_sum
        
        dfs(root)

        return self.max_product % MOD