import math

"""
    This method draws and colors the background of the image
    
    Arguments:
        cc: Cairo.context()
        width, height: width and height in px of image
        rgb: tuple (r,g,b) of rgb color for background
"""
def draw_background(cc, width, height, rgb):

    cc.set_source_rgb(rgb[0], rgb[1], rgb[2])
    cc.rectangle(0, 0, width, height)
    cc.fill()


"""
    This method draws a single object: a circle
    
    Arguments:
        cc: Cairo.context()
        center_coordinates: tuple (x, y) of center of object
        radius: radius of circle
        rgb: tuple (r,g,b) of object color
        rings: 0 -> no rings, else rings
        rings_rgb: tuple (r,g,b) of rings color
"""
def draw_object(cc, center_coordinates, radius, rgb, rings, rings_rgb):

    center_x = center_coordinates[0]
    center_y = center_coordinates[1]

    # drawing circle with given color
    cc.set_source_rgb(rgb[0], rgb[1], rgb[2])
    cc.arc(center_x, center_y, radius, 0, 2 * math.pi)
    cc.fill()

    if rings != 0:
        # drawing line to represent rings
        cc.move_to(center_x - rings, center_y)
        cc.line_to(center_x + rings, center_y)
        cc.set_source_rgb(rings_rgb[0], rings_rgb[1], rings_rgb[2])
        cc.set_line_width(2)
        cc.stroke()


"""
    This method draws the entire system

    Arguments:
        cc: Cairo.context()
        main_body: dictionary, describes the entire system starting from the main body
        mb_coordinates: tuple (x,y) coordinates of the center of the system
        distance_coefficient: multiplier for distance between same-hierarchy objects (needs to change between planets 
                                and moons.) Could be derived in some way from the radius of the object
        
"""
def draw_system(cc, main_body, mb_coordinates, distance_moltiplicator=300, size_moltiplicator=10):

    # Data needed to draw main body ------------------------------------

    main_body_radius = km_to_px(main_body.radius, size_moltiplicator)
    main_body_rgb = rgb_to_unit(main_body.color)
    main_body_rings = km_to_px(main_body.rings, size_moltiplicator)
    main_body_rings_rgb = rgb_to_unit(main_body.ringscolor)

    # drawing main body
    draw_object(cc, mb_coordinates, main_body_radius, main_body_rgb, main_body_rings, main_body_rings_rgb)

    # Drawing rest of the system ---------------------------------------

    # needed to distance appropriately the different bodies
    last_satellite_x = mb_coordinates[0]
    last_satellite_radius = 0

    # cycling through the main body's satellites: planets
    for satellite in main_body.systems:

        satellite_radius = km_to_px(satellite.radius, size_moltiplicator)
        satellite_rings = km_to_px(satellite.rings, size_moltiplicator)

        satellite_and_rings_radius = satellite_radius
        if satellite_rings != 0:
            satellite_and_rings_radius = satellite_rings

        # this line will put the objects at a distance dependent from the size of the bodies
        planet_x = unscaled_distance(last_satellite_x, last_satellite_radius, satellite_and_rings_radius, distance_moltiplicator)

        # necessary to distance planets
        last_satellite_x = planet_x
        last_satellite_radius = satellite_radius
        if satellite_rings != 0:
            last_satellite_radius = satellite_rings

        # distance_moltiplicator is smaller to keep moons closer to each other
        draw_system(cc, satellite, (planet_x, mb_coordinates[1]), 10, size_moltiplicator)


# helper functions ------------------------------------------------------

def unscaled_distance(last_x, last_radius, this_radius, fixed):        # maybe fixed should be a function of this_radius
    return last_x+last_radius+this_radius+(this_radius*0.3)+fixed

def km_to_px(km, size_moltiplicator):
    # 1737km = 10px
    moon_one_pixel = 1737.0
    return (km / moon_one_pixel * size_moltiplicator)

def rgb_to_unit(vals):
    return (vals[0] / 255.0, vals[1] / 255.0, vals[2] / 255.0)

