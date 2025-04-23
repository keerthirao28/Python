battery_percentage = int(input("Enter battery percentage: "))

if battery_percentage >= 80:
    print("Battery level is high. No need for battery saver.")
elif battery_percentage >= 30:
    print("Battery level is moderate. Consider enabling battery saver.")
else:
    print("Battery is low! Turning on battery saver mode.")
