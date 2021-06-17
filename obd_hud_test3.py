import obd
import time
connection = obd.Async() # same constructor as 'obd.OBD()'

connection.watch(obd.commands.[1][12]) # keep track of the RPM

connection.start() # start the async update loop

print (connection.query(obd.commands.RPM)) # non-blocking, returns immediately

time.sleep(60)
connection.stop()
