from screeninfo import get_monitors

monitor_details = get_monitors()

width = monitor_details[0].width
height = monitor_details[0].height

print(f"Monitor Width {width} & Height {height}")
