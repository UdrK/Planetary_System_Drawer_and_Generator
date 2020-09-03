import system
from solar_system import solar_radius as SR
from solar_system import earth_radius as ER
from solar_system import astronomical_unit as AU

# name, periapsis, apoapsis, radius, color, rings, ringscolor, systems

g = system.System('Kepler 11 g', AU*0.466, AU*0.466, ER*3.33, (211, 0, 106), 0, (0,0,0), [])
f = system.System('Kepler 11 f', AU*0.013, AU*0.013, ER*2.49, (185, 0, 211), 0, (0,0,0), [])
e = system.System('Kepler 11 e', AU*0.012, AU*0.012, ER*3.12, (87, 0, 211), 0, (0,0,0), [])
d = system.System('Kepler 11 d', AU*0.004, AU*0.004, ER*3.12, (0, 60, 211), 0, (0,0,0), [])
c = system.System('Kepler 11 c', AU*0.026, AU*0.026, ER*2.87, (0, 182, 211), 0, (0,0,0), [])   # random size next to jupiter since mass is close
b = system.System('Kepler 11 b', AU*0.091, AU*0.091, ER*1.83, (48, 152, 48), 0, (0,0,0), [])

planets = [b, c, d, e, f, g]
kepler_11 = system.System('Kepler 11', 0, 0, 1.021*SR, (252, 238, 33), 0, (0,0,0), planets)