#!/usr/bin/python
__author__ = 'xors'

import sys, getopt

def numeric_compare(x, y):
    return x['sq'] - y['sq']

def get_rgb_from_hex(hex_code):
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return r, g, b

def get_hex_from_rgb(r, g, b):
    def fixHexCode(hexCode):
        if len(hexCode) < 4:
            return hexCode+'0'
        return hexCode

    hex_r = fixHexCode(str(hex(r)))
    hex_g = fixHexCode(str(hex(g)))
    hex_b = fixHexCode(str(hex(b)))
    return hex_r, hex_g, hex_b

def usage():
    print 'pick_closest.py -p <pallete_file> -c <color_hex_code>'
    sys.exit(2)

def main(argv):
    pallete_file = ''
    color_hex_code = ''
    if len(argv) != 4:
        usage()
    try:
        opts, args = getopt.getopt(argv,"hp:c:",["palette_file=","color_hex_code="])
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-p", "--palette"):
            pallete_file = arg
        elif opt in ("-c", "--color"):
            color_hex_code = arg

    f = open(pallete_file, 'r')
    palette = []
    for line in f.readlines():
        mas = line.strip().split('#')
        hex_code = mas[1]
        r, g, b = get_rgb_from_hex(hex_code)
        palette.append({
            'r': r,
            'g': g,
            'b': b,
        })
    f.close()

    init_r, init_g, init_b = get_rgb_from_hex(color_hex_code)

    min_sq = []
    for color in palette:
        min_sq.append({
            'sq': (int(init_r) - color['r'])**2 + (int(init_g) - color['g'])**2 + (int(init_b) - color['b'])**2,
            'color': color
        })

    res = sorted(min_sq, cmp=numeric_compare)

    hex_r, hex_g, hex_b = get_hex_from_rgb(res[0]['color']['r'], res[   0]['color']['g'], res[0]['color']['b'])
    print hex_r.replace('0x', '') + hex_g.replace('0x', '') + hex_b.replace('0x', '')


if __name__ == '__main__':
    main(sys.argv[1:])
