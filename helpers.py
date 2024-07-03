import constants as const
import subprocess

def readInputFile(filename):
	with open(const.PATH_INPUT+filename, "r") as file:
		data = file.read()
	return data

def writeInputFile(filename, str):
	f = open(const.PATH_INPUT+filename, "w+")
	f.write(str)
	f.close()
	return True

def writeOutputFile(filename, str):
	f = open(const.PATH_OUTPUT+filename, "w+")
	f.write(str)
	f.close()
	return True
