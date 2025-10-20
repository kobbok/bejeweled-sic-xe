# Bejeweled

The classic game of Bejeweled (aka match 3 gems) written in SIC/XE.
Match 3 or more gems to "destroy" them. Destroyed gems are removed from the board, the gems above the destroyed gems "fall" down and new gems get generated to fill the now empty space at the top of columns containing destroyed gems.
Matching 5 or more gems will cause a "hyper cube" to be created. This hyper cube can be matched with any gem color, to destroy all gems of that color currently on the board. Matching two hyper cubes will ||clear the entire board||.

## Setup
- The `sictools.jar` is the recommended tool to use for running the game.
- The frequency must be set to at least `100000` for acceptable performance.
- The graphical screen must be at `0A000` with a width and height of `128`.
- The keyboard must be at `0F000` (moved since the graphical screen overlaps it).

## Controls
- `a` moves the selection left
- `w` moves the selection up
- `d` moves the selection right
- `s` moves the selection down
- `space` selects the gem or swaps gems if a gem is already selected
- `escape` deselects the currently selected gem

## Sprites
The game uses sprites for the gems. The sprites are stored in a sprite map (`sprites.bmp`) which is the converted with the `extract.py` script to SIC/XE `BYTE` instructions.

Sprite drawing is also optimized by drawing up to 6 pixels at a time by abusing the `F` register (with the caveat that some pixel colors cannot be used as their byte representation changes when loaded into the `F` register).

## TODO
- Moves that dont cause a match should be prevented
- Flash gems that are destroyed from white to black
