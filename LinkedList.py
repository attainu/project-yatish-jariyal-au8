#Creating Node Class
class Node:
    def __init__(self, slotNo):
        self.next = None
        self.car = None
        self.slotNo = slotNo


#Creating Car Class
class Car:
    def __init__(self, regNo, color):
        self.regNo = regNo
        self.color = color


#Creating LinkedList Class
class LinkedList:
    def __init__(self, size):
        self.size = size
        self.head = None
        self.initLinkedList()

    def addNodeAtHead(self, slotNo):
        # create new node
        newNode = Node(slotNo)
        if not self.head: # when linked list is empty
            self.head = newNode
        else: # not empty
            newNode.next = self.head
            self.head = newNode
        
    # creating linked list of n nodes
    def initLinkedList(self): 
        for i in range(self.size, 0, -1):
            # call add node at start
            self.addNodeAtHead(i)
    
    # printing linked list
    def printLinkedList(self):
        p = self.head
        while p is not None:
            p = p.next

    def addCar(self, regNo, color):
        car = Car(regNo, color)
        singleNode = self.head
        parked = False
        while singleNode is not None:
            if singleNode.car is None:
                print("Allocated slot number:", singleNode.slotNo)
                singleNode.car = car
                parked = True
                break
            else:
                singleNode = singleNode.next
    
        if not parked:
            print("Sorry, parking lot is full")

    def removeCar(self, slotNo):
        singleNode = self.head
        while singleNode is not None:
            if singleNode.slotNo == slotNo:
                print("Slot number", slotNo, "is free")
                singleNode.car = None
                break
            else:
                singleNode = singleNode.next
    

    def parkingStatus(self):
        singleNode = self.head
        print('Slot No. Registration No. Color')
        while singleNode is not None:
            if singleNode.car is not None:
                print(singleNode.slotNo, singleNode.car.regNo, singleNode.car.color)
            singleNode = singleNode.next
    

    def regNoForCarWithColor(self, color):
        regNos = []
        singleNode = self.head
        while singleNode is not None:
            if singleNode.car is not None and singleNode.car.color == color:
                regNos.append(singleNode.car.regNo)
            singleNode = singleNode.next
        
        print(", ".join(regNos)) if len(regNos) > 0 else print('Not Found!')
    

    def slotNoForCarWithColor(self, color):
        slotNos = []
        singleNode = self.head
        while singleNode is not None:
            if singleNode.car is not None and singleNode.car.color == color:
                slotNos.append(str(singleNode.slotNo))
            singleNode = singleNode.next
        
        print(", ".join(slotNos)) if len(slotNos) > 0 else print('Not Found!')
    

    def slotNoForCarWithRegNo(self, regNo):
        slotNos = []
        singleNode = self.head
        while singleNode is not None:
            if singleNode.car is not None and singleNode.car.regNo == regNo:
                slotNos.append(str(singleNode.slotNo))
            singleNode = singleNode.next
        
        print(", ".join(slotNos)) if len(slotNos) > 0 else print('Not Found!')
