import functions as f
import time
import constants as cst

print("containerStats started")
# ожидаемый формат команды в stats.txt : camino-back
# args = f.getStatsParams()
# containerName = args[0]
# f.clearBufferStats()
stopCommand = False

while ( not stopCommand ):
    # print("containerStats waiting")
    containerName = f.getParamContainerStats()
    f.clearBufferStats("container_stats")
    if(containerName != "" and containerName != "stopScript"):
        print("containerStats working")
        f.statusContainer(containerName, cst.STATS_OUT_FL)
    time.sleep(1)
    stopCommand = f.isStop(containerName)

# print("Script stopped")