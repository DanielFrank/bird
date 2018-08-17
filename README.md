# Bird Coding Challenge
  
## Bird Engineering: Coding Exercise

### Bird Events:
The input to your program is a text file containing a list of Bird events from a completed simulation. Bird events are events which happen in our system, e.g. when a ride is started or ended. A drop event is when a Bird is initially put into the simulation. The format of the events is

| Column        | Type           | Description  |
| ------------- | ------------- | ----- |
| timestamp     | Integer | The time in seconds since the start of the simulation |
| bird_id | String | The id of the associated Bird vehicle, e.g. JK5T |
| event_type | String |The type of the event is one of START_RIDE, END_RIDE, DROP |
| x | Double | The x coordinate in a cartesian coordinate system of the location of where the event happened in the simulation |
| y | Double | The y coordinate in a cartesian coordinate system of the location of where the event happened in the simulation |
| user_id | Integer | The id of the associated user or NULL if the event does not have an associated user |

Each column is separated by a comma (,) and each line represents a single event. The list is ordered by time starting with the first event that happened.

### Goal:
The goal of the program is to parse a list of such events and print out to the command line (stdout) answers to the following questions. A list of sample events of one completed simulation is sent as a separate file, so you can test your code with them. Assume each question has exactly one valid answer, each bird has been dropped off as its first event and all rides have a start and end event.

### Questions:
<ol>
<li>What is the total number of Bird vehicles dropped off in the simulation?</li>
<li>Which Bird ends up the farthest away from its drop location? What is the distance?</li>
<li>Which Bird has traveled the longest distance in total on all of its rides? How far is it?</li>
###Bonus:
<li>Which user has paid the most? How much is it? The cost of a ride is $1 to start and $0.15 for every minute. If the ride is lasts less than 1 minute, the cost is $0.
For example:
- Ride time 98 seconds = $1.30
- Ride time 153 seconds = $1.45
- Ride time 52 seconds = $0.00</li>
<li>Which Bird has the longest wait time between two rides? How many seconds is it?</li>
<li>What is the average speed travelled across all rides?</li>

## Intro
 
The following is the solution to the Bird Coding Challenge. 

## Tech

Code was written in Python 3. I took advantage of the built-in modules of unittest, math (for square root), csv and argparse.
Used git for version control

## Running Instructions

Run <em>python3 src/main.py [path-to-filename]</em>

## Notes
<ol>
<li>Ride Distance is defined as the cartesian distance between the starting point of the ride and the end point. If someone makes a round trip in the ride, the distance will be 0.</li>
<li>For the user_store, I should have made it a singleton but it wasn't worth the effort.</li>
<li>I did no error checking for things the instructions said I could assume (Bird is dropped off as its first event and rides have starts and stops).
<li>For question 4, regarding user who "paid the most", I defined this in terms of the total rides the user made as opposed to which user paid the most for an individual ride.</li>
<li>For question 5, I only looked at time between rides. If a Bird had a long time between drop-off and its first ride, that time was ignored.</li>
<li>For question 6, I took the total distance of the rides and divided by the total time. Rides with no distance but time spent were counted in the time total.</li>
</ol>
