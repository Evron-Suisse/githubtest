import obd
import time

#connection = obd.OBD()
#instead of querying a connection each time you want a response,
#you can create an asynchronous connection that updatates each time the value changes

connection = obd.Async() #a subclass of OBD that can control a threaded update loop

#a callback that prints every new value to the console
def new_rpm(r):
    print(r.value)


connection.watch(obd.commands.RPM, callback = new_rpm) #keeps track of RPM




connection.start() #starts the async of new values

# the call back will now be fired upon receipt of new values

time.sleep(60) #suspends execution for the given number of seconds
connection.stop() #stops the update loop