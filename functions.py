import subprocess
import hashlib
import helpers as h

# список всех конейнеров
def getContainersData():
	res = runCommand('docker ps -a')
	if (isSuccess(res)):
		ret = res.stdout
	else:
		ret = []
	return ret

# преобразовать в массив строк
def getContainersList():
	resp = getContainersData()
	return resp.splitlines()[1:]

# проверить наличие в списке контейнеров
def ifContainerExists(name):
	ret = False
	if (name.strip() != ""):
		command = f"docker ps --filter \"NAME={name}\" "
		res = runCommand(command)
		if (isSuccess(res) and len(res.stdout.splitlines()) > 1):
			ret = True
	# contList = getContainersList()
	# for i in range(0, len(contList)):
	# 	row = contList[i].split('\t')
	# 	print(row)

	return ret

#
def isSuccess(data):
	out = False
	if data.returncode == 0:
		out = True
	return out

# запуск шелл команды из питона, вернуть результат в виде текста
def runCommand(command):
	return subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# параметры пользователя из файла (название контейнера)  
def getContainerParams():
	str = h.readInputFile('params.txt')
	params = str.split()
	if len(params) < 1:
		params = ["","",""]
	# if len(params) < 2:
	# 	params.extend([""])
	# if len(params) < 3:
	# 	params.extend([""])
	return params

# создать контейнер
def createContainer(imgName, contName):
	# command = f"docker create --name {contName} -p 8003:80 -v /home/sadmin/Work/dockerpipe:/api/docker/hostpipe {imgName}"
	command = f"docker create --name {contName} -v /home/sadmin/Work/pipe/neurobuffer:/code/buffer {imgName}"
	print(command)
	res = runCommand(command)
	if (isSuccess(res)):
		ret = res.stdout
	else:
		ret = []
	return ret

# запустить контейнер
def startContainer(name):
	command = f"docker start {name}"
	res = runCommand(command)
	if (isSuccess(res)):
		ret = res.stdout
	else:
		ret = []
	return ret

# запустить контейнер
def stopContainer(name):
	command = f"docker container stop {name}"
	res = runCommand(command)
	if (isSuccess(res)):
		ret = res.stdout
	else:
		ret = []
	return ret

# состояние контейнера
def statusContainer(name):
	resp = runCommand('docker stats '+name+' --format "{{.ID}} {{.Name}} {{.Container}} {{.CPUPerc}}" --no-stream')
	# print(resp.stdout.splitlines()[0].split()[0])
	print(resp.stdout)
	h.writeOutputFile('response.txt', resp.stdout)
	# return resp.stdout

# 
def clearBuffer():
	h.writeInputFile('params.txt', '')


# command = 'docker images'
# command = 'docker ps -a'
# output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# if output.returncode != 0:
#  print('Ошибка:', output.stderr)
# else:
# 	arr = output.stdout.splitlines()
# 	print('Count containers='+ str(len(arr)))
# 	# print(arr[0])
# 	# print(arr[1])
# 	# words = arr[0].split()
# 	# print(words[1])
# # print('Вывод:', output.stdout)

# my_file = open("container-start/status.txt", "w+")
# my_file.write("running")
# my_file.close()