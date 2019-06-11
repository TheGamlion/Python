class Graph:
    edges = {}
    
    def  add_entry(self,dic):
        self.edges.update(dic)

#returns liste mit direkt verbunden Knoten
    def get_connections(self,num1):
        return self.edges[num1]

    def del_entry(self,num1):
        self.edges.pop(num1)
        for x in self.edges:
            try:
                self.edges[x].remove(num1)
            except ValueError:
                pass

    def __repr__(self):
        for x in self.edges:
            print (x, " ", self.edges[x])
        return ""

    def check_way(self, num1, num2):
        for x in self.edges[num1]:
            if x == num2:
                return True
        return False









graph = Graph()
graph.add_entry({1:[2,3]})
graph.add_entry({2:[1,3,4,5]})
graph.add_entry({3:[1,2,5]})
graph.add_entry({4:[2,5]})
graph.add_entry({5:[2,3,4]})


print(graph)
graph.del_entry(1)

print(graph)