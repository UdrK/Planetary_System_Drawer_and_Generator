grey = [138, 138, 138]      # color shared by different moons

system = {
    'name': 'Sun',
    'periapsis': 0,
    'apoapsis': 0,
    'radius': 695510,
    'color': [215, 39, 2],
    'satellites': [{
        'name': 'Mercury',
        'periapsis': 46001200,
        'apoapsis': 69816900,
        'radius': 2439,
        'rings': 0,
        'ringscolor': [0, 0, 0],
        'color': [155,157,170],
        'satellites': []
    },{
        'name': 'Venus',
        'periapsis': 107477000,
        'apoapsis': 108939000,
        'radius': 6051,
        'color': [212, 160, 38],
        'rings': 0,
        'ringscolor': [0, 0, 0],
        'satellites': []
    },{
        'name': 'Earth',
        'periapsis': 147095000,
        'apoapsis': 152100000,
        'radius': 6371,
        'color': [33, 134, 207],
        'rings': 0,
        'ringscolor': [0, 0, 0],
        'satellites': [{
            'name': 'Moon',
            'periapsis': 362600,
            'apoapsis': 405400,
            'radius': 1737,
            'color': [82,81,77],
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        }]
    },{
        'name': 'Mars',
        'periapsis': 206700000,
        'apoapsis': 249200000,
        'radius': 3389,
        'color': [199, 100, 0],
        'rings': 0,
        'ringscolor': [0, 0, 0],
        'satellites': [{
            'name': 'Phobos',
            'periapsis': 9234,
            'apoapsis': 9517,
            'radius': 11,
            'color': grey,
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        },{
            'name': 'Deimos',
            'periapsis': 23455,
            'apoapsis': 23470,
            'radius': 6,
            'color': grey,
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        }]
    },{
        'name': 'Jupiter',
        'periapsis': 740000000,
        'apoapsis': 816000000,
        'radius': 69911,
        'color': [230, 198, 139],
        'rings': 0,
        'ringscolor': [0, 0, 0],
        'satellites': [{
            'name': 'Europa',
            'periapsis': 664862,
            'apoapsis': 676938,
            'radius': 1560,
            'color': [187,178,155],
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        },{
            'name': 'Ganymede',
            'periapsis': 1069200,
            'apoapsis': 1071600,
            'radius': 2634,
            'color': [57,39,36],
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        },{
            'name': 'Callisto',
            'periapsis': 1869000,
            'apoapsis': 1897000,
            'radius': 2410,
            'color': [57,39,36],
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        },{
            'name': 'Io',
            'periapsis': 420000,
            'apoapsis': 423400,
            'radius': 1821,
            'color': [133,119,74],
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        }]
    },{
        'name': 'Saturn',
        'periapsis': 1352550000,
        'apoapsis': 1433530000,
        'radius': 58232,
        'color': [245, 231, 207],
        'rings': 136780,
        'ringscolor': [110, 99, 77],
        'satellites': [{
            'name': 'Titan',
            'periapsis': 1186680,
            'apoapsis': 1257060,
            'radius': 2574,
            'color': [236, 201, 101],
            'rings': 0,
            'ringscolor': [0,0,0],
            'satellites': []
        }, {
            'name': 'Iapetus',
            'periapsis': 3458936,
            'apoapsis': 3662704,
            'radius': 734,
            'color': [66, 52, 14],
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        }, {
            'name': 'Rhea',
            'periapsis': 376566,
            'apoapsis': 378226,
            'radius': 763,
            'color': [159, 159, 159],
            'rings': 0,
            'ringscolor': [0,0,0],
            'satellites': []
        }]
    },{
        'name': 'Uranus',
        'periapsis': 2742000000,
        'apoapsis': 3008000000,
        'radius': 25362,
        'color': [207, 245, 248],
        'rings': 0,
        'ringscolor': [0, 0, 0],
        'satellites': [{
            'name': 'Ariel',
            'periapsis': 191129,
            'apoapsis': 190670,
            'radius': 578,
            'color': [115, 97, 95],
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        }, {
            'name': 'Umbriel',
            'periapsis': 264962,
            'apoapsis': 267037,
            'radius': 584,
            'color': [89, 89, 89],
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        }, {
            'name': 'Titania',
            'periapsis': 435820,
            'apoapsis': 436779,
            'radius': 788,
            'color': [193, 181, 169],
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        }, {
            'name': 'Oberon',
            'periapsis': 582683,
            'apoapsis': 584316,
            'radius': 761,
            'color': [177, 146, 115],
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        }]
    },{
        'name': 'Neptune',
        'periapsis': 4460000000,
        'apoapsis': 4540000000,
        'radius': 24622,
        'color': [61,91,231],
        'rings': 0,
        'ringscolor': [0, 0, 0],
        'satellites': [{
            'name': 'Triton',
            'periapsis': 354754,
            'apoapsis': 354765,
            'radius': 1353,
            'color': [210,197,188],
            'rings': 0,
            'ringscolor': [0, 0, 0],
            'satellites': []
        }]
    }]
}