from LinkedList import Car, Node, LinkedList
import sys

parkingLot = None

#Creating Parking Lot
def createParkingLot(size):
    global parkingLot
    parkingLot = LinkedList(size)

#Printing Parking Lot
def printParkingLot():
    global parkingLot
    parkingLot.printLinkedList()

#Parking Car in Parking Lot
def parkCar(regNo, color):
    global parkingLot
    parkingLot.addCar(regNo, color)

#Leaving Car from Parking Lot
def leaveCar(slotNo):
    global parkingLot
    parkingLot.removeCar(slotNo)

#Commands for testing

def runCommand(command):
    global parkingLot
    splitted = command.split(" ")
    if splitted[0] == 'create_parking_lot':
        size = int(splitted[1])
        createParkingLot(size)
        printParkingLot()
    elif splitted[0] == 'park':
        regNo = splitted[1]
        color = splitted[2]
        parkCar(regNo, color)
    elif splitted[0] == 'leave':
        slotNo = int(splitted[1])
        leaveCar(slotNo)
    elif splitted[0] == 'status':
        parkingLot.parkingStatus()
    elif splitted[0] == 'registration_numbers_for_cars_with_colour':
        color = splitted[1]
        parkingLot.regNoForCarWithColor(color)
    elif splitted[0] == 'slot_numbers_for_cars_with_colour':
        color = splitted[1]
        parkingLot.slotNoForCarWithColor(color)
    elif splitted[0] == 'slot_number_for_registration_number':
        regNo = splitted[1]
        parkingLot.slotNoForCarWithRegNo(regNo)
    else:
        print('Please enter a valid command!')

if len(sys.argv) > 1:
    filename = sys.argv[1]
    file = open(filename, 'r')
    for line in file:
        runCommand(line)
else:
    # Loop to accept user's command or file as command line input  
    while True:
        command = input('Enter command\n') #is this ok?
        if command == 'exit':
            break
        runCommand(command)