from console.screen import sc


class Cursor:

    @staticmethod
    def print_in_position(x, y, message):
        """Print message in specific position on screen"""
        with sc.location(x, y):
            print(message)
