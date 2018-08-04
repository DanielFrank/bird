import argparse
from csv import reader
from models.bird import Bird
from store.user_store import UserStore

user_store = UserStore()
bird_dict = dict()
ride_list = list()

DROP = "DROP"
START_RIDE = "START_RIDE"
END_RIDE =  "END_RIDE"
TIME_COLUMN = 0
BIRD_COLUMN = 1
EVENT_COLUMN = 2
X_COLUMN = 3
Y_COLUMN = 4
USER_COLUMN = 5

def process_event(event_line):
    event = event_line[EVENT_COLUMN]
    {
        DROP: process_drop_off,
        START_RIDE: process_start_ride,
        END_RIDE: process_end_ride
    }[event](event_line)
    
def process_drop_off(drop_off):
    bird = Bird(drop_off[BIRD_COLUMN], make_position_tuple(drop_off))
    bird_dict[drop_off[BIRD_COLUMN]] = bird

def process_start_ride(start_ride):
    bird = get_bird(start_ride)
    user = get_user(start_ride)
    ride = bird.start_ride(user.id, make_position_tuple(start_ride), get_time(start_ride))
    ride_list.append(ride)

def process_end_ride(end_ride):
    bird = get_bird(end_ride)
    user = get_user(end_ride)
    ride = bird.end_ride(make_position_tuple(end_ride), get_time(end_ride))
    user.add_completed_ride(ride)    

def get_bird(event_line):
    return bird_dict[event_line[BIRD_COLUMN]] 

def get_user(event_line):
    user_id = int(event_line[USER_COLUMN])
    return user_store.get_user(user_id)

def get_time(event_line):
    return int(event_line[TIME_COLUMN])

def make_position_tuple(event_line):
    return tuple([float(event_line[X_COLUMN]), float(event_line[Y_COLUMN])])

def answer_questions():
    farthest_bird_from_drop, longest_total_distance_bird, longest_wait_bird = answer_bird_questions()
    most_spent_user = get_spent_most_user()
    average_speed = get_average_speed()
    print("Question 1: There were {:d} Birds dropped off".format(len(bird_dict.values())))
    print("Question 2: Bird {} is farthest way ending up {:.4f} distance from drop off point"
          .format(farthest_bird_from_drop.id, farthest_bird_from_drop.get_distance_from_drop_position()))
    print("Question 3: Bird {} traveled the farthest total distance of {:.4f} "
          .format(longest_total_distance_bird.id, longest_total_distance_bird.get_total_distance()))
    print("Question 4: User {:d} spent the most by spending ${:.2f} for {:d} rides"
          .format(most_spent_user.id, most_spent_user.get_total_spent(), most_spent_user.get_num_rides()))
    print("Question 5: Bird {} waited the longest between rides for {:d} seconds"
          .format(longest_wait_bird.id, longest_wait_bird.get_longest_wait()))
    print("Question 6: The average speed of all the rides is  {:.4f} units/second"
          .format(average_speed))

    
def answer_bird_questions():
    farthest_distance_from_drop, longest_total_distance, longest_wait = 0,0,0
    farthest_bird_from_drop, longest_total_distance_bird, longest_wait_bird = None,None,None
    for bird in bird_dict.values():
        if (bird.get_distance_from_drop_position() > farthest_distance_from_drop):
            farthest_bird_from_drop = bird
            farthest_distance_from_drop = bird.get_distance_from_drop_position()
        if (bird.get_total_distance() > longest_total_distance):
            longest_total_distance_bird = bird
            longest_total_distance = bird.get_total_distance()
        if (bird.get_longest_wait() > longest_wait):
            longest_wait_bird = bird
            longest_wait = bird.get_longest_wait()
    return (farthest_bird_from_drop, longest_total_distance_bird, longest_wait_bird)

def get_spent_most_user():
    highest_total_spent = 0
    most_spent_user = None
    for user in user_store.get_user_list():
        if (user.get_total_spent() > highest_total_spent):
            most_spent_user = user
            highest_total_spent = user.get_total_spent()
    return most_spent_user    

def get_average_speed():
    total_distance = 0
    total_time = 0
    for ride in ride_list:
        total_distance = ride.get_distance()
        total_time = ride.get_time()
    return total_distance/total_time
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parses a CSV event file and answers questions about them")
    parser.add_argument("file", help="path of the CSV event file")
    args = parser.parse_args()
    file_path = args.file
    events = list()
    with open(file_path, 'r') as fp:
        event_reader = reader(fp)
        events = list(event_reader)
    for event in events:
        process_event(event)
    answer_questions()
