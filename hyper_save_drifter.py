#!/usr/bin/python
import argparse
import os
import base64
import json
import platform
from string import strip

#I like having the directory this file exists in as a variable
dir_path = os.path.dirname(os.path.abspath(__file__))

#Allow user to change the name of their save.
player_name_change = None


#Save Folder Locations
linux_save_location = os.path.expanduser("~/.config/HyperLightDrifter")
mac_save_location = os.path.expanduser("~/Library/Application Support/com.HeartMachine.HyperLightDrifter")
windows_save_location = "%s\HyperLightDrifter" % os.getenv("LOCALAPPDATA")


#Save File Name Formats
linux_save_format = "hyperlight_recordofthedrifter_%d.sav"
mac_save_format = "hyperlight_recordofthedrifter_%d.sav"
windows_save_format = "HyperLight_RecordOfTheDrifter_%d.sav"


def decode_save(file_path):
    """
        Opens Save file, splits into header and content.
        Returns the decoded and raw versions of the header and content.
    """
    with open(file_path, 'r') as save_to_move:
        header = save_to_move.read(80)
        contents = save_to_move.read()
        decoded_header = base64.b64decode(header)
        decoded_contents = base64.b64decode(contents)
        decoded_contents = decoded_contents.rstrip('\0') #There's a NUL char for padding
        return decoded_header, decoded_contents, header, contents


def create_frankensave(save_to_move, temp_save_path):
    """
        Grabs the header for this machine from temp_save_path and
        grafts it onto the contents of the original save_to_move (from old machine).

        Also swaps out the name if requested.
    """
    if os.path.isfile(save_to_move):
        if os.path.isfile(temp_save_path):
            old_header_string, good_contents_string, good_header_raw, good_contents_raw = decode_save(save_to_move)

            temp_header_string, temp_contents_string, temp_header_raw, temp_contents_raw = decode_save(temp_save_path)

            #Just in case someone wants to change their name.
            if( player_name_change is not "" and player_name_change is not None):

                #get it as a dict by loading the json
                json_save_data = json.loads(good_contents_string)

                #modify the gameName to the new name we want
                json_save_data["gameName"] = player_name_change.upper()
                #save it back as a string
                string_save_data = json.dumps(json_save_data)
                print("Changing name to %s" % player_name_change.upper())

                #reencode the save data
                good_contents_raw = base64.b64encode(string_save_data)

            frankensave = "".join([temp_header_raw, good_contents_raw])

            return frankensave
        else:
            print("Error: %s is not file" % temp_save_path)

    else:
        print("Error: %s is not file" % save_to_move)

def format_save_location(save_num=0):
    """
        create the path string for the new save file
    """

    if 0 <= save_num <= 3:
        OS_NAME = platform.system()
        if OS_NAME == "Linux":
            print("I'm a Linux machine!\n")
            save_name = linux_save_format % save_num
            save_path = os.path.join(linux_save_location, save_name)

        elif (OS_NAME == "Windows"):
            print("I'm a PC.\n")
            save_name = windows_save_format % save_num
            save_path = os.path.join(windows_save_location, save_name)
            pass

        elif (OS_NAME == "osx"):
            print("I'm a Mac!\n")
            save_name = mac_save_format % save_num
            save_path = os.path.join(mac_save_location, save_name)
            pass
        else:
            print("I have no OS?\n")
            save_path = None

        return save_path
    else:
        print("Error: Only 4 save slots, you tried to pick one out of that range.")
        return None


def migrate_save(old_save_path,temp_save_path,save_num=3,new_file_name=None):
    global player_name_change
    player_name_change = new_file_name

    #Grab the new save information
    new_save_data = create_frankensave(old_save_path, temp_save_path)

    #Figure out which file we want
    save_path = format_save_location(save_num)

    #Tell people what's happening
    if save_path is not None:

        def write_save_file():
            print("Creating save file at %s" % save_path)
            with open(save_path, "w") as new_file:
                new_file.write(new_save_data)
                print("Save created.")

        if os.path.isfile(save_path):
            print("Save file %s already exists!" % save_path)
            save_anyways = raw_input("Please type 'OVERWRITE' if you wish to save anyways: ")
            if save_anyways == "OVERWRITE":
                print("Confirmation accepted; Overwriting old save file.")
                write_save_file()
            else:
                print("Cancelling to avoid data loss tears :)")
                return
        else:
            write_save_file()
    else:
        print("Error, save path not created")

def commandline_main():

    parser = argparse.ArgumentParser()
    parser.add_argument('save_to_move', help='')
    parser.add_argument('temp_save', help='')
    parser.add_argument('--save-num', nargs=1, type=int)
    parser.add_argument("--change-name", nargs=1, type=str)
    args = parser.parse_args()

    #This is the old save that we want to put on this machine.
    # save_to_move = os.path.join(dir_path, "my_old_save_file.sav") #relative path
    save_to_move = args.save_to_move

    #this is the new save file that has the header we want
    # temp_save_path = os.path.join(dir_path, "no_progress_save.sav")#relative path
    temp_save_path = args.temp_save


    #save slot number. The count starts at 0 so if you want file 4 to be written over,
    #make this number 3
    if args.save_num :
        save_slot_number = args.save_num[0]
    else:
        save_slot_number = 3

    if save_slot_number > 3:
        print "Error! save-num must be between 0 and 3 (inclusive)"
        return

    #This says whether or not you want to change your name
    if args.change_name:
        player_name_change = args.change_name[0]

    migrate_save(save_to_move, temp_save_path, save_slot_number, player_name_change)

if __name__ == "__main__":
    commandline_main()
