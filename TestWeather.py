from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('e447c4b3d5b3eaf55963973d40d0959a')

temp = w.temperature('celsius')
place = input('Country/City:')

mgr = owm.weather_manager()
observation = mgr.weather_at_place( place )
w = observation.weather
print(w)
print('Погода' + temp)