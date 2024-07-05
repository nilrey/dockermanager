import functions as f
import time
import constants as cst
# ожидаемый формат команды в params.txt : imagename start containername
# args = f.getContainerParams()
# imgName = args[0]
# contAct = args[1]
# containerName = args[2]
# f.clearBuffer()
stopCommand = False
print("containerManager started")

while ( not stopCommand ):
    args = f.getContainerParams()
    imgName = args[0]
    contAct = args[1]
    containerName = args[2]
    f.clearBuffer()
    if(imgName != "" and containerName != "stopScript"):
        if (contAct == "start"):
            if(not f.ifContainerExists(containerName)):
                # если нет - создать
                f.createContainer(imgName, containerName)
            f.startContainer(containerName)
        elif (contAct == "stop" and f.ifContainerExists(containerName)):
            f.stopContainer(containerName)
        f.statusContainerRun(containerName)
    
    stopCommand = f.isStop(containerName)
    time.sleep(1)

# print("Script stopped")