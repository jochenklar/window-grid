import argparse
import os

import gi

gi.require_version('Wnck', '3.0')
from gi.repository import Wnck  # noqa: E402


def main():
    columns = os.getenv('WINDOW_GRID_COLUMNS', 12)
    rows = os.getenv('WINDOW_GRID_ROWS', 6)

    parser = argparse.ArgumentParser()
    parser.add_argument('column', type=int, help='move to this column', choices=range(0, columns))
    parser.add_argument('row', type=int, help='move to this row', choices=range(0, rows))
    parser.add_argument('width', type=int, help='set his width', choices=range(1, columns + 1))
    parser.add_argument('height', type=int, help='set his height', choices=range(1, rows + 1))
    parser.add_argument('--padding', type=int, help='padding between windows in pixel',
                                     default=os.getenv('WINDOW_GRID_PADDING', 20))
    parser.add_argument('--margin-top', type=int, help='additional margin to the top of the screen in pixel',
                                        default=os.getenv('WINDOW_GRID_MARGIN_TOP', 30))

    args = parser.parse_args()

    screen = Wnck.Screen.get_default()
    screen.force_update()
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    window = screen.get_active_window()
    window.unmaximize()

    x, y, w, h = get_geometry(screen_width, screen_height, columns, rows, window,
                              args.column, args.row, args.width, args.height, args.padding, args.margin_top)

    resize_window(window, x, y, w, h)


def get_geometry(screen_width, screen_height, columns, rows, window,
                 column, row, width, height, padding, margin_top):
    left, top, screen_width, screen_height = get_workarea(screen_width, screen_height, margin_top)
    left_border, top_border = get_borders(window)

    x = left + screen_width * column // columns
    x -= left_border
    x += padding

    y = top + screen_height * row // rows
    y -= top_border
    y += padding

    w = screen_width * width // columns
    w -= 2 * padding

    h = screen_height * height // rows
    h -= 2 * padding

    return x, y, w, h


def get_workarea(screen_width, screen_height, margin_top):
    return 0, margin_top, screen_width, screen_height - margin_top


def get_borders(window):
    client_window_geometry = window.get_client_window_geometry()
    geometry = window.get_geometry()
    return (client_window_geometry.xp - geometry.xp, client_window_geometry.yp - geometry.yp)


def resize_window(window, x, y, width, height):
    gravity = Wnck.WindowGravity.CURRENT
    mask = Wnck.WindowMoveResizeMask.X | \
           Wnck.WindowMoveResizeMask.Y | \
           Wnck.WindowMoveResizeMask.WIDTH | \
           Wnck.WindowMoveResizeMask.HEIGHT
    window.set_geometry(gravity, mask, x, y, width, height)
