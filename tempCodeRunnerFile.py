atures(image):
    feature = np.array(image)
    feature = feature.reshape(1,48,48,1)
    return fea