# Test coordinates
# lat_long = "(-4.43763300000, 39.51327200000)"


# Replace () with []
def replace_brackets(coordinates_string):
    if coordinates_string == 0:
        return None
    else:
        new_str = coordinates_string.replace('(', '[')
        final_str = new_str.replace(')', ']')
        return final_str

# Test function
#replace_brackets(lat_long)