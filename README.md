# Planetary System Drawer and Generator
This project consists mainly of 2 parts:

## A planetary system drawer
The drawer uses pycairo to draw a png based on the planetary system information.

The drawing consists of a 2d representation of the planetary system.

PIL can be used to apply noise to the image to make it have texture.

The method that draws the system is recursive since a system is defined as an object and a list of systems.

## A few, real life planetary systems

Including of course:
* The solar system

But also some extra-solar systems:
* Kepler-11
* Trappist-1
* V1400 Centauri

## A planetary system generator

As of now, i've implemented 2 generators:
* Random generator: has limits as min and max sizes, and limited set of colors, but everything else is random. Produces unpleasant color palettes.
* Solar system like generator: produces a system with 4 small bodies, 2 large bodies, 2 mediums bodies, and several smaller bodies. Uses a set of predetermined colors that play nice with the star which is random. As a few bugs, may crash.

## Example

The solar system, objects radii to scale, distances __not__ to scale

![TEST4](https://user-images.githubusercontent.com/26527575/92143337-700f5b80-ee15-11ea-93e6-0b078e480021.png)
