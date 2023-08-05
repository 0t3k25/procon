class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        purchaseAmount = str(purchaseAmount)
        if int(purchaseAmount[-1]) >= 5:
            number = int(purchaseAmount[-1])
            add_num = 10 - number
            return 100 - (int(purchaseAmount) + add_num)
        elif int(purchaseAmount[-1]) < 5:
            number = int(purchaseAmount[-1])
            return 100 - (int(purchaseAmount) - number)
        else:
            return 100 - purchaseAmount
