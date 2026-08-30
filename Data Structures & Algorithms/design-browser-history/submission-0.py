class BrowserHistory:

    def __init__(self, homepage: str):

        self._data = [homepage]
        self.current = 0 

    def visit(self, url: str) -> None:

        self.current += 1

        if self.current >= len(self._data):
            self._data.append(url)
            return
        
        self._data = self._data[:self.current]
        self._data.append(url)
        return

        

    def back(self, steps: int) -> str:

        index = max(0, self.current - steps)
        self.current = index
        return self._data[self.current]

    def forward(self, steps: int) -> str:

        index = min(len(self._data)- 1, self.current + steps)
        self.current = index
        return self._data[self.current]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)