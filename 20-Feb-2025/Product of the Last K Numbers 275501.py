# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.product = [1]

    def add(self, num: int) -> None:
        if num:
            self.product.append(self.product[-1] * num)
        else:
            self.product = [1]
              

    def getProduct(self, k: int) -> int:
        n = len(self.product) - 1
        if k > n:
            return 0
        else:
            return self.product[-1] // self.product[n-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)