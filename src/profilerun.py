'''Initial draft of OptiCraft server for Minecraft classic'''
from servercontroller import ServerController
import traceback
import time
from console import *
try:
    import cProfile as Profile
except ImportError:
    import Profile

def Main():
    ServerControl = ServerController()
    try:
        ServerControl.Run()
    except:
        Console.Error("Server","Server is shutting down.")
        fHandle = open("CrashLog.txt","a")
        fHandle.write("="*30 + "\n")
        fHandle.write("Crash date: %s\n" %time.strftime("%c", time.gmtime()))
        fHandle.write("="*30 + "\n")
        traceback.print_exc(file=fHandle)
        fHandle.close()
        ServerControl.Shutdown(True)

if __name__ == "__main__":
    Profile.run('Main()', 'profiler-%s.out' %time.strftime("%d-%m-%Y_%H-%M-%S", time.gmtime()))