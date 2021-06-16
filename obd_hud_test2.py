import obd
import time

# connection = obd.OBD()
# instead of querying a connection each time you want a response,
# you can create an asynchronous connection that updatates each time the value changes

connection = obd.Async()  # a subclass of OBD that can control a threaded update loop


# a callback that prints every new value to the console
def new_status(st):
    print(st.value)


def new_freeze_dtc(fdtc):
    print(fdtc.value)


def new_fuel_status(fs):
    print(fs.value)


def new_engine_load(el):
    print(el.value)


def new_coolant_temp(ct):
    print(ct.value)


def new_short_fuel_trim_1(sft1):
    print(sft1.value)


def new_long_fuel_trim_1(lft1):
    print(lft1.value)


def new_short_fuel_trim_2(sft2):
    print(sft2.value)


def new_long_fuel_trim_2(lft2):
    print(lft2.value)


def new_fuel_pressure(fp):
    print(fp.value)


def new_intake_pressure(ip):
    print(ip.value)


def new_rpm(r):
    print(r.value)


def new_speed(s):
    print(s.value)


def new_timing_advance(ta):
    print(ta.value)


def new_intake_temp(it):
    print(it.value)


def new_mass_air_flow(maf):
    print(maf.value)


connection.watch(obd.commands.STATUS, callback=new_status)
connection.watch(obd.commands.FREEZE_DTC, callback=new_freeze_dtc)
connection.watch(obd.commands.FUEL_STATUS, callback=new_fuel_status)
connection.watch(obd.commands.ENGINE_LOAD, callback=new_engine_load)
connection.watch(obd.commands.COOLANT_TEMP, callback=new_coolant_temp)
connection.watch(obd.commands.SHORT_FUEL_TRIM_1, callback=new_short_fuel_trim_1)
connection.watch(obd.commands.LONG_FUEL_TRIM_1, callback=new_long_fuel_trim_1)
connection.watch(obd.commands.SHORT_FUEL_TRIM_2, callback=new_short_fuel_trim_2)
connection.watch(obd.commands.LONG_FUEL_TRIM_2, callback=new_long_fuel_trim_2)
connection.watch(obd.commands.FUEL_PRESSURE, callback=new_fuel_pressure)
connection.watch(obd.commands.INTAKE_PRESSURE, callback=new_intake_pressure)
connection.watch(obd.commands.RPM, callback=new_rpm)  # keeps track of RPM
connection.watch(obd.commands.SPEED, callback=new_speed)
connection.watch(obd.commands.TIMING_ADVANCE, callback=new_timing_advance)
connection.watch(obd.commands.INTAKE_TEMP, callback=new_intake_temp)
connection.watch(obd.commands.MAF, callback=new_mass_air_flow)

connection.start()  # starts the async of new values

# the call back will now be fired upon receipt of new values

time.sleep(60)  # suspends execution for the given number of seconds
connection.stop()  # stops the update loop
