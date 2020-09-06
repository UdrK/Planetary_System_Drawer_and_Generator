from system import System
from systems.solar_system import solar_radius as SR
from systems.solar_system import earth_radius as ER
import random

#  name, periapsis, apoapsis, radius, color, rings, ringscolor, systems

# making more probable stars that are probable to exist isn't easy, so i'll settle with random (at least for now)
# src: https://physics.stackexchange.com/questions/66805/distribution-of-star-colours-in-a-galaxy
star_colors = {
    'blue': (55, 160, 255),
    'light_blue': (128, 194, 255),
    'white': (247, 252, 253),
    'light_yellow': (254, 254, 214),
    'yellow': (253, 244, 163),
    'orange': (255, 158, 94),
    'red': (255, 73, 64)
}

# data on star size distribution is hard to come by, and in any case giant star seem to be very rare, and adhering
# perfectly to the data would mean never seeing such stars.
# sizes expressed in solar radii
star_types = {
    'large': (1.3, 2),
    'sun-like': (0.8, 1.2),
    'small': (0.4, 0.7),
    'dwarf': (0.1, 0.3),
}

# the type of planet isn't directly related to its size because density plays a major role
# however i'm interested in size
planet_types = {
    'gas_giant': (8, 12),
    'icy_giant': (3, 8),
    'super_earth': (1.2, 3),
    'terrestrial_planets': (0.8, 1.2),
    'dwarf_planets': (0.1, 0.7)
}

# the type of planet isn't directly related to its size because density plays a major role
# however i'm interested in size
planet_colors = [
    (85, 168, 104),
    (196, 78, 82),
    (129, 114, 179),
    (147, 120, 96),
    (140, 140, 140),
    (204, 185, 116),
    (100, 181, 205),
    (76, 114, 176),
    (221, 132, 82),
    (106, 204, 100),
    (214, 95, 95),
    (213, 187, 103),
    (130, 198, 226),
    (238, 133, 74),
    (72, 120, 208),
    (185, 242, 240),
    (161, 201, 244),
    (255, 180, 130),
    (141, 229, 161),
    (255, 159, 155),
    (236, 225, 51),
    (70, 162, 90),
    (18, 67, 43),
    (242, 242, 242),
    (78, 105, 160)
]


"""
    This method returns a random star
    
    Arguments:
        type: string meant to be the key of the system_generator.star_types dictionary
        color: string meant to be the key of the system_generator.star_colors dictionary 
"""
def generate_star(type='random', color='random'):

    if color == 'random':
        color, rgb_color = random.choice(list(star_colors.items()))
    else:
        rgb_color = star_colors[color]

    if type == 'random':
        type, size_limits = random.choice(list(star_types.items()))
        star_size = random.uniform(size_limits[0], size_limits[1])
    else:
        star_size = random.uniform(star_types[type][0], star_types[type][1])

    return System('{} {} star'.format(color, type), 0, 0, star_size*SR, rgb_color, 0, (0,0,0), [])


"""
    This method returns a procedurally generated planet

    Arguments:
        type: string meant to be the key of the system_generator.planet_types dictionary
        color: string meant to be the key of the system_generator.planet_colors dictionary
        
"""
def generate_planet(name, type='random', color='random', rings='random'):

    # color ------------------------------------------------------------------------
    if color == 'random':
        rgb_color = random.choice(planet_colors)
    else:
        rgb_color = planet_colors[int(color)]

    # size --------------------------------------------------------------------------

    if type == 'random':
        type, size_limits = random.choice(list(planet_types.items()))
        planet_size = random.uniform(size_limits[0], size_limits[1])
    else:
        planet_size = random.uniform(planet_types[type][0], planet_types[type][1])

    # rings -------------------------------------------------------------------------

    rings_size = 0
    rings_color = random.choice([(110, 99, 77), (45, 200, 200)])
    if rings == 'random':
        if random.choice(list(range(0, 10))) == 0:    # 10% change rings
            rings_size = random.uniform(1.25*planet_size, 3*planet_size)
    else:
        rings_size = rings

    return System(name, 0, 0, planet_size*ER, rgb_color, rings_size*ER,  rings_color, [])

"""
    This method returns a procedurally generated planetary system
    
    Arguments:
        number of planets: int, self explanatory
"""
def generate_random_system(number_of_planets=6):

    star = generate_star()
    for i in range(number_of_planets):
        star.systems.append(generate_planet('{}'.format(i)))

    return star
