class Logger:

    def __init__(self):
        self.limit = 10
        self.log = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        lastTime = self.log[message]
        if timestamp >= lastTime:
            self.log[message] = timestamp + self.limit
            return True
        return False

        


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
