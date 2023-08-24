## Array
A =[1,2,3,4,5,6,7,8,9]


## linked list 

# class Node:
#     def __init__(self,val,next=None) -> None:
#         self.data = val
#         self.next = next
    

# class LinkedList:
#     def __init__(self) -> None:
#         self.head = None

#     def indert_at_begining(self,data):
       
#         node = Node(data,self.head)
#         self.head = node

#     def indert_at_end(self,data):
#         node =Node(data)
#         if self.head is None:
#             self.head = node
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next

#         itr.next = node



#     def printing(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr =''
#         while itr:
#             # print(itr.data)
#             llstr += str(itr.data) + "--->"
#             itr = itr.next
#         print(llstr)

#     def getlenght(self):
#         count =0
#         if self.head is None:
#             return count
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next
            
#         return count
    
#     def insert_values(self,datalis):
#         self.head=None
#         for i in datalis:
#             self.indert_at_end(i)

#     def insert_at(self,index,data):
#         if index <0 and index > self.getlenght():
#             print("provide valid index")
#             return 
        
#         if index ==0:
#             self.indert_at_begining(data)
#             return

#         count = 0
#         itr=self.head
#         while itr:
#             if count ==index-1:
#                 node = Node(data,itr.next)
#                 itr.next = node
#                 break

#             itr=itr.next
#             count=count+1

#     def remove_at(self,index):
#         if index <0 and index > self.getlenght():
#             print("provide valid index")
#             return 
        
#         if index ==0:
#             self.head = self.head.next
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index-1:
#                 node = itr.next
#                 itr.next= node.next
            
#             itr = itr.next
#             count +=1




# if __name__ == '__main__':
#     obj = LinkedList( )

#     obj.insert_values([44,89,9,23,89])
#     obj.indert_at_end(99)
    
#     obj.insert_at(5,77)
#     print(obj.getlenght())
#     obj.remove_at(5)
#     print(obj.getlenght())
#     obj.printing()




        

## hash map 
class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data = data
        self.next = next
class Hashmap:
    def __init__(self) -> None:
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        h= 0 
        for char in key:
            h+= ord(char)
        return h%100
    
    def add(self,key,value):
        h = self.get_hash(key)
        found = False
        for idx,val in enumerate(self.arr[h]):
            if len(val) ==2 and val[0] == key:
                self.arr[h][idx].append((key,value ))
                found = True
                break
        
        if not found:
            self.arr[h].append((key,value))

    def remove(self,key):
        self.arr[self.get_hash(key)] = None

    def get(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            # print(element)
            if element[0] ==key:
                return element[1]

        # return self.arr[self.get_hash(key)]

    
obj  = Hashmap()
obj.add("march 9 ", 180)
obj.add("march 6 ", 1)
obj.add("march 7 ", 42)
obj.add("march 17 ", 100)

print(obj.get("march 17 "))

print(obj.arr)