import logging
from argparse import ArgumentParser
from time import sleep, time

import settings
import toggl_track


def program(interval=60, max_iterations=24 * 60, token=None):
    user = toggl_track.me(token=token)
    if not user:
        return
    username = user['fullname']
    print(f'Checking current timer for user {username}:')

    iteration = 0
    while True:
        timer = toggl_track.current_timer(token=token)
        if timer is None:
            print('Timer is not started!')
            return
        now = int(time())
        duration = timer['duration']  # negative unix timestamp
        diff = now + duration
        hours = diff // 3600
        diff -= hours * 3600
        hours = f'{hours}h ' if hours else ''
        minutes = diff // 60
        diff -= minutes * 60
        minutes = f'{minutes}m ' if minutes else ''
        seconds = f'{diff}s ' if diff else ''
        description = timer['description'] or ''
        if description:
            description = f' ({description})'
        print(f'Started: {hours}{minutes}{seconds}ago{description}')
        iteration += 1
        if iteration >= max_iterations:
            if max_iterations > 1:
                print('Maximum iterations reached. Exiting...')
            return
        try:
            sleep(interval)
        except KeyboardInterrupt:
            print('Enough is enough!')
            exit(1)


def main():
    logging.basicConfig(format='%(asctime)s %(filename)s: %(message)s')

    parser = ArgumentParser(
        description='Check current Toggl timer and wait for it to finish.',
    )
    parser.add_argument('-token', '--token', help='Specify custom Toggl API token')
    parser.add_argument('-c', '--continue', dest='continuous', action='store_true', help='Continuous start')
    parser.add_argument('-m', '--max-iterations', type=int, help='How many times to retry if timer is not finished',
                        default=0)
    parser.add_argument('-i', '--interval', type=int, help='How often to retry (sec)', default=60)
    parser.add_argument('-d', '--debug', action='store_true', help='Output debug information')

    args = parser.parse_args()
    token = args.token
    if not token:
        assert settings.TOGGL_TRACK_API_TOKEN is not None, 'Specify local_settings.TOGGL_TRACK_API_TOKEN'
        token = settings.TOGGL_TRACK_API_TOKEN
    assert args.interval >= 5, 'Interval should be more than 5 sec'
    if args.continuous and not args.max_iterations:
        args.max_iterations = 24 * 60
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    program(interval=args.interval, max_iterations=args.max_iterations, token=token)


if __name__ == '__main__':
    main()
