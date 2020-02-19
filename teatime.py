import argparse
import os
import sys
from time import sleep

# Parse all of the arguments
def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--timer', help='Initialise a timer',
                        action='store_true')
    parser.add_argument('-th','--temphot', help='Temperature of hot water',
                        action='store', default=100., type=float)
    parser.add_argument('-tc', '--tempcold', help='Temperature of cold water',
                        action='store', default=20., type=float)
    parser.add_argument('-vh', '--volumehot', help='Volume of hot water',
                        action='store', type=float)
    parser.add_argument('-tt', '--temptarget', help='Temperate target',
                        action='store', default=60., type=float)
    args = parser.parse_args()
    return args

# Calculate the volume of water that needs to be added. It is assumed that the
# density of water is 1 kg/l.
def calculate_volume(v1, t0, t1, t2):
    return v1 * (t1 - t0) / (t0 - t2)

def timer():
    if sys.platform not in ('linux', 'darwin'):
        print('The timer function only works on Linux or Mac OS platforms.')
        return 1
    
    print('Please enter how long the tea should steep.')
    minutes = float(input('Minutes: '))
    seconds = float(input('Seconds: '))
    sleep(minutes*60 + seconds)
    
    print('Your tea is ready!')
    if sys.platform=='linux':
        os.system('aplay /usr/share/sounds/KDE-Sys-App-Positive.ogg;')
    elif sys.platform=='darwin':
        os.system('afplay /System/Library/Sounds/Blow.aiff --volume 10;')
    return 0

# Main function. Sets input temperatures and volumes and calculates the target
# volume.
def main():
    args = args_parser()
    if args.volumehot == None:
        vh = float(input('Volume of hot water:'))
    else:
        vh = args.volumehot

    v2 = calculate_volume(vh, args.temptarget, args.temphot, args.tempcold)

    print('\nPlease add {:.2f} l of cold water to the hot water.'.format(v2))
    
    if args.timer:
        timer()
    print('Enjoy your tea!')

    return 0

if __name__=='__main__':
    main()

