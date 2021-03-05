import datetime
import pytz

"""
t = datetime.time(9,30,45,100000)

print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

dt_tm = datetime.datetime(2016,7,26,12,30,45,100000)

print(dt_tm)
print(dt_tm.year)

tdelts =datetime.timedelta(days=7)
print(dt_tm + tdelts)
tdelts =datetime.timedelta(hours=12)
print(dt_tm + tdelts)

dt_tdy = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_tdy)
print(dt_now)
print(dt_utcnow)          """

"""
dt = datetime.datetime(2016,7,27,12,30,45,tzinfo=pytz.UTC)
print(dt)          """

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone("US/Mountain"))
print(dt_mtn)
"""
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)    """

#this will raise error
dt_mtn = datetime.datetime.now()
dt_east = dt_mtn.astimezone(pytz.timezone("US/Eastern"))
print(dt_mtn)

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone("US/Mountain")
dt_mtn = mtn_tz.localize(dt_mtn)
print(dt_mtn)

