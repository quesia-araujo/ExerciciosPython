transport_speed = {'airplane': 600, 'car': 100, 'bus': 80}

distance = float(input('Enter the distance of a trip: '))


def func_time_of_travel(distance: float, speed: int) -> float:
    return distance/speed


for transport, speed in transport_speed.items():
    travel_time = func_time_of_travel(distance, speed)
    print(f'{transport} arrived in {travel_time:.2f} hours')
