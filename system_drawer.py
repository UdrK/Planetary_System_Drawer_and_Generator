import cairo, math, random, noise
from PIL import Image
import solar_system

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
        
"""
def draw_system(cc, main_body, mb_coordinates):

    # Data needed to draw main body ------------------------------------

    main_body_radius = km_to_px(main_body['radius'])

    # color
    main_body_rgb = (rgb_to_unit(main_body['color'][0]),
                     rgb_to_unit(main_body['color'][1]),
                     rgb_to_unit(main_body['color'][2]))

    # main body doesn't have rings:
    rings = 0
    rings_rgb = (0, 0, 0)

    # ------------------------------------------------------------------

    # drawing main body
    draw_object(cc, mb_coordinates, main_body_radius, main_body_rgb, rings, rings_rgb)


    # Drawing rest of the system ---------------------------------------

    # needed to distance appropriately the different bodies
    last_planet_x = 0
    last_planet_radius = 0

    # cycling through the main body's satellites: planets
    for planet in main_body['satellites']:

        # this line necessary if you want scaled distances based on the system's description
        planet_x = km_to_px(planet['periapsis'])

        planet_radius = km_to_px(planet['radius'])
        planet_rings = km_to_px(planet['rings'])
        planet_rgb = (rgb_to_unit(planet['color'][0]),
                      rgb_to_unit(planet['color'][1]),
                      rgb_to_unit(planet['color'][2]))

        planet_rings_rgb = (rgb_to_unit(planet['ringscolor'][0]),
                            rgb_to_unit(planet['ringscolor'][1]),
                            rgb_to_unit(planet['ringscolor'][2]))

        planet_and_rings_radius = planet_radius
        if planet_rings != 0:
            planet_and_rings_radius = planet_rings

        # this line will put the objects at a distance dependent from the size of the bodies
        planet_x = unscaled_distance(last_planet_x, last_planet_radius, planet_and_rings_radius, 300)

        # drawing object
        draw_object(cc, (planet_x, mb_coordinates[1]), planet_radius, planet_rgb, planet_rings, planet_rings_rgb)

        # necessary to distance planets
        last_planet_x = planet_x
        last_planet_radius = planet_radius
        if planet_rings != 0:
            last_planet_radius = planet_rings

        # drawing moons
        last_moon_x = planet_x
        last_moon_radius = 0
        for moon in planet['satellites']:

            # this line necessary if you want scaled distances based on the system's description
            moon_x = km_to_px(moon['periapsis'])
            moon_radius = km_to_px(moon['radius'])

            moon_rings = km_to_px(moon['rings'])

            moon_rgb = (rgb_to_unit(moon['color'][0]),
                        rgb_to_unit(moon['color'][1]),
                        rgb_to_unit(moon['color'][2]))

            moon_rings_rgb = (rgb_to_unit(moon['ringscolor'][0]),
                              rgb_to_unit(moon['ringscolor'][1]),
                              rgb_to_unit(moon['ringscolor'][2]))

            # unscaled distance
            moon_x = unscaled_distance(last_moon_x, last_moon_radius, moon_radius, 10)

            draw_object(cc, (moon_x, mb_coordinates[1]), moon_radius, moon_rgb,
                        moon_rings, moon_rings_rgb)

            last_moon_x = moon_x
            last_moon_radius = moon_radius
            if moon_rings != 0:
                last_moon_radius = moon_rings

# Scale stuff

def unscaled_distance(last_x, last_radius, this_radius, fixed):
    return last_x+last_radius+this_radius+(this_radius*0.3)+fixed

def km_to_px(km):
    # 1737km = 10px
    moon_one_pixel = 1737.0
    return (km/moon_one_pixel*10)

def rgb_to_unit(val):
    return val/255.0


def main():
    # 1920 1080
    print('Starting')
    width = 6144
    height = 2048
    filename = 'TEST2.png'

    ims = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    cc = cairo.Context(ims)

    draw_background(cc, width, height, (.15, .15, .15))

    system = solar_system.system
    system['periapsis'] = 0
    draw_system(cc, system, (0, height/2))

    print('Almost there')

    ims.write_to_png(filename)
    """
    noizy = True
    # perlin noise
    if noizy:
        pil_image = Image.open(filename)
        pixels = pil_image.load()

        for i in range(pil_image.size[0]):
            for j in range(pil_image.size[1]):
                if random.randint(0, 99) < 10:
                    r,g,b = pixels[i,j]
                    noiz = noise.pnoise2(i/100.0, j/100.0, octaves=6, persistence=.5, lacunarity=2.0, repeatx=1024, repeaty=1024, base=0)
                    pixels[i, j] = (int(r*noiz), int(g*noiz), int(b*noiz))

        print('Here we go')
        pil_image.save(filename)
    """
if __name__ == "__main__":
    main()
