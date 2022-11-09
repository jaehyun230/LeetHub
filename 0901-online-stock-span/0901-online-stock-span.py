class StockSpanner:

    def __init__(self):
        self.mono = []

    def next(self, price: int) -> int:
        count = 1
        if self.mono :
            while self.mono and self.mono[-1][0] <= price:
                count += self.mono[-1][1]
                self.mono.pop()
        self.mono.append((price, count))
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)