def crosscorr(data_a, data_b, lag=0):
    return data_a.corr(data_b.shift(lag))

def get_correlations(leader, follower, n=10):
    measurements = []

    for i in range(0, 50):
        corr_measure = crosscorr(leader, follower, i)
        measurements.append(corr_measure)
    
    return measurements