def get_true_quantile(r_true, quantile=0.5):
    i = np.arange(len(r_true))
    c = np.cumsum(r_true)
    q = np.searchsorted(c, quantile*c[-1])
    return np.where(c[q]/c[-1] == quantile, 0.5 * (i[q] + i[q+1]), i[q])