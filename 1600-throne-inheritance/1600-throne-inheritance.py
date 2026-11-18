class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)
        self.deadPeople = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)
    def death(self, name: str) -> None:
        self.deadPeople.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        order = []

        def dfs(name):
            if name not in self.deadPeople:
                order.append(name)
            for nei in self.children[name]:
                dfs(nei)
        
        dfs(self.king)
        return order
            
        

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()