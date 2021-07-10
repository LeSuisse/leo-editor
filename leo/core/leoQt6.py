#@+leo-ver=5-thin
#@+node:ekr.20210407011013.1: * @file leoQt6.py
"""
Import wrapper for pyQt6.

For Qt6, plugins are responsible for loading all optional modules.

"""
# pylint: disable=unused-import,no-name-in-module,c-extension-no-member,import-error
#
# Required imports
from PyQt6 import QtCore
from PyQt6 import QtGui
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
assert QtGui and QtWidgets  # For pyflakes.
from PyQt6.QtCore import QUrl
from PyQt6.QtCore import pyqtSignal as Signal
from PyQt6 import uic
assert QUrl and Signal and uic  # For pyflakes.
#
# Standard abbreviations.
QtConst = Qt
qt_version = QtCore.QT_VERSION_STR
#
# Optional(?) modules.
try:
    printsupport = Qt.printsupport
except Exception:
    pass
#@-leo
