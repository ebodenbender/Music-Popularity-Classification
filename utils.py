"""
Programmed by Emily Bodenbender
8/22/23

Description: Utilities for data science tasks.
"""

def compute_slope_intercept(x, y):
    meanx = np.mean(x)
    meany = np.mean(y)

    num = sum([(x[i] - meanx) * (y[i] - meany) for i in range(len(x))])
    denom = sum([(x[i] - meanx) ** 2 for i in range(len(x))])
    m = num / denom
    # y = mx + b -> b = y - mx
    b = meany - m * meanx
    return m, b

def get_frequencies(col):
    col.sort() # inplace
    # parallel lists
    values = []
    counts = []
    for value in col:
        if value in values: # seen it before
            counts[-1] += 1 # okay because sorted
        else: # haven't seen it before
            values.append(value)
            counts.append(1)
    
    return values, counts