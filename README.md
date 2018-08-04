# Bird Coding Challenge

##Intro
 
The following is the solution to the Bird Coding Challenge. 

## Tech

Code was written in Python 3. I took advantage of the built-in modules of unittest, math (for square root), csv and argparse.
Used git for version control

##Running Instructions

Run <em>python3 src/main.py [path-to-filename]</em>

## Notes
<ol>
<li>Ride Distance is defined as the cartesian distance between the starting point of the ride and the end point. If someone makes a round trip in the ride, the distance will be 0.</li>
<li>For the user_store, I should have made it a singleton but it wasn't worth the effort.</li>
<li>For question 4, regarding user who "paid the most", I defined this in terms of the total rides the user made as opposed to which user paid the most for an individual ride.</li>
<li>For question 5, I only looked at time between rides. If a Bird had a long time between drop-off and its first ride, that time was ignored.</li>
<li>For question 6, I took the total distance of the rides and divided by the total time. Rides with no distance but time spent were counted in the time total.</li>
</ol>
