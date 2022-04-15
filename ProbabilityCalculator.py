# Heads will be represented by ones in this program
def count_heads(flips):
    return flips.replace("0b", "").count('1')


def map_distribution(num_flips):
    flip_distribution = []
    for i in range(num_flips + 1):
        flip_distribution.append(0.0)
    for flip in range(pow(2, num_flips)):
        num_heads = count_heads(bin(flip))
        flip_distribution[num_heads] = flip_distribution[num_heads] + 1.0
    return flip_distribution


def calc_fair_chance(num_flips, flip_distribution):
    total_possible_flips = pow(2, num_flips)
    fair_distribution = []
    for num_heads in range(num_flips + 1):
        # Since it's balanced chances, we just need to know the amount fitting
        # the relevant metric versus the total amount.
        fair_distribution.append(flip_distribution[num_heads] / total_possible_flips)
    return fair_distribution


# The description of the game tells us the cheaters are using coins with a
# 75% chance of heads
def calc_cheat_chance(num_flips, flip_distribution):
    cheat_distribution = []
    for num_heads in range(num_flips + 1):
        cheat_distribution.append(pow(0.75, num_heads) * pow(.25, (num_flips - num_heads)) *
                                  flip_distribution[num_heads])
    return cheat_distribution


# Equal chance of any given individual being a liar or honest
def calc_cheat_likelihood(honest_distribution, cheat_distribution):
    cheat_chance = []
    for num_heads in range(len(honest_distribution)):
        total_chance = honest_distribution[num_heads] + cheat_distribution[num_heads]
        cheat_chance.append(cheat_distribution[num_heads] / total_chance)
    return cheat_chance


def get_data_for_n_flips(flips):
    distribution = map_distribution(flips)
    honest_distribution = calc_fair_chance(flips, distribution)
    cheat_distribution = calc_cheat_chance(flips, distribution)
    return calc_cheat_likelihood(honest_distribution, cheat_distribution)


def populate_file():
    record_file = open("C:\\Repos\\Detect-Liars\\output.txt", 'w')
    num_flips = 1
    keep_checking = True
    for i in range(20):
        lying_likelihood = get_data_for_n_flips(num_flips)
        for num_heads in range(len(lying_likelihood)):
            output_string = "Num Heads: %d Num Tails: %d Lying Likelihood: %f \n" % (num_heads, num_flips - num_heads,
                                                                                     lying_likelihood[num_heads])
            record_file.write(output_string)
        num_flips = num_flips + 1
    record_file.close()
    return


def main():
    populate_file()
    return


if __name__ == '__main__':
    main()
