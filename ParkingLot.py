from LinkedList import Car, Node, LinkedList
import sys

parkingLot = None

#Commands for testing

def runCommand(command):
    global parkingLot
    splitted = command.split(" ")
    if splitted[0] == 'create_parking_lot':
        size = int(splitted[1])
        parkingLot = LinkedList(size) #Creating Parking Lot
    elif splitted[0] == 'tabular_status':
        parkingLot.tabularParkingStatus() #Status of the parking lot in tabular format
    elif splitted[0] == 'park':
        regNo = splitted[1]
        color = splitted[2]
        parkingLot.addCar(regNo, color) #Parking Car in Parking Lot
    elif splitted[0] == 'leave':
        slotNo = int(splitted[1])
        parkingLot.removeCar(slotNo) #Leaving Car from Parking Lot
    elif splitted[0] == 'status':
        parkingLot.parkingStatus() #Status of the parking lot
    elif splitted[0] == 'registration_numbers_for_cars_with_colour':
        color = splitted[1]
        parkingLot.regNoForCarWithColor(color) #Registration numbers of all the cars for given color
    elif splitted[0] == 'slot_numbers_for_cars_with_colour':
        color = splitted[1]
        parkingLot.slotNoForCarWithColor(color) #Slot numbers of all the cars for given color
    elif splitted[0] == 'slot_number_for_registration_number':
        regNo = splitted[1]
        parkingLot.slotNoForCarWithRegNo(regNo) #Slot numbers of all the cars for given registration number
    elif splitted[0] == 'visualize_parking_lot':
        parkingLot.visualizeParkingLot() #Visualizing the parking lot (extra feature)
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
        command = input('Enter command\n') 
        if command == 'exit':
            break
        runCommand(command)