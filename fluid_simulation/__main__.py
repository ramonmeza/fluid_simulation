import argparse
import logging
import sys

from .game import Game


def main(window_width: int, window_height: int, fullscreen: bool) -> int:
    try:
        game = Game(window_width, window_height, fullscreen)
        game.run()
    except Exception as e:
        logging.critical("An error occurred: %s", str(e))
        return -1

    return 0


if __name__ == "__main__":
    logging.basicConfig()

    cli = argparse.ArgumentParser()
    cli.add_argument("--window-width", type=int, default=1920)
    cli.add_argument("--window-height", type=int, default=1080)
    cli.add_argument("--fullscreen", action='store_true', default=False)
    cli_args = cli.parse_args()

    logging.info("Command-line arguments: %s", cli_args)

    sys.exit(main(cli_args.window_width, cli_args.window_height, cli_args.fullscreen))
