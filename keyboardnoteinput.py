from reaper_python import *

actwin = RPR_MIDIEditor_GetActive()
unselect = 40214
insnum = [40157, 40158, 40159, 40160, 40161, 40162, 40163, 40164, 40165, 40166, 40167, 40168, 40169, 40170, 40171, 40172, 40173, 40174, 40175, 40176]
moveright = 40048


def note(n):
    RPR_MIDIEditor_OnCommand(actwin, unselect)  # unselect all
    RPR_MIDIEditor_OnCommand(actwin, insnum[n])  # insert note at note n
    RPR_MIDIEditor_OnCommand(actwin, moveright)  # move edit cursor right by grid

