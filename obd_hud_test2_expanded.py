# Since the standard query() function is blocking, it can be a hazard for UI event loops.
# To deal with this, python-OBD has an Async connection object
# that can be used in place of the standard OBD object.
# Async is a subclass of OBD, and therefore inherits all of the standard methods.
# However, Async adds a few in order to control a threaded update loop.
# This loop will keep the values of your commands up to date with the vehicle.
# This way, when the user querys the car, the latest response is returned immediately.

import obd
import time
connection = obd.Async()  # same constructor as 'obd.OBD()'

for i in range(4, 17, 1):
    connection.watch(obd.commands[1][i])

connection.start()  # start the async update loop

print(connection.query(obd.commands[1][4:17]))  # non-blocking, returns immediately

time.sleep(60)
connection.stop()