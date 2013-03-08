from reaper_python import *

actwin = RPR_MIDIEditor_GetActive()
unselect = 40214
insnum = [40157, 40158, 40159, 40160, 40161, 40162, 40163, 40164, 40165, 40166, 40167, 40168, 40169, 40170, 40171, 40172, 40173, 40174, 40175, 40176]
moveright = 40048

def noteminus7():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[0])  # insert note at -7
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteminus6():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[1])  # insert note at -6
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteminus5():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[2])  # insert note at -5
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteminus4():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[3])  # insert note at -4
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteminus3():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[4])  # insert note at -3
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteminus2():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[5])  # insert note at -2
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid

    
def noteminus1():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[6])  # insert note at -1
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def notemiddle():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[7])  # insert note at current note
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus1():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[8])  # insert note at +1
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus2():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[9])  # insert note at +2
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus3():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[10])  # insert note at +3
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus4():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[11])  # insert note at +4
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus5():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[12])  # insert note at +5
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus6():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[13])  # insert note at +6
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus7():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[14])  # insert note at +7
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus8():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[15])  # insert note at +8
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus9():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[16])  # insert note at +9
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus10():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[17])  # insert note at +10
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus11():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[18])  # insert note at +11
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid


def noteplus12():
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[19])  # insert note at +12
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid