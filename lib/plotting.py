import matplotlib.pyplot as plt


def plot_correlations(correlations):
    plt.plot(list(range(0, len(correlations))), correlations)
    plt.xlabel("Lag in days")
    plt.ylabel("correlation coefficient")
    plt.title("Correlations & Lag")
    plt.show


def save_correlation_plot(destination, leader, follower, correlations):
    plt.plot(list(range(0, len(correlations))), correlations)
    plt.xlabel("Lag in days")
    plt.ylabel("correlation coefficient")
    plt.title(f'{leader} leading {follower}')
    plt.savefig(f'{destination}/{leader}-{follower}.png')
