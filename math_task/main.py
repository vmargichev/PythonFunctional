def get_median_font_size(font_sizes):
    sorted_fonts = sorted(font_sizes)
    len_fonts = len(sorted_fonts)
    if len_fonts == 0:
        return None
    elif len_fonts % 2 == 0:
        return (sorted_fonts[len_fonts // 2 - 1]  + sorted_fonts[(len_fonts // 2)]) / 2
    else:
        return sorted_fonts[len_fonts // 2]
