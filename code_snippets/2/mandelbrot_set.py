import numpy as np
import plotly.express as px
np.warnings.filterwarnings("ignore")

def get_mandelbrot_set():
    max_iter = 200
    w_width, w_height = 800, 800
    x_min, x_max, y_min, y_max = -3, 5, -1.5, 1.5
    x_range, y_range = x_max - x_min, y_max - y_min

    mandelbrot_set = []
    for x in range(w_width):
        for y in range(w_height):
            pixel_x = x_min + x / w_width * x_range
            pixel_y = y_min + y / w_height * y_range

            n_iter = 1
            z = 0
            c = complex(pixel_x, pixel_y)
            while n_iter < max_iter and z * np.conj(z) <= 4:
                z = z * z + c
                n_iter += 1

            if n_iter == max_iter:
                mandelbrot_set.append((pixel_x, pixel_y))
    return mandelbrot_set

mandelbrot_set = get_mandelbrot_set()
fig = px.scatter(
    x=list(map(lambda x: x[0], mandelbrot_set)),
    y=list(map(lambda y: y[1], mandelbrot_set))
)
fig.show()
