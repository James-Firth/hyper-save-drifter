


    .         /\
            /    \
          /        \
      Hyper Save Drifter
          \        /
            \    /
              \/

:hand: **Stop! Back up your save files before use.**
*Note:* This program has only been tested moving from Windows to Linux so far.
More testing will be done.

# Installation

* Currently no setup required! Just run `hyper_save_drifter.py`
    * If you are not familiar with python, please install python and then run the command (via commandline) `python hyper_save_drifter.py` from the folder you copied this to.

# Usage

1. Copy your old save file from your other computer to your new computer
    * [Save Game Locations (Depends on OS)](http://pcgamingwiki.com/wiki/Hyper_Light_Drifter#Save_game_data_location)
1. Create a new save file on your new computer
    1. Start a new game and watch (or skip) the initial cutscene
    1. The game should now auto-save
    1. Once it has saved, exit the game.
1. Find the save file you just created
    * [Save Game Locations (Depends on OS)](http://pcgamingwiki.com/wiki/Hyper_Light_Drifter#Save_game_data_location)
1. Run `python hyper_save_drifter.py /path/to/my_old.sav /path/to/temp.sav [--save-num save_slot_number] [--change-name my_new_filename]`
    * Replace the paths with the path to your old save file and your temp save (created in Step 2)
      * eg: `C:/Users/James/Download/from_old_pc.sav` or `/home/James/Downloads/from_old_pc.sav`
    * `--save-num` is optional if you want to set the save slot number to something (default is 4th slot)
      * NOTE: The saves are zero-indexed. Therefore, to save in slot 1 set `--save-num 0` to save in slot 4 set `--save-num 3`
    * `--change-name` is optional and changes the name your your save file.

# Plans/To-Do

* GUI interface for people who don't like CLIs
* More checks and confirmations to ensure everyone is happy with the result.
* Back-up files before doing anything.
* Test more OS versions to be safe.

# License

 Back up your save files before you use this! Despite testing, things can go wrong
 and I wouldn't want anyone's files being deleted. I am not responsible if your save file is lost, corrupted or otherwise damaged. Again **BACK UP YOU SAVE FILES**

    The MIT License (MIT)

    Copyright (c) 2016 James Firth

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
