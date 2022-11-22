import random
import numpy
from ortools.linear_solver import pywraplp
import matplotlib.pyplot as plt


def show_bins(numberOfBins, groupValues, idealValue):
    fig, ax = plt.subplots(1, 1, figsize=(16, 6))
    # Plots
    ax.bar(x=range(int(numberOfBins)), height=groupValues, color="#408090")
    ax.hlines(idealValue, -1, numberOfBins, colors="#995050", linewidths=5)
    # Style
    ax.set_xlim(-1, numberOfBins)
    ax.set_ylim(0, max(groupValues) + 2)
    p = list(range(0, int(numberOfBins)))
    # ax.set_xticklabels(list(range(0, int(numberOfBins))))

    ax.set_xlabel("Groups")
    ax.set_ylabel("Weight/Value")

    plt.show()


def create_data_model():
    """Create the data for the example."""
    data = {}
    # weights = [48, 30, 19, 36, 36, 27, 42, 42, 36, 24, 30]
    weights = random.sample(range(0, 100), random.randint(0, 50))
    data['weights'] = weights
    data['items'] = list(range(len(weights)))
    data['bins'] = data['items']
    data['bin_capacity'] = 100
    return data


def main():
    data = create_data_model()

    # Create the mip solver with the SCIP backend.
    solver = pywraplp.Solver.CreateSolver('SCIP')

    if not solver:
        return

    # Variables
    # x[i, j] = 1 if item i is packed in bin j.
    x = {}
    for i in data['items']:
        for j in data['bins']:
            x[(i, j)] = solver.IntVar(0, 1, 'x_%i_%i' % (i, j))

    # y[j] = 1 if bin j is used.
    y = {}
    for j in data['bins']:
        y[j] = solver.IntVar(0, 1, 'y[%i]' % j)

    # Constraints
    # Each item must be in exactly one bin.
    for i in data['items']:
        solver.Add(sum(x[i, j] for j in data['bins']) == 1)

    # The amount packed in each bin cannot exceed its capacity.
    for j in data['bins']:
        solver.Add(
            sum(x[(i, j)] * data['weights'][i] for i in data['items']) <= y[j] *
            data['bin_capacity'])

    # Objective: minimize the number of bins used.
    solver.Minimize(solver.Sum([y[j] for j in data['bins']]))
    status = solver.Solve()

    kanta = []

    if status == pywraplp.Solver.OPTIMAL:
        num_bins = 0.
        for j in data['bins']:
            if y[j].solution_value() == 1:
                bin_items = []
                bin_weight = 0
                for i in data['items']:
                    if x[i, j].solution_value() > 0:
                        bin_items.append(i)
                        bin_weight += data['weights'][i]
                kanta.append(bin_weight)

                if bin_weight > 0:
                    num_bins += 1
                    print('Bin number', j)
                    print('  Items packed:', bin_items)
                    print('  Total weight:', bin_weight)
                    print()
        print()
        print('Number of bins used:', num_bins)
        print('Time = ', solver.WallTime(), ' milliseconds')
    else:
        print('The problem does not have an optimal solution.')
    print(f'Prosjecna popunjenost:', numpy.average(kanta)/data['bin_capacity'])
    show_bins(num_bins, kanta, numpy.average(kanta))


if __name__ == '__main__':
    main()
