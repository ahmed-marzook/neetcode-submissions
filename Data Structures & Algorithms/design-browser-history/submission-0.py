class Node:
    def __init__(self, url: string, next: "Node" = None, prev: "Node" = None):
        self.url= url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)
        
    def visit(self, url: str) -> None:
        newVisit = Node(url);
        self.current.next = newVisit
        newVisit.prev = self.current
        self.current = newVisit
        

    def back(self, steps: int) -> str:
        i = 0

        while self.current.prev and i < steps:
            self.current = self.current.prev
            i += 1
        
        return self.current.url

        

    def forward(self, steps: int) -> str:
        i = 0
        while self.current.next and i < steps:
            self.current = self.current.next
            i += 1
        
        return self.current.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)