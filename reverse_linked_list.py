class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def add(self, data):
        if not self.head:
            self.head = Node(data)
            return
        # traverse the linked list until we reach the tail 
        cur = self.head
        while(cur.next):
            cur = cur.next
        cur.next = Node(data) 
    
    def print_list(self):
        cur = self.head
        while(cur):
            print(cur.data)  
            cur = cur.next
    # this is why I wanted to make this small script 
    def reverse(self):
        stack = []
        cur = self.head 
        while (cur.next):
            stack.append(cur)
            cur = cur.next
        # re assign the head 
        self.head = cur 
        while( stack ):
            previous = stack.pop()
            cur.next = previous
            cur = previous
        # set tail's next to null 
        cur.next = None
            

def main():


    list = LinkedList() 
    list.add(4)
    list.add(5)
    list.add(6)
    list.add(8)
    list.add(55)
    list.print_list()
    print("reversed")
    list.reverse()
    list.print_list()

if __name__ == '__main__':
    main() 