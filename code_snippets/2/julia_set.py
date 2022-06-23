from multiprocessing import Pool
import plotly.express as px
import numpy as np

w_width = w_height = 800
n_workers = 1
per_worker = int(w_width / n_workers)
spiltted = [(per_worker * i, per_worker * (i + 1) - 1) for i in range(n_workers)]

def get_julia_set(c, border, left, right):
    print('Started')
    w_width = right - left + 1
    w_height = 800
    
    max_iter = 200
    a, b, y_min, y_max = -1.2 * border, 1.2 * border, -1.2 * border, 1.2 * border
    x_range, y_range = b - a, y_max - y_min

    x_min, x_max = a + left / 800 * x_range, a + right / 800 * x_range
    x_range = x_max - x_min

    julia_set = np.zeros((w_height, w_width))
    for x in range(w_width - 1):
        for y in range(w_height):
            n_iter = 0
            z = complex(x_min + x / w_width * x_range, (y_min + y / w_height * y_range))
            while n_iter < max_iter and z * np.conj(z) < border ** 2:
                z = z * z + c
                n_iter += 1
            
            julia_set[y, x] = n_iter / max_iter
    return julia_set

cs = [
    .35 - .55j,
]

for c in cs:
    border = ( ( 1 + np.sqrt( 1 + 4 * np.abs(c) ) ) / 2 ).real

    # pool = Pool(n_workers)
    # results = pool.map(get_julia_set, )
    # julia_set = ...
    julia_set = get_julia_set(c, border, 0, 799)
    fig = px.imshow(julia_set, title=f'Julia set for c={c}')
    fig.show()
