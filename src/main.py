import cairo, math, random, noise
from PIL import Image
from system_drawer import *
from solar_system import solar_system

def apply_noise(filename, noise_type='perlin'):
    if noise_type == 'perlin':
        pil_image = Image.open(filename)
        pixels = pil_image.load()
        for i in range(pil_image.size[0]):
            for j in range(pil_image.size[1]):
                if random.randint(0, 99) < 10:
                    r,g,b = pixels[i,j]
                    noiz = noise.pnoise2(i/100.0, j/100.0, octaves=6, persistence=.5, lacunarity=2.0, repeatx=1024, repeaty=1024, base=0)
                    pixels[i, j] = (int(r*noiz), int(g*noiz), int(b*noiz))
        pil_image.save(filename)

def main():
    print('Starting')
    width = 6144
    height = 2048
    filename = '..\TEST2.png'

    ims = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    cc = cairo.Context(ims)

    draw_background(cc, width, height, (.15, .15, .15))
    draw_system(cc, solar_system, (0, height/2))

    # print('Applying noise')
    # apply_noise(filename)

    print('Saving file')
    ims.write_to_png(filename)

if __name__ == "__main__":
    main()