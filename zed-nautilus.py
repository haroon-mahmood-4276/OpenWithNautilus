# Zed Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to vscode
ZED = 'zed'

# what name do you want to see in the context menu?
ZEDNAME = 'Zed'

class ZedExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_zed(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

        call(ZED + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='ZedOpen',
            label='Open in ' + ZEDNAME,
            tip='Opens the selected files with Zed'
        )
        item.connect('activate', self.launch_zed, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='ZedOpenBackground',
            label='Open in ' + ZEDNAME,
            tip='Opens the current directory in Zed'
        )
        item.connect('activate', self.launch_zed, [file_])

        return [item]
