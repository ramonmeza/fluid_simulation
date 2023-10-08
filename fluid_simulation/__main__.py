import argparse
import datetime
import time
import logging
import sys

from .game import Game


def main(window_width: int, window_height: int, fullscreen: bool, debug: bool) -> int:
    try:
        Game.debug = debug
        Game.init(window_width, window_height, fullscreen)
        Game.run()
    except Exception as e:
        logging.critical("An error occurred: %s", str(e))
        return -1

    return 0


if __name__ == "__main__":
    unix_now = int(time.mktime(datetime.datetime.now().timetuple()))
    logging.basicConfig(
        filename=f"fluid_simulation-{unix_now}.log",
        encoding="utf-8",
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s: %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
    )

    cli = argparse.ArgumentParser()
    cli.add_argument("--window-width", type=int, default=1920)
    cli.add_argument("--window-height", type=int, default=1080)
    cli.add_argument("--fullscreen", action="store_true", default=False)
    cli.add_argument("--debug", action="store_true", default=False)
    cli_args = cli.parse_args()

    logging.info("Command-line arguments: %s", cli_args)

    sys.exit(
        main(
            cli_args.window_width,
            cli_args.window_height,
            cli_args.fullscreen,
            cli_args.debug,
        )
    )
