import matplotlib.pyplot as plt
import random
import seaborn as sns


def monty_hall():
    """This function recreates the Monty Hall Paradox."""
    # This section sets up the situation by randomly choosing the door behind which the prize will be.
    all_doors = [1, 2, 3]
    prize_door = random.choice(all_doors)
    other_doors = [door for door in all_doors if door != prize_door]
    # From here on, we have the interaction between contestant and host.
    chosen_door = random.choice(all_doors)
    if chosen_door == prize_door:
        opened_door = random.choice(other_doors)
    else:
        opened_door = [door for door in other_doors if door != chosen_door][0]

    remaining_door = [door for door in all_doors if door not in [chosen_door, opened_door]][0]

    return remaining_door == prize_door


# Here, we sample multiple runs of the Paradox so that we will have statistically significant data.
num_of_runs = 10000

sample = [monty_hall() for _ in range(num_of_runs)]
success_rate = sum(sample)/num_of_runs

print(f"{success_rate*100:.2f}%")

# ax = sns.barplot(x=['Fracasso', 'Sucesso'],
#                  y=[1-success_rate, success_rate],
#                  color='#3498db',
#                  width=0.6)
#
# ax.set_facecolor('#F5F5F5')
# ax.set_ylim(0, 1)
#
# plt.savefig('Monty Hall Plot')
