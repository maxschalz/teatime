import argparse
from subprocess import run
from sys import platform
from time import sleep


def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-nt', '--notimer', help='Disable the timer',
                        action='store_true')
    parser.add_argument('-th','--temphot', help='Temperature of hot water',
                        action='store', default=100., type=float)
    parser.add_argument('-tc', '--tempcold', help='Temperature of cold water',
                        action='store', default=20., type=float)
    parser.add_argument('-vh', '--volumehot', help='Volume of hot water',
                        action='store', type=float)
    parser.add_argument('-tt', '--temptarget', help='Target temperature',
                        action='store', default=60., type=float)
    args = parser.parse_args()
    return args


def calculate_volume(v1, t0, t1, t2):
    """Calculate the volume of water that needs to be added.

    Parameters
    ----------
    v1 : float
        Volume of hot water
    t0 : float
        Target temperature
    t1 : float
        Temperature of hot water
    t2 : float
        Temperature of cold water
    """
    return v1 * (t1 - t0) / (t0 - t2)


def timer():
    """Set timer and play sound at the end of the timer."""
    print('Please enter how long the tea should steep.')
    minutes = float(input('Minutes: '))
    seconds = float(input('Seconds: '))
    sleep(minutes*60 + seconds)

    print('Your tea is ready!')
    if platform=='linux':
        run('aplay /usr/share/sounds/KDE-Sys-App-Positive.ogg;'.split())
        return
    elif platform=='darwin':
        run('afplay /System/Library/Sounds/Blow.aiff --volume 10;'.split())
        return

    msg = 'The timer function only works on Linux or Mac OS platforms.'
    raise RuntimeError(msg)


def main():
    """Set input temperatures and volumes and calculate the target volume."""
    args = args_parser()
    if args.volumehot == None:
        vh = float(input('Volume of hot water: '))
    else:
        vh = args.volumehot

    v2 = calculate_volume(vh, args.temptarget, args.temphot, args.tempcold)

    print(f'\nPlease add {v2:.2f} l of cold water to the hot water to obtain '
          f'{args.temptarget}°C hot water.')

    if not args.notimer:
        timer()
    print('Enjoy your tea!')


if __name__=='__main__':
    main()
