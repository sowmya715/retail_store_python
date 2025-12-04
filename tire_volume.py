import math

"""
Problem Statement:
Write a Python program that calculates the approximate volume of a tire based
on its width, aspect ratio, and wheel diameter.

Requirements:
1. Ask the user to enter:
   - The width of the tire in millimeters (e.g., 205)
   - The aspect ratio of the tire (e.g., 60)
   - The diameter of the wheel in inches (e.g., 15)
2. Validate that all three values are greater than zero.
   - If a value is not greater than zero, ask the user to re-enter it.
3. Use the following formula to approximate the volume of the tire:

       V = (π * w² * a * (w * a + 2540 * d)) / 10,000,000,000

   where:
       V = volume in liters
       w = width in millimeters
       a = aspect ratio
       d = diameter in inches

4. Display the final volume rounded to two decimal places in liters.
"""

def readValues():
    """Read and validate tire width, aspect ratio, and diameter."""
    input_values = {"width": 0, "aspectRatio": 0, "diameter": 0}

    width = int(input("Enter the width of the tire in mm (ex 205): "))
    aspectRatio = int(input("Enter the aspect ratio of the tire (ex 60): "))
    diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

    while True:
        if width > 0:
            input_values["width"] = width
        else:
            print("Width must be greater than zero. Please try again.")
            width = int(input("Enter the width of the tire in mm (ex 205): "))
            continue

        if aspectRatio > 0:
            input_values["aspectRatio"] = aspectRatio
        else:
            print("Aspect ratio must be greater than zero. Please try again.")
            aspectRatio = int(input("Enter the aspect ratio of the tire (ex 60): "))
            continue

        if diameter > 0:
            input_values["diameter"] = diameter
        else:
            print("Diameter must be greater than zero. Please try again.")
            diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
            continue

        return input_values


def calculateTireVolume(width, aspect_ratio, diameter):
    """Calculate tire volume in liters using the given formula."""
    return (((math.pi * (width ** 2)) * aspect_ratio) *
            ((width * aspect_ratio) + (2540 * diameter))) / 10000000000


# Main logic
values = readValues()
calculated_value = calculateTireVolume(
    values.get("width"),
    values.get("aspectRatio"),
    values.get("diameter")
)

calculated_value = round(calculated_value, 2)
print(f"The approximate volume is {calculated_value} liters")
