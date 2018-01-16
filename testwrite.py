#! /usr/bin/env python

import sys
import getopt
from os import getcwd
from os.path import abspath, split

here = getcwd()
prev = split(abspath(here))[0]

def usage():
    print 'usage:'
    print './generateCMakeFile.py *argv'
    print 'parameter:'
    print '-h --help    : help information'   
    print '-d --dir     : the directory of the generated CMakeLists.txt locate'
    print '-p --project : the project name'
    print '-l --lib     : the lirary name'
    print '-e --exe     : the generated exe file name'
    print '-a -all      : set the project name, library name and the exe name using the same '\
                        'parameter'


def getArgvs():
    try:
        options, args = getopt.getopt(sys.argv[1:], "hp:l:e:d:a:", 
            ["help", "project=", "lib=", "exe=", "dir==", "all=="])
    except getopt.GetoptError:
        sys.exit()
    projectName = libraryName = exeName = dirName = None
    for name, value in options:
        if name in ("-h", "--help"):
            usage()
        if name in ("-p", "--project"):
            projectName = value
        if name in ("-l", "--lib"):
            libraryName = value
        if name in ("-e", "--exe"):
            exeName = value
        if name in ("-a", "--all"):
            projectName = libraryName = exeName = value
        if name in ("-d", "--dir"):
            if value == ".":
                dirName = here
            elif value == "..":
                dirName = prev
            else:
                dirName = value

    return projectName, libraryName, exeName, dirName


def generateCMakeFile(projectName, libraryName, exeName):
    if projectName is None:
        projectName = "default"
    if libraryName is None:
        libraryName = "defalut"
    if exeName is None:
        exeName = "defalut"

    cMakeFileLineList = []
    cMakeFileLineProject = "PROJECT({})\n".format(projectName)
    cMakeFileLineList.append(cMakeFileLineProject)
    cMakeFileLineCMakeVersion = "CMAKE_MINIMUM_REQUIRED(VERSION 2.8)\n"
    cMakeFileLineList.append(cMakeFileLineCMakeVersion)
    cMakeFileLineSetProjectRootPath = "SET(PROJECT_ROOT_PATH \"${CMAKE_SOURCE_DIR}\")\n"
    cMakeFileLineList.append(cMakeFileLineSetProjectRootPath)
    cMakeFileLineSetExeOutputPath = "SET(EXECUTABLE_OUTPUT_PATH \"${PROJECT_ROOT_PATH}/\")\n"
    cMakeFileLineList.append(cMakeFileLineSetExeOutputPath)
    cMakeFileLineSetLibOutputPath = "SET(LIBRARY_OUTPUT_PATH \"${PROJECT_ROOT_PATH}/lib/\")\n"
    cMakeFileLineList.append(cMakeFileLineSetLibOutputPath)
    cMakeFileLineSetCompile = "SET(CMAKE_CXX_COMPILE \"g++\")\n"
    cMakeFileLineList.append(cMakeFileLineSetCompile)
    cMakeFileLineSetCompileFlags = "SET(CMAKE_CXX_FLAGS \"-std=c++0x -g -fPIC -Wall -O0\")\n"
    cMakeFileLineList.append(cMakeFileLineSetCompileFlags)
    cMakeFileLineIncludeDir = "INCLUDE_DIRECTORIES(\"${PROJECT_ROOT_PATH}/include/\")\n"
    cMakeFileLineList.append(cMakeFileLineIncludeDir)
    cMakeFileLineLinkDir = "LINK_DIRECTORIES(\"${PROJECT_ROOT_PATH}/lib/\")\n"
    cMakeFileLineList.append(cMakeFileLineLinkDir)
    cMakeFileLineAuxSrcDir = "AUX_SOURCE_DIRECTORY(${{PROJECT_ROOT_PATH}}/src/ {}_src)\n".format(projectName)
    cMakeFileLineList.append(cMakeFileLineAuxSrcDir)
    cMakeFileLineExec = "ADD_EXECUTABLE({} ${{{}_src}} main.cpp)\n".format(exeName, projectName)
    cMakeFileLineList.append(cMakeFileLineExec)
    cMakeFileLineStaticLib = "ADD_LIBRARY({}_static STATIC ${{{}_src}})\n".format(libraryName, projectName)
    cMakeFileLineList.append(cMakeFileLineStaticLib)
    cMakeFileLineSharedLib = "ADD_LIBRARY({}_shared SHARED ${{{}_src}})\n".format(libraryName, projectName)
    cMakeFileLineList.append(cMakeFileLineSharedLib)

    cMakeFileText = "".join(cMakeFileLineList)
    return cMakeFileText


def main():
    projectName, libraryName, exeName, dirName = getArgvs()
    cMakeFileText = generateCMakeFile(projectName, libraryName, exeName)

    if dirName is None:
        dirName = here
    fileDir = dirName + '/' + 'CMakeLists.txt'
    with open(fileDir, 'w') as f:
        f.write(cMakeFileText)


if __name__ == "__main__":
    main()

