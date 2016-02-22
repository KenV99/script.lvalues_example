#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#     Copyright (C) 2015 KenV99
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import os
import sys
import xbmcaddon
import xbmcgui

def startdebugger():
    debugegg = 'C:\\Program Files (x86)\\JetBrains\\PyCharm 5.0.2\\debug-eggs\\pycharm-debug.egg'
    if os.path.exists(debugegg):
        sys.path.append(debugegg)
        try:
            import pydevd
        except ImportError:
            pass
        else:
            pydevd.settrace('localhost', port=51234, stdoutToServer=True, stderrToServer=True, suspend=False)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'lselector':
            settingid = sys.argv[2]
            # startdebugger()
            choicesl = [32003, 32004, 32005]
            choices = []
            for choice in choicesl:
                choices.append(xbmcaddon.Addon().getLocalizedString(choice))
            result = xbmcgui.Dialog().select('Choose', choices)
            xbmcaddon.Addon().setSetting('%sv' % settingid, choices[result])
            xbmcaddon.Addon().setSetting(settingid, str(choicesl[result]))

