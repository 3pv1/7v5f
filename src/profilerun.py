'''Initial draft of OptiCraft server for Minecraft classic'''
from servercontroller import ServerController
import traceback
import time
try:
    import cProfile as Profile
except ImportError:
    import Profile

def Main():
    ServerControl = ServerController()
    try:
        ServerControl.run()
    except:
        fHandle = open("CrashLog.txt","a")
        fHandle.write("="*30 + "\n")
        fHandle.write("Crash date: %s\n" %time.strftime("%c", time.gmtime()))
        fHandle.write("="*30 + "\n")
        traceback.print_exc(file=fHandle)
        fHandle.close()
        ServerControl.HeartBeatControl.Running = False
        ServerControl.SaveAllWorlds()

if __name__ == "__main__":
    Profile.run('Main()', 'profiler.out')