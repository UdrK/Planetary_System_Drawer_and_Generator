star_colors = {
    'blue': (55, 160, 255),
    'light_blue': (128, 194, 255),
    'white': (247, 252, 253),
    'light_yellow': (254, 254, 214),
    'yellow': (253, 244, 163),
    'orange': (255, 158, 94),
    'red': (255, 73, 64)
}

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


__blue_white_star_rocky_planet_colors = [(196, 78, 82), (147, 120, 96), (172, 172, 172), (140, 140, 140), (201, 162, 109)]
__blue_white_star_planet_colors = {
        'gas_giant': [(221, 132, 82), (129, 114, 179), (255, 159, 155), (255, 180, 130)],
        'icy_giant': [(141, 229, 161), (213, 187, 103)],
        'super_earth': __blue_white_star_rocky_planet_colors,
        'terrestrial_planet': __blue_white_star_rocky_planet_colors,
        'dwarf_planet': __blue_white_star_rocky_planet_colors
}

_yellow_star_planet_colors = {
    'gas_giant': [(221, 132, 82), (129, 114, 179)],
    'icy_giant': [(100, 181, 205), (78, 105, 160)],
    'super_earth': __blue_white_star_rocky_planet_colors,
    'terrestrial_planet': __blue_white_star_rocky_planet_colors,
    'dwarf_planet': __blue_white_star_rocky_planet_colors
}

__orange_red_star_rocky_planet_colors = [(85, 168, 104), (140, 140, 140), (172, 172, 172), (185, 242, 240), (236, 225, 51)]

__orange_star_planet_colors = {
    'gas_giant': [(72, 120, 208), (78, 105, 160), (129, 114, 179)],
    'icy_giant': [(247, 252, 253), (130, 198, 223), (222, 225, 168)],
    'super_earth': __orange_red_star_rocky_planet_colors,
    'terrestrial_planet': __orange_red_star_rocky_planet_colors,
    'dwarf_planet': __orange_red_star_rocky_planet_colors
}

__red_star_planet_colors = {
    'gas_giant': [(72, 120, 208), (78, 105, 160), (129, 114, 179)],
    'icy_giant': [(247, 252, 253), (130, 198, 223), (222, 225, 168)],
    'super_earth': __orange_red_star_rocky_planet_colors,
    'terrestrial_planet': __orange_red_star_rocky_planet_colors,
    'dwarf_planet': __orange_red_star_rocky_planet_colors[1:len(__orange_red_star_rocky_planet_colors)].append((106, 204, 100))
}

star_appropriate_planet_type_colors = {
    'blue': __blue_white_star_planet_colors,
    'light_blue': __blue_white_star_planet_colors,
    'white': __blue_white_star_planet_colors,
    'light_yellow': _yellow_star_planet_colors,
    'yellow': _yellow_star_planet_colors,
    'orange': __orange_star_planet_colors,
    'red': __red_star_planet_colors
}