from __future__ import print_function

import mbuild as mb
from mbuild.components.solvents.water import Water
from mbuild.examples.ethane.ethane import Ethane


def main():
    """Solvate an ethane molecule in a Box of water. """

    # Create ethane and give it a box.
    ethane = Ethane()
    host_box = mb.Box(mins=[-.9, -.9, -.9], maxs=[1.9, 1.9, 1.9])
    print("Host (ethane) box: {}".format(host_box))

    # Create a water box.
    water = Water()
    guest_box = water.boundingbox()
    print("Guest (water) box: {}".format(guest_box))

    # Solvate ethane with water box.
    mb.solvate(ethane, water, host_box, guest_box)

if __name__ == "__main__":
    main()
