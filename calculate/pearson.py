import math


def pearson(list_one, list_two):
    """
    Accepts paired lists and returns a number between -1 and 1,
    known as Pearson's r, that indicates of how closely correlated
    the two datasets are.

    A score of close to one indicates a high positive correlation.
    That means that X tends to be big when Y is big.

    A score close to negative one indicates a high negative correlation.
    That means X tends to be small when Y is big.

    A score close to zero indicates little correlation between the two
    datasets.

    This script is cobbled together from a variety of sources, linked
    in the sources section below.

    h3. Example usage

        >> import calculate
        >> calculate.pearson([6,5,2], [2,5,6])
        -0.8461538461538467

    h3. A Warning

        Correlation does not equal causation. Just because the two
        datasets are closely related doesn't not mean that one causes
        the other to be the way it is.

    h3. Sources

        http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_\
coefficient
        http://davidmlane.com/hyperstat/A56626.html
        http://www.cmh.edu/stats/definitions/correlation.htm
        http://www.amazon.com/Programming-Collective-Intelligence-Building-\
Applications/dp/0596529325
    """
    if len(list_one) != len(list_two):
        raise ValueError('The two lists you provided do not have the same \
number of entries. Pearson\'s r can only be calculated with paired data.')

    n = len(list_one)

    # Convert all of the data to floats
    list_one = list(map(float, list_one))
    list_two = list(map(float, list_two))

    # Add up the total for each
    sum_one = sum(list_one)
    sum_two = sum(list_two)

    # Sum the squares of each
    sum_of_squares_one = sum([pow(i, 2) for i in list_one])
    sum_of_squares_two = sum([pow(i, 2) for i in list_two])

    # Sum up the product of each element multiplied against its pair
    product_sum = sum([
        item_one * item_two for item_one, item_two in zip(list_one, list_two)
    ])

    # Use the raw materials above to assemble the equation
    pearson_numerator = product_sum - (sum_one * sum_two / n)
    pearson_denominator = math.sqrt(
        (sum_of_squares_one - pow(sum_one, 2) / n) *
        (sum_of_squares_two - pow(sum_two, 2) / n)
    )

    # To avoid avoid dividing by zero,
    # catch it early on and drop out
    if pearson_denominator == 0:
        return 0

    # Divide the equation to return the r value
    return pearson_numerator / pearson_denominator
