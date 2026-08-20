class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None
class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10 ** 4)]
        

    def add(self, key: int) -> None:
        currentPointer = self.set[key % len(self.set)]

        while currentPointer.next:
            if currentPointer.next.key == key:
                return
            currentPointer = currentPointer.next
        currentPointer.next = ListNode(key)    

    def remove(self, key: int) -> None:
        currentPointer = self.set[key % len(self.set)]

        while currentPointer.next:
            if currentPointer.next.key == key:
                currentPointer.next = currentPointer.next.next
                return
            currentPointer = currentPointer.next
        

    def contains(self, key: int) -> bool:
        currentPointer = self.set[key % len(self.set)]

        while currentPointer.next:
            if currentPointer.next.key == key:
                return True
            currentPointer = currentPointer.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
