import numpy as np
import matplotlib.pyplot as plt
from scipy import spatial
from timeit import default_timer as timer

plot_runtime = True

if plot_runtime:
    n1 = 4
    n2 = 7
    stats = []
    stats_settings = []
    for i in range(n1):
        n = 10**(i+2)
        for j in range(n2):
            c = 2**(j+2)

            A = np.random.randint(101, size=(n, c))
            pt = np.random.randint(101, size=c)
            start = timer()
            distance, index = spatial.cKDTree(A).query(pt, k=5)
            end = timer()
            t = end - start # time in seconds
            stats.append(t)
            stats_settings.append([n, c])
            print('Elapsed time for', n,'users and', c, 'categories is ', t)

    print(stats_settings)
    fig = plt.figure()
    ax = plt.gca()
    ax.set_xlabel('Settings [#users, #categories]')
    ax.set_ylabel('Time [s]')
    ax.set_title('Runtime analysis')

    plt.semilogy(range(len(stats)), stats)
    plt.xticks(np.arange(n1*n2), stats_settings, rotation=90)
    plt.show()
    fig.savefig('runtime_semilog.png', bbox_inches='tight')
    plt.bar(range(len(stats)), stats)
    plt.show()
    fig.savefig('runtime_bar.png', bbox_inches='tight')

# small example
n = 1000
c = 5
A = np.random.randint(101, size=(n, c))

pt = np.random.randint(101, size=c)

distance,index = spatial.KDTree(A).query(pt, k=5)
distance = 100 - distance/c

print('people skills: \n', A)
print('skills needed: \n', pt)
print('index: \n', index)
print('match percentage: \n', distance)


