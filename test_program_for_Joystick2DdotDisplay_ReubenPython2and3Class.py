# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision M, 04/28/2025

Verified working on: Python 2.7, 3.11/12 for Windows 10/11 64-bit, Ubuntu 20.04, and Raspberry Pi 4/5.
'''

__author__ = 'reuben.brewer'

#################################################
from MyPrint_ReubenPython2and3Class import *
from Joystick2DdotDisplay_ReubenPython2and3Class import *
#################################################

#################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import keyboard
#################################################

#################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
#################################################

#################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#################################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global Joystick2DdotDisplay_ReubenPython2and3ClassObject
    global Joystick2DdotDisplay_OPEN_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if Joystick2DdotDisplay_OPEN_FLAG == 1:
                Joystick2DdotDisplay_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(OptionalArugment = 0):
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_Joystick2DdotDisplay
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_Joystick2DdotDisplay = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_Joystick2DdotDisplay, text='   Joystick2DdotDisplay   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############
        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_Joystick2DdotDisplay = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    #################################################
    global Joystick2DdotDisplay_ReubenPython2and3ClassObject
    global Joystick2DdotDisplay_OPEN_FLAG
    global GUI_ROW_Joystick2DdotDisplay
    global GUI_COLUMN_Joystick2DdotDisplay
    global GUI_PADX_Joystick2DdotDisplay
    global GUI_PADY_Joystick2DdotDisplay
    global GUI_ROWSPAN_Joystick2DdotDisplay
    global GUI_COLUMNSPAN_Joystick2DdotDisplay

    global Joystick2DdotDisplay_ReubenPython2and3ClassObject_GUIparametersDict
    Joystick2DdotDisplay_ReubenPython2and3ClassObject_GUIparametersDict = dict([("root", Tab_Joystick2DdotDisplay),
                                    ("GUI_ROW", GUI_ROW_Joystick2DdotDisplay),
                                    ("GUI_COLUMN", GUI_COLUMN_Joystick2DdotDisplay),
                                    ("GUI_PADX", GUI_PADX_Joystick2DdotDisplay),
                                    ("GUI_PADY", GUI_PADY_Joystick2DdotDisplay),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_Joystick2DdotDisplay),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_Joystick2DdotDisplay)])

    global Joystick2DdotDisplay_ReubenPython2and3ClassObject_setup_dict
    Joystick2DdotDisplay_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", Joystick2DdotDisplay_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                         ("NameToDisplay_UserSet", "Test"),
                                                                         ("JoystickXYboxCanvas_HeightAndWidth", 300),
                                                                         ("MaxValue", 20.0),
                                                                         ("Crosshairs_ShowFlag", 1),
                                                                         ("Crosshairs_HorizontalLine_Yvalue", 2.0),
                                                                         ("Crosshairs_VerticalLine_Xvalue", 0.0),
                                                                         ("ExtendMarkerRadiallyToOriginFlag", 1),
                                                                         ("CircularBoundary_Radius", 5.0)])

    try:
        Joystick2DdotDisplay_ReubenPython2and3ClassObject = Joystick2DdotDisplay_ReubenPython2and3Class(Joystick2DdotDisplay_ReubenPython2and3ClassObject_setup_dict)
        Joystick2DdotDisplay_OPEN_FLAG = Joystick2DdotDisplay_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

    except:
        exceptions = sys.exc_info()[0]
        print("Joystick2DdotDisplay_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
        traceback.print_exc()
    #################################################
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_Joystick2DdotDisplay_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1

    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_MyPrint_FLAG
    SHOW_IN_GUI_MyPrint_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_Joystick2DdotDisplay
    global GUI_COLUMN_Joystick2DdotDisplay
    global GUI_PADX_Joystick2DdotDisplay
    global GUI_PADY_Joystick2DdotDisplay
    global GUI_ROWSPAN_Joystick2DdotDisplay
    global GUI_COLUMNSPAN_Joystick2DdotDisplay
    GUI_ROW_Joystick2DdotDisplay = 1

    GUI_COLUMN_Joystick2DdotDisplay = 0
    GUI_PADX_Joystick2DdotDisplay = 1
    GUI_PADY_Joystick2DdotDisplay = 1
    GUI_ROWSPAN_Joystick2DdotDisplay = 1
    GUI_COLUMNSPAN_Joystick2DdotDisplay = 1

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint
    GUI_ROW_MyPrint = 2

    GUI_COLUMN_MyPrint = 0
    GUI_PADX_MyPrint = 1
    GUI_PADY_MyPrint = 1
    GUI_ROWSPAN_MyPrint = 1
    GUI_COLUMNSPAN_MyPrint = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global root

    global root_Xpos
    root_Xpos = 70

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_Joystick2DdotDisplay
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global SinusoidalMotionInput_ROMtestTimeToPeakAngle
    SinusoidalMotionInput_ROMtestTimeToPeakAngle = 2.0

    global SinusoidalMotionInput_MinValue
    SinusoidalMotionInput_MinValue = -10.0

    global SinusoidalMotionInput_MaxValue
    SinusoidalMotionInput_MaxValue = 10.0
    #################################################
    #################################################

    #################################################
    #################################################
    global Joystick2DdotDisplay_ReubenPython2and3ClassObject

    global Joystick2DdotDisplay_OPEN_FLAG
    Joystick2DdotDisplay_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
        Tab_MainControls = None
        Tab_Joystick2DdotDisplay = None
        Tab_MyPrint = None
    #################################################
    #################################################


    #################################################
    #################################################
    if USE_KEYBOARD_FLAG == 1 and EXIT_PROGRAM_FLAG == 0:
        keyboard.on_press_key("esc", ExitProgram_Callback)
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:

        global MyPrint_ReubenPython2and3ClassObject_GUIparametersDict
        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MyPrint),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                                                        ("GUI_PADX", GUI_PADX_MyPrint),
                                                                        ("GUI_PADY", GUI_PADY_MyPrint),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

        global MyPrint_ReubenPython2and3ClassObject_setup_dict
        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MyPrint_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if Joystick2DdotDisplay_OPEN_FLAG != 1:
        print("Failed to open Joystick2DdotDisplay_ReubenPython2and3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1 and MyPrint_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    print("Starting main loop 'test_program_for_Joystick2DdotDisplay_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################
        ###################################################

        ################################################### SET's
        ###################################################
        SinusoidalMotionInput_TimeGain = math.pi / (2.0 * SinusoidalMotionInput_ROMtestTimeToPeakAngle)

        SinusoidalMotionInput_CommandedValue_X = (SinusoidalMotionInput_MaxValue + SinusoidalMotionInput_MinValue)/2.0 + 0.5*abs(SinusoidalMotionInput_MaxValue - SinusoidalMotionInput_MinValue)*math.sin(SinusoidalMotionInput_TimeGain*CurrentTime_MainLoopThread)
        SinusoidalMotionInput_CommandedValue_Y = (SinusoidalMotionInput_MaxValue + SinusoidalMotionInput_MinValue)/2.0 + 0.5*abs(SinusoidalMotionInput_MaxValue - SinusoidalMotionInput_MinValue)*math.cos(SinusoidalMotionInput_TimeGain*CurrentTime_MainLoopThread)

        Joystick2DdotDisplay_ReubenPython2and3ClassObject.UpdateDotCoordinatesAndDotColor(SinusoidalMotionInput_CommandedValue_X, SinusoidalMotionInput_CommandedValue_Y, round(SinusoidalMotionInput_CommandedValue_X))
        ###################################################
        ###################################################

        time.sleep(0.002)
    #################################################
    #################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_Joystick2DdotDisplay_ReubenPython2and3Class.")

    #################################################
    if Joystick2DdotDisplay_OPEN_FLAG == 1:
        pass
        #Joystick2DdotDisplay_ReubenPython2and3ClassObject.ExitProgram_Callback() #THIS FUNCTION DOESN'T EXIST AS THE CLASS DOESN NOT NEED TO BE CLOSED.
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################