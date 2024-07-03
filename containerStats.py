import functions as f
import time
import constants as cst

print("containerStats started")
# ожидаемый формат команды в stats.txt : camino-back
args = f.getStatsParams()
containerName = args[0]
f.clearBufferStats()

while (containerName != "stopScript"):
    print("containerStats waiting")
    if(containerName != "" and containerName != "stopScript"):
        print("containerStats working")
        f.statusContainer(containerName, cst.STATS_OUT_FL)
    time.sleep(1)
    containerName = f.getStatsParams()[0]
    f.clearBufferStats()

# print("Script stopped")