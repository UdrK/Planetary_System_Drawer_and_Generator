import system
from solar_system import solar_radius as SR
from solar_system import earth_radius as ER
from solar_system import astronomical_unit as AU

# name, periapsis, apoapsis, radius, color, rings, ringscolor, systems

h = system.System('Trappist 1 h', AU*0.062, AU*0.062, ER*0.33, (39, 150, 89), 0, (0,0,0), [])
g = system.System('Trappist 1 g', AU*0.047, AU*0.047, ER*1.15, (211, 0, 106), 0, (0,0,0), [])
f = system.System('Trappist 1 f', AU*0.039, AU*0.039, ER*0.93, (185, 0, 211), 0, (0,0,0), [])
e = system.System('Trappist 1 e', AU*0.029, AU*0.029, ER*0.77, (87, 0, 211), 0, (0,0,0), [])
d = system.System('Trappist 1 d', AU*0.022, AU*0.022, ER*0.30, (0, 60, 211), 0, (0,0,0), [])
c = system.System('Trappist 1 c', AU*0.016, AU*0.016, ER*1.16, (0, 182, 211), 0, (0,0,0), [])   # random size next to jupiter since mass is close
b = system.System('Trappist 1 b', AU*0.012, AU*0.012, ER*1.02, (48, 152, 48), 0, (0,0,0), [])

planets = [b, c, d, e, f, g, h]
trappist_1 = system.System('Trappist 1', 0, 0, 0.119*SR, (249, 127, 50), 0, (0,0,0), planets)