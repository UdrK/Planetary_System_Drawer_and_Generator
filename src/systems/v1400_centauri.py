import system
from systems.solar_system import solar_radius as SR
from systems.solar_system import earth_radius as ER
from systems.solar_system import astronomical_unit as AU

# name, periapsis, apoapsis, radius, color, rings, ringscolor, systems

b = system.System('1SWAP J1407b', AU*3.9, AU*3.9, ER*10.92, (48, 152, 48), 42000000, (110, 99, 77), [])

planets = [b]
v1400_centauri = system.System('V1400 Centauri', 0, 0, 0.93*SR, (249, 127, 50), 0, (0,0,0), planets)