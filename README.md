window-grid
===========

The script allows windows to be moved and resized using GTK3, a bit like [Rectangle](https://rectangleapp.com/) or [Lasso](https://www.thelasso.app/) on the Mac.

By default, it uses a grid of 12 columns and 6 rows. The currently active window can be placed using, e.g.:

```bash
window-grid 3 0 6 6
```

which would place the current window in column `3` (25% from the left side of the screen) and row `0` (top), and sets its height to `6` (full height) and it width to `6` (half of the screen).

It works nicely with [xbindkeys](https://wiki.archlinux.org/title/Xbindkeys).


Setup
-----

The script can be installed for the current user in `~/.local`:

```
# directly from GitHub
pip install git+https://github.com/jochenklar/window-grid

# from the cloned repo
pip install .
```

When used in a virtual env, the `--system-site-packages` needs to be used to be able to access the systems GTK python bindings:

```
python3 -m venv env --system-site-packages
```


Usage
-----

The script uses

```
usage: window-grid [-h] [--padding PADDING] [--margin-top MARGIN_TOP]
                   {0,1,2,3,4,5} {0,1,2,3,4,5,6,7,8,9,10,11} {1,2,3,4,5,6,7,8,9,10,11} {1,2,3,4,5}

positional arguments:
  {0,1,2,3,4,5}         move to this row
  {0,1,2,3,4,5,6,7,8,9,10,11}
                        move to this column
  {1,2,3,4,5,6,7,8,9,10,11}
                        set his width
  {1,2,3,4,5}           set his height

optional arguments:
  -h, --help            show this help message and exit
  --padding PADDING     padding between windows in pixel
  --margin-top MARGIN_TOP
                        additional margin to the top of the screen in pixel
```

The following environment variables can be used to set default values:

```txt
WINDOW_GRID_COLUMNS=12     # the number of columns of the used grid
WINDOW_GRID_ROWS=6         # the number of rows of the used grid
WINDOW_GRID_PADDING=20     # the padding between windows in pixel
WINDOW_GRID_MARGIN_TOP=30  # an additional margin to the top of the screen in pixel
```


xbindkeys
---------

The following config can be used in `.xbindkeysrc` to use `window-grid` with keyboard shordcuts.

```plain
"window-grid 0 4 3 2"
   control+shift+KP_End
"window-grid 3 4 6 2"
   control+shift+KP_Down
"window-grid 9 4 3 2"
   control+shift+KP_Next
"window-grid 0 2 3 2"
   control+shift+KP_Left
"window-grid 3 2 6 2"
   control+shift+KP_Begin
"window-grid 9 2 3 2"
   control+shift+KP_Right
"window-grid 0 0 3 2"
   control+shift+KP_Home
"window-grid 3 0 6 2"
   control+shift+KP_Up
"window-grid 9 0 3 2"
   control+shift+KP_Prior
"window-grid 0 0 12 4"
   control+shift+KP_Divide

"window-grid 3 4 3 2"
   control+shift+alt+KP_End
"window-grid 3 2 6 4"
   control+shift+alt+KP_Down
"window-grid 6 4 3 2"
   control+shift+alt+KP_Next
"window-grid 0 0 3 6"
   control+shift+alt+KP_Left
"window-grid 3 0 6 6"
   control+shift+alt+KP_Begin
"window-grid 9 0 3 6"
   control+shift+alt+KP_Right
"window-grid 0 0 3 4"
   control+shift+alt+KP_Home
"window-grid 3 0 6 4"
   control+shift+alt+KP_Up
"window-grid 9 0 3 4"
   control+shift+alt+KP_Prior
"window-grid 0 0 12 6"
   control+shift+alt+KP_Divide

"window-grid 0 3 4 3"
   control+shift+1
"window-grid 4 3 4 3"
   control+shift+2
"window-grid 8 3 4 3"
   control+shift+3
"window-grid 0 0 4 3"
   control+shift+4
"window-grid 4 0 4 3"
   control+shift+5
"window-grid 8 0 4 3"
   control+shift+6
```

After changing the config ,`xbindkeys` need to be restarted:

```
killall xbindkeys
```

For debugging, `xbindkeys -n` can be run in a seperate terminal.


Acknowledgement
---------------

The script was adopted from https://wiki.xfce.org/windowgrid, which does not seem to be online anymore.
