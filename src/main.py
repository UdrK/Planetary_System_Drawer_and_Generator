import cairo, random, noise
from PIL import Image
from system_drawer import *
from systems.v1400_centauri import v1400_centauri

def apply_noise_save(filename, noise_type='perlin'):
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
    filename = '..\TEST5.png'

    ims = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    cc = cairo.Context(ims)

    draw_background(cc, width, height, (.15, .15, .15))
    draw_system(cc, v1400_centauri, (0, height/2), size_moltiplicator=0.1)

    print('Saving file')
    ims.write_to_png(filename)

    #print('Applying noise')
    #apply_noise_save(filename)

if __name__ == "__main__":
    main()