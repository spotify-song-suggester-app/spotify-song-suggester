import pickle
from sklearn.preprocessing import MinMaxScaler


# load pre-trained models
# pca = pickle.load(open('pca.pkl', 'rb'))
# nn = pickle.load(open('nearest_neighbors.pkl', 'rb'))

pca = pickle.load(open('../pca.pkl', 'rb'))
nn = pickle.load(open('../nearest_neighbors.pkl', 'rb'))


def preprocess(X):
    '''
    Use 'MinMaxScaler' to prep data for PCA

    Args:
        X (object)
    Returns:
        X_scaled (object)
    '''

    scaler = MinMaxScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled


def PCA(X_scaled):
    '''
    Use PCA for dimensionality reduction

    Args:
        X_scaled (object)
    Returns:
        X_reduced (object)
    '''

    X_reduced = pca.transform(X_scaled)

    return X_reduced


def predict(vect):
    '''
    Use k-Nearest Neighbors to predict 10 similar songs

    Args:
        vect (list) of song features
    Returns:
        indices (list) of top 10 similar songs
    '''

    distance, indices = nn.kneighbors(vect)

    return indices[0]
