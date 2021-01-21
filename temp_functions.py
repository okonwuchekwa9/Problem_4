def fahr_to_celsius(temp_data):
    """converts Fahrenheit to Celsius"""
    return (temp_data - 32)/1.8

def temp_classifier(temp_celsius):
    """This is a temp classifier for grading temperature"""
    if temp_celsius < -2:
        return 0
    elif temp_celsius >= -2 and temp_celsius < 2:
        return 1
    elif temp_celsius >= 2 and temp_celsius <= 15:
        return 2
    else:
        return 3