
sprite_map = []

with open("sprites.bmp", "rb") as f:
    header = f.read(54)
    color_count = header[50]
    print(f"Ignoring bytes: {header}, we have {color_count} colors")
    colors = []
    for i in range(color_count):
        encoded_color = f.read(4)
        # I R G B
        color = {
            "b": int(encoded_color[0]/255 * 3),
            "g": int(encoded_color[1]/255 * 3),
            "r": int(encoded_color[2]/255 * 3),
            "i": int(encoded_color[3]/255 * 3)
            }
        colors.append(color)
        print(f"Found color i={color['i']} r={color['r']} g={color['g']} b={color['b']}")
    #i=0
    while f.peek(1) != b'':
        pixel_pair = f.read(1)
        #if i%8 == 0:
        #    print("")
        #print(f"{pixel_pair[0]:02x}", end="")
        #i+=1
        pixel_1 = (pixel_pair[0] & 0xf0) >> 4
        pixel_2 = (pixel_pair[0] & 0x0f)
        #print(f"pixel_1={pixel_1}, pixel_2={pixel_2}")
        sprite_map.append(colors[pixel_1])
        sprite_map.append(colors[pixel_2])

#print(sprite_map)

final_sprite_map = []
for pixel in sprite_map[::-1]:
    i_part = pixel['i'] << 6
    r_part = pixel['r'] << 4
    g_part = pixel['g'] << 2
    b_part = pixel['b'] << 0
    #print(f"{i_part:02x}-{pixel['i']} | {r_part:02x}-{pixel['r']} | {g_part:02x}-{pixel['g']} | {b_part:02x}-{pixel['b']}")
    final_sprite_map.append((pixel["i"] << 6) | (pixel["r"] << 4) | (pixel["g"] << 2) | (pixel["b"]))

for i in range(len(final_sprite_map)):
    if i%32 == 0:
        print("")
    print(f"{final_sprite_map[i]:02x} ", end='')

sic_encoded = []
for pixel in final_sprite_map:
    sic_encoded.append(f"\t\tBYTE\t0x{pixel:02x}")

final_sic_string = '\n'.join(sic_encoded)

with open("image_data_sic.asm", "w") as f:
    f.write(final_sic_string)