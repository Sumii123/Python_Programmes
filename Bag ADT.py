class Bag():
    def __init__(self,maxsize=10):
        self.maxsize = maxsize
        self.item = list()
    
    def add(self,item):
        if len(self) >= self.maxsize:
            raise Exception("full")
        self.item.append(item)

    def remove(self,item):
        self.item.remove(item)

    def __len__(self):
        return len(self.item)

    def __iter__(self):
        for item in self.item:
            yield item

    def display(self):
        print("the elements in bag are:")
        for i in self.item:
            print(i)

bag = Bag()
a = int(input("enter the number of elements you want to add to bag"))
for i in range(a):
    print("enter element ",i+1)
    element = int(input())
    bag.add(element)
bag.display()

    