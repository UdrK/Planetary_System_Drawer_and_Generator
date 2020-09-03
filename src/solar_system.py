import system
grey = [138, 138, 138]      # color shared by different moons

# name, periapsis, apoapsis, radius, color, rings, ringscolor, systems

mercury = system.System('Mercury', 46001200, 69816900, 2439, (212, 160, 38), 0, (0,0,0), [])
venus = system.System('Venus', 107477000, 108939000, 6051, (212, 160, 38), 0, (0,0,0), [])

moon = system.System('Moon', 362600, 405400, 1737, (82, 81, 77), 0, (0,0,0), [])
earth = system.System('Earth', 147095000, 152100000, 6371, (33, 134, 207), 0, (0,0,0), [moon])

phobos = system.System('Phobos', 9234, 9517, 11, grey, 0, (0,0,0), [])
deimos = system.System('Deimos', 23455, 23470, 6, grey, 0, (0,0,0), [])
mars = system.System('Earth', 206700000, 249200000, 3389, (199, 100, 0), 0, (0,0,0), [phobos, deimos])

io = system.System('Io', 420000, 423400, 1821, (133, 119, 74), 0, (0,0,0), [])
europa = system.System('Europa', 664862, 676938, 1560, (187, 178, 155), 0, (0,0,0), [])
ganymede = system.System('Ganymede', 1069200, 1071600, 2634, (57, 39, 36), 0, (0,0,0), [])
callisto = system.System('Callisto', 1869000, 1897000, 2410, (57, 39, 36), 0, (0,0,0), [])
jupiter = system.System('Jupiter', 740000000, 816000000, 69911, (230, 198, 139), 0, (0,0,0), [io, europa, ganymede, callisto])

rhea = system.System('Rhea', 376566, 3662704, 763, (159, 159, 159), 0, (0,0,0), [])
titan = system.System('Titan', 1186680, 1257060, 2574, (236, 201, 101), 0, (0,0,0), [])
iapetus = system.System('Iapetus', 3458936, 3662704, 734, (66, 52, 14), 0, (0,0,0), [])
saturn = system.System('Saturn', 1352550000, 1433530000, 58232, (245, 231, 207), 136780, (110, 99, 77), [rhea, titan, iapetus])

ariel = system.System('Ariel', 191129, 190670, 578, (115, 97, 95), 0, (0,0,0), [])
umbriel = system.System('Umbriel', 264962, 267037, 584, (89, 89, 89), 0, (0,0,0), [])
titania = system.System('Titania', 435820, 436779, 788, (193, 181, 169), 0, (0,0,0), [])
oberon = system.System('Oberon', 582683, 584316, 761, (177, 146, 115), 0, (0,0,0), [])
uranus = system.System('Uranus', 2742000000, 3008000000, 25362, (207, 245, 248), 0, (0, 0, 0), [ariel, umbriel, titania, oberon])

triton = system.System('Triton', 354754, 354765, 1353, (210,197,188), 0, (0,0,0), [])
neptune = system.System('Neptune', 4460000000, 4540000000, 24622, (61,91,231), 0, (0, 0, 0), [triton])

planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
solar_system = system.System('Sun', 0, 0, 695510, (215, 39, 2), 0, (0,0,0), planets)
