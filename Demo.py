from betterLogs4Python import BetterLogger

# After getting a logger object with the logfile path,
# you can log by calling the log function with optionally a logLevel that defines what type of log Message it is:
#       10 : "DEBUG",
#       20 : "INFO",
#       30 : "WARNING",
#       40 : "ERROR",
#       50 : "FATAL"

# Defaults of BetterLogger class: logFilename="app.log", loggerName="",includeTime=False,printToConsole=True,printToFile=True,lineLimiter=-1, runLimiter=-1, logLevelThreshold=0, runSeparator="----------"
# For a simple Log you can use the defaults!

logger = BetterLogger(logFilename="test.log")

logger.log("Hello this is an Info!") # Default log Level is 20 (INFO)
logger.log("Hello this is an Debug!",logLevelNum=10)
logger.log("Hello this is an Error!",logLevelNum=40)

# You can add new log message types with a new logLevelNumber
logger.addLogLevelName("EXECUTION",25)
logger.log("Hello this the new execution type!",logLevelNum=25)


# Output will be to the test.log file and to console:
#[INFO] Hello this is an Info!
#[DEBUG] Hello this is an Debug!
#[ERROR] Hello this is an Error!
#[EXECUTION] Hello this the new execution type!




# Example for a Logger that logs only to the File "test.log". (Not the Console!)
# The log includes Timestamps and a module name "testModule". 
# The number of Lines in the Logfile is limited to 15 lines (oldest lines get removed when exceded!).
# The Logger will only write logs if the given logLevel is greater than 10 (10 is not included)  
logger = BetterLogger(logFilename="test.log",includeTime=True,loggerName="testModule",printToConsole=False,printToFile=True,lineLimiter=15,logLevelThreshold=5)

logger.addLogLevelName("Test",5)
logger.log("Hello this is a less important Test type!",logLevelNum=5) # Won't get printed because the logLevel is not greater than the logLevelThreshold (5)

logger.addLogLevelName("Important",100)
logger.log("This is a more Important message!",100)
# The Output will only be in the file "test.log"
#[2021-09-05 07:00:40,239] testModule: [Important] This is a more Important message!




# Example for a Logger that logs to the File "test.log" and the Console.
# The Log contains no Timestamp and no module name. 
# The log file only stores 2 runs seperated by "-----" (older runs get deleted)
logger = BetterLogger(logFilename="test.log",runLimiter=2,runSeparator="-----")
logger.log("Test")
for i in range(4): # Simulate 4 runs
    logger.log("Info-Log of 1 run!")
    logger.log("Oh Error in run: "+str(i+1),40)
    logger.finishRun()

# Output in console includes logs for all 4 runs but in file are only logs for run 3 and 4 (last 2 runs):
#[INFO] Info-Log of 1 run!
#[ERROR] Oh Error in run: 3
#-----
#[INFO] Info-Log of 1 run!
#[ERROR] Oh Error in run: 4
#-----

