import functions as f
import time

# ожидаемый формат команды в params.txt : imagename start containername
args = f.getContainerParams()
imgName = args[0]
contAct = args[1]
contName = args[2]
f.clearBuffer()

while (contName != "stopScript"):
    args = f.getContainerParams()
    imgName = args[0]
    contAct = args[1]
    contName = args[2]
    f.clearBuffer()
    if(imgName != "" and contName != "stopScript"):
        if (contAct == "start"):
            if(not f.ifContainerExists(contName)):
                # если нет - создать
                f.createContainer(imgName, contName)
            f.startContainer(contName)
        elif (contAct == "stop" and f.ifContainerExists(contName)):
            f.stopContainer(contName)
        f.statusContainer(contName)
    time.sleep(3)

# print("Script stopped")