#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 29, 2021
# Calculates the volume of a cylinder

import math


def volume_cylinder(radius, height):
    volume = (radius * radius) * height * math.pi
    return volume


def main():
    user_input1 = (input("Enter radius of the cylinder (mm): "))
    user_input2 = (input("Enter height of cylinder (mm): "))
    try:
        user_radius = int(user_input1)
        try:
            user_height = int(user_input2)
            volume_cylinder(user_radius, user_height)
            final_volume = volume_cylinder(user_radius, user_height)
            print("{:.2f} mm² is the volume of your cylinder".format
                  (final_volume))
        except Exception:
            print("{} is not a dimension".format(user_input2))
    except Exception:
        print("{} is not a dimension".format(user_input1))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
