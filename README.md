# betterLogs4Python
As the name says, it's a little helper for logging more comfortably in python 3 (for now only python3 support) to file and console!

## Installation

For an easy installation install betterLogs4Python via pip:

```bash
pip3 install betterLogs4Python
```

For an executable Demo or test run [Demo.py](https://github.com/JonasMayerDev/betterLogs4Python/blob/main/LICENSE).

## How To Use

1. Create a BetterLogger object (maybe with parameters)
    All Parameters are optional:
    
    Parameter          | Default       |Description
    -------------------|---------------|------------------------------------
    logFilename        |"app.log"      |(String) Defines the filename/path the BetterLogger will log to if printToFile is True.
    loggerName         |""             |(String) Defines a module name that will be added to the log message.
    includeTime        |False          |(Bool)   Defines if the log time should be included.
    printToConsole     |True           |(Bool)   Defines if the log messages should be printed to stdout (Console output).
    printToFile        |True           |(Bool)   Defines if the log messages should be printed to file (specified in logFilename parameter).
    lineLimiter        |-1             |(Int > 0) Defines the max number of lines in the log file. (-1 means no limit) (When exceeding the limit, old logs get deleted).
    runLimiter         |-1             |(Int > 0) Defines the max number of runs in the log file. Runs are separated with String defined in runSeparator parameter. (-1 means no limit) (When exceeding the limit, old runs get deleted).
    logLevelThreshold  |0              |(Int)    Defines the threshold of log level number that get logged (Message will only get printed to File or Console if it's logLevelNum > logLevelThreshold. Else the log will be ignored. Default logLevelNum is 20).
    runSeparator       |"----------"   |(String)   Defines the String that defines the end of a run. It gets used to retain the runLimit and gets logged when finishRun function is called. (If you normal log contains the runSeparator String it counts as the runSeparator)

    ```python
    logger = BetterLogger()
    ```

2. Log to file by calling the log function with the logLevelNum parameter to define the type of the log message (default ist 20).
    The logLevelNum corresponds to the types as follows:
    
    Number	    |Type  
    ------------|-------------------
    10 		    |"DEBUG"  
    20 (Default)|"INFO" 
    30 		    |"WARNING"
    40 		    |"ERROR"  
    50 		    |"FATAL"  

    ```python
    logger.log("Hello this is an Debug!",logLevelNum=10)
    ```
    You can also add new log types:
    ```python
    logger.addLogLevelName("EXECUTION",25)
    logger.log("Hello this the new execution type!",logLevelNum=25)
    ```
3. If using the runLimiter maybe call the finishRun function to finish the run.
    ```python
    logger.finishRun()
    ```
4. Enjoy the Output :)

## Simple logger
```python
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

```
## More advanced logger
```python
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
```

## Run limited logger 
```python
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
```

When you notice any errors, have a problem using this software or have a suggestion for improvement, feel free to open an [issue](https://github.com/JonasMayerDev/betterLogs4Python/issues) or a [pull request](https://github.com/JonasMayerDev/betterLogs4Python/pulls) 

## License
This software is licensed under the MIT License:
```
MIT License

Copyright (c) 2021 Jonas Mayer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
