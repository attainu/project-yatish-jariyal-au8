Parking Lot is a Python Project for parking cars, keeping track of registration numbers, etc.

<h1>How to run this project</h1>
<h3>Input using command prompt</h3>
<pre>
    <code>
        python ParkingLot.py
    </code>
</pre>

<h3>Input using file</h3>
<pre>
    <code>
        python ParkingLot.py input.txt  
    </code>
</pre>

<h3>List of commands</h3>
<pre>
    <code>
        create_parking_lot 6 
        # created a parking lot of 6 slots
    </code>
    <code>
        park KA-01-HH-1234 White  
        # parked a car with registration number and color
    </code>
    <code>
        leave 1
        # car parked on slot 1 left
    </code>
    <code>
        status  
        # shows list of all parked cars with reg Nos and colors
    </code>
    <code>    
        registration_numbers_for_cars_with_colour White  
        # shows all registration numbers with color white
    </code>
    <code>
        slot_numbers_for_cars_with_colour White  
        # shows all slot numbers where particular colored car is parked
    </code>
    <code>
        slot_number_for_registration_number KA-01-HH-3141  
        # shows slot number of car with given reg No
    </code>
    <code>   
        exit
    </code>
</pre>

<h3>Extra Features</h3>
<pre>
    <code>
        visualize_parking_lot
        # Shows total no of slots, next available parking slot and visualization of parking lot
    </code>
    <code>
        tabular_status
        # Shows status of all slots in a tabular format
    </code>
</pre>