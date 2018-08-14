def rgb(r, g, b):
    if (r < 0 or g < 0 or b < 0 or r > 255 or g > 255 or b > 255):
        res = "Invalid argument"
    else:
        hex = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f']
        r16 = hex[int(r) // 16] + hex[int(r) % 16]
        g16 = hex[int(g) // 16] + hex[int(g) % 16]
        b16 = hex[int(b) // 16] + hex[int(b) % 16]
        res = "#" + r16 + g16 + b16
    return res
