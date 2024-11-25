# Sublime Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to vscode
SUBLIME = 'subl'

# what name do you want to see in the context menu?
SUBLIMENAME = 'Sublime'

# always create new window?
NEWWINDOW = False


class SublimeExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_sublime(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

            # If one of the files we are trying to open is a folder
            # create a new instance of vscode
            if os.path.isdir(filepath) and os.path.exists(filepath):
                args = '--new-window '

        if NEWWINDOW:
            args = '--new-window '

        call(SUBLIME + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='SublimeOpen',
            label='Open in ' + SUBLIMENAME,
            tip='Opens the selected files with Sublime'
        )
        item.connect('activate', self.launch_sublime, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='SublimeOpenBackground',
            label='Open in ' + SUBLIMENAME,
            tip='Opens the current directory in Sublime'
        )
        item.connect('activate', self.launch_sublime, [file_])

        return [item]
