import constants as const
import subprocess

def readInputFile(filename):
	with open(const.PATH_INPUT+filename, "r") as file:
		data = file.read()
	return data

def writeToFile(filepath, str, type="w+"):
	with open(filepath, type) as f:
		f.write(str)
	return True


def writeInputFile(filename, str, type="w+"):
	writeToFile(const.PATH_INPUT+filename, str, type)
	return True

def writeOutputFile(filename, str, type="w+"):
	writeToFile(const.PATH_OUTPUT+filename, str, type)
	return True
