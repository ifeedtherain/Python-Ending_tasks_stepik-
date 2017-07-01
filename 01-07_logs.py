import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, arg):
	    super(LoggableList, self).append(arg)
	    self.log(arg)