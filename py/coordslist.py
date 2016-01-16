# Test coordinates
# lat_long = "(1.73400000000, 38.38000000000)"


def get_coordinates(coordinates_string):
    if not coordinates_string or coordinates_string == '0' or coordinates_string == 0:
        coordinates_string = "(-0.0, 0.0)"  # How else not to include these missing coordinates?

    latlong_list = coordinates_string[1:-1].split(',')  # Remove brackets and put lat and long in list
    latlong_list.reverse()  # reverse into format [long, lat]
    return [float(i) for i in latlong_list]  # Convert to floating point numbers

# Test function
# get_coordinates(lat_long)
