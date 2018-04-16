#!/usr/bin/python

"""Test of learn mode."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(KeyPressAction(0, None, "KP_Insert"))
sequence.append(TypeAction("h"))
sequence.append(KeyReleaseAction(0, None, "KP_Insert"))

sequence.append(PauseAction(2000))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("F1"))
sequence.append(utils.AssertPresentationAction(
    "1. F1 for help",
    ["BRAILLE LINE:  'yelp application Orca Screen Reader frame'",
     "     VISIBLE:  'Orca Screen Reader frame', cursor=1",
     "BRAILLE LINE:  ' Orca's logo Orca Screen Reader h1'",
     "     VISIBLE:  'Orca's logo Orca Screen Reader h', cursor=1",
     "BRAILLE LINE:  'Finished loading Orca Screen Reader.'",
     "     VISIBLE:  'Finished loading Orca Screen Rea', cursor=0",
     "BRAILLE LINE:  ' Orca's logo Orca Screen Reader h1'",
     "     VISIBLE:  'Orca's logo Orca Screen Reader h', cursor=1",
     "SPEECH OUTPUT: 'F1 '",
     "SPEECH OUTPUT: 'Orca Screen Reader frame'",
     "SPEECH OUTPUT: ' \ufffc link Orca Screen Reade'",
     "SPEECH OUTPUT: 'heading level 1'",
     "SPEECH OUTPUT: 'Before You Begin",
     "'",
     "SPEECH OUTPUT: 'If you are not yet familiar with the navigation commands provided by your desktop environment, you are encouraged to read that documentation first.'",
     "SPEECH OUTPUT: 'Getting Started'",
     "SPEECH OUTPUT: 'heading level 2'",
     "SPEECH OUTPUT: 'Welcome to Orca",
     " link'",
     "SPEECH OUTPUT: 'Introducing the Orca screen reader",
     " link'",
     "SPEECH OUTPUT: 'The Orca Modifier",
     " link'",
     "SPEECH OUTPUT: 'A key that works like Shift, Ctrl, and Alt",
     " link'",
     "SPEECH OUTPUT: 'Configuration",
     " link'",
     "SPEECH OUTPUT: 'Setting up Orca",
     " link'",
     "SPEECH OUTPUT: '\"Learn\" Mode",
     " link'",
     "SPEECH OUTPUT: 'Discovering Orca's commands",
     " link'",
     "SPEECH OUTPUT: 'Keyboard Layout",
     " link'",
     "SPEECH OUTPUT: 'Selecting the Desktop or Laptop layout",
     " link'",
     "SPEECH OUTPUT: 'CapsLock in Laptop Layout",
     " link'",
     "SPEECH OUTPUT: 'Toggling it when it is the Orca Modifier",
     " link'",
     "SPEECH OUTPUT: 'Keybindings",
     " link'",
     "SPEECH OUTPUT: 'Binding, rebinding, and unbinding commands",
     " link'",
     "SPEECH OUTPUT: 'Profiles",
     " link'",
     "SPEECH OUTPUT: 'Maintaining multiple configurations'",
     "SPEECH OUTPUT: 'Reading Documents and Web Pages'",
     "SPEECH OUTPUT: 'heading level 2'",
     "SPEECH OUTPUT: 'Documents",
     " link'",
     "SPEECH OUTPUT: 'Reading content",
     " link'",
     "SPEECH OUTPUT: 'Text Attributes",
     " link'",
     "SPEECH OUTPUT: 'Examining text formatting",
     " link'",
     "SPEECH OUTPUT: 'Structural Navigation",
     " link'",
     "SPEECH OUTPUT: 'Moving by heading and other elements",
     " link'",
     "SPEECH OUTPUT: 'Tables",
     " link'",
     "SPEECH OUTPUT: 'Navigating and setting dynamic headers",
     " link'",
     "SPEECH OUTPUT: 'Filling out forms",
     " link'",
     "SPEECH OUTPUT: 'Accessing widgets embedded in documents",
     " link'",
     "SPEECH OUTPUT: 'Live Regions",
     " link'",
     "SPEECH OUTPUT: 'Interacting with dynamic web content'",
     "SPEECH OUTPUT: 'Reviewing and Interacting with Screen Contents'",
     "SPEECH OUTPUT: 'heading level 2'",
     "SPEECH OUTPUT: 'WhereAmI",
     " link'",
     "SPEECH OUTPUT: 'Learning about your location",
     " link'",
     "SPEECH OUTPUT: 'Flat Review",
     " link'",
     "SPEECH OUTPUT: 'Examining a window spatially",
     " link'",
     "SPEECH OUTPUT: 'Orca Find",
     " link'",
     "SPEECH OUTPUT: 'Searching a window for objects",
     " link'",
     "SPEECH OUTPUT: 'Mouse Review",
     " link'",
     "SPEECH OUTPUT: 'Using the pointer to examine the screen",
     " link'",
     "SPEECH OUTPUT: 'Notifications",
     " link'",
     "SPEECH OUTPUT: 'Reading previously-received messages",
     " link'",
     "SPEECH OUTPUT: 'Bookmarks",
     " link'",
     "SPEECH OUTPUT: 'Storing and retrieving objects'",
     "SPEECH OUTPUT: 'Quick Reference'",
     "SPEECH OUTPUT: 'heading level 2'",
     "SPEECH OUTPUT: 'Commands",
     " link'",
     "SPEECH OUTPUT: 'Preferences link'",
     "SPEECH OUTPUT: 'About'",
     "SPEECH OUTPUT: 'heading level 2'",
     "SPEECH OUTPUT: 'Finished loading Orca Screen Reader.'"]))

sequence.append(KeyComboAction("<Alt>F4"))
sequence.append(utils.AssertionSummaryAction())
sequence.start()