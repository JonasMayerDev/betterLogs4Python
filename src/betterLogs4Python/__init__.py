#  SPDX-FileCopyrightText: 2021 Jonas Mayer <jonas.mayer.dev@gmail.com>
#  SPDX-License-Identifier: MIT
class BetterLogger:
    import logging
    import sys

    logLevelTable = { 
        10 : "DEBUG",
        20 : "INFO",
        30 : "WARNING",
        40 : "ERROR",
        50 : "FATAL"
    }

    def get_console_handler(self):
        console_handler = self.logging.StreamHandler(self.sys.stdout)
        console_handler.setFormatter(self.FORMATTER)
        return console_handler

    def get_file_handler(self):
        file_handler = self.logging.FileHandler(self.filename)
        file_handler.setFormatter(self.FORMATTER)
        return file_handler

    def __init__(self,logFilename="app.log", loggerName="",includeTime=False,printToConsole=True,printToFile=True,lineLimiter=-1, runLimiter=-1, logLevelThreshold=0, runSeparator="----------"):

        self.filename = logFilename
        self.logLevelThreshold = logLevelThreshold
        self.lineLimiter=lineLimiter
        self.runLimiter=runLimiter
        self.runDevider = runSeparator
        formatterName = "%(name)s: "
        if(loggerName == ""):
            formatterName = ""
        
        if(includeTime):
            self.FORMATTER = self.logging.Formatter("[%(asctime)s] "+ formatterName+"%(message)s")
        else:
            self.FORMATTER = self.logging.Formatter(formatterName+"%(message)s")


        self.my_logger = self.logging.getLogger(loggerName)
        self.my_logger.propagate = False
        self.my_logger.setLevel(self.logging.DEBUG) # better to have too much log than not enough
        
        for hdl in self.my_logger.handlers:         # remove old logger handlers from previous run (For some reason need to be run twice)
            self.my_logger.removeHandler(hdl)
        for hdl in self.my_logger.handlers:
            self.my_logger.removeHandler(hdl)

        if(printToConsole):
            self.my_logger.addHandler(self.get_console_handler())
        if(printToFile):
            self.my_logger.addHandler(self.get_file_handler())
    
    def getLogLevelName(self, logLevelNum):
        try:
            return self.logLevelTable[logLevelNum]
        except KeyError:
            raise Exception("\nLog levelNumber not known!\nAdd it with addLogLevelName function of better Logger or choose an existing one: "+str(self.logLevelTable))

    def addLogLevelName(self, name, number):
        self.logLevelTable[number] = name
    
    def checkRunNumber(self):
        runCount = 0
        with open(self.filename,"r") as reader:
            for line in reader.readlines():
                if(self.runDevider in line):
                    runCount += 1
        return runCount
    
    def deleteRuns(self,runNumber):
        with open(self.filename,"r+") as editor:
            lines = editor.readlines()
            lineCount = 0
            for line in lines:
                if(self.runDevider in line):
                    runNumber -= 1
                if(runNumber <= 0):
                    break
                lineCount += 1
            editor.seek(0)
            editor.truncate()

            # start writing lines except the first line
            # lines[1:] from line n to last line
            editor.writelines(lines[lineCount+1:])
    
    def checkLineNumber(self):
        with open(self.filename,"r") as reader:
            return len(reader.readlines())

    def deleteLines(self,lineNumber):
        with open(self.filename,"r+") as editor:
            lines = editor.readlines()
            editor.seek(0)
            editor.truncate()

            # start writing lines except the first line
            # lines[1:] from line n to last line
            editor.writelines(lines[lineNumber:])

    def log(self,message,logLevelNum=20):
        if(self.logLevelThreshold >= logLevelNum):
            return
        
        if(self.runLimiter != -1 ):
            runNumber = self.checkRunNumber()
            if(runNumber >= self.runLimiter):
                self.deleteRuns(runNumber+1-self.runLimiter)
        
        if(self.lineLimiter != -1 ):
            lineNumber = self.checkLineNumber()
            if(lineNumber >= self.lineLimiter):
                self.deleteLines(lineNumber+1-self.lineLimiter)
        
        self.my_logger.log(self.logging.INFO,"["+str(self.getLogLevelName(logLevelNum))+"] "+str(message))

    def finishRun(self):
        self.my_logger.log(self.logging.INFO,self.runDevider)



