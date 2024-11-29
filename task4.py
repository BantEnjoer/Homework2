def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in range(1, 7, 2))

def rgb_to_hex(*rgb_colors):
    return [f"#{r:02x}{g:02x}{b:02x}" for r, g, b in rgb_colors]

def color_averager(*hex_colors):
    rgb_colors = [hex_to_rgb(color) for color in hex_colors]
    averaged_rgb = tuple(
        sum(color[i] for color in rgb_colors) // len(rgb_colors) for i in range(3)
    )
    return rgb_to_hex(averaged_rgb)[0]

