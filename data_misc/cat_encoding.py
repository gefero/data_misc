class Thermo_Encoding(BaseEstimator, TransformerMixin):
    """
    Thermometer encoding for ordinal variables in pd.Series objects.

    Parameters:
    -----------
    order_labels: dict, with categories of the variable as keys and codes as values

    Values:
    -------
    Returns a pd.DataFrame.

    """

    def __init__(self, order_labels):
        self.order_labels = order_labels

    def transform(self, X, *_):

        x = X.astype('str').map(self.order_labels).astype('int64')
        k = np.arange(0, np.max(x) + 1)
        bars = (k[:-1] < k.reshape(-1, 1)).astype(int)
        X_therm = bars[x]

        col_label = [X.name + '_' + str(lab) +  '_' + str(val) for val, lab in self.order_labels.items()]
        col_label.sort()

        X_therm = pd.DataFrame(X_therm, columns=col_label)
        return X_therm

    def fit(self, *_):
        return self
