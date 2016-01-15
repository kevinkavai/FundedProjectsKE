# Test coordinates
# lat_long = "(1.73400000000, 38.38000000000)"


def get_coordinates(coordinates_string):
    if not coordinates_string or coordinates_string == '0' or coordinates_string == 0:
        coordinates_string = "(-0.0, 0.0)"  # How else?

    latlong_list = coordinates_string[1:-1].split(',')  # Remove brackets and put in list
    return [float(i) for i in latlong_list]  # Convert to floating point numbers

# Test function
# get_coordinates(lat_long)