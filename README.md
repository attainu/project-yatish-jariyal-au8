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

        park   White  
        # parked a car with registration number and color
        
        leave 1
        # car parked on slot 1 left

        status  
        # shows list of all parked cars with reg Nos and colors
        
        registration_numbers_for_cars_with_colour White  
        # shows all registration numbers with color white

        slot_numbers_for_cars_with_colour White  
        # shows all slot numbers where particular colored car is parked

        slot_number_for_registration_number KA-01-HH-3141  
        # shows slot number of car with given reg No
    </code>
</pre>