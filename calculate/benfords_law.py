from __future__ import print_function
import math
import calculate


def benfords_law(number_list, method='first_digit', verbose=True):
    """
    Accepts a list of numbers and applies a quick-and-dirty run
    against Benford's Law.

    Benford's Law makes statements about the occurance of leading digits in a
    dataset. It claims that a leading digit of 1 will occur about 30 percent
    of the time, and each number after it a little bit less, with the number
    9 occuring the least.

    Datasets that greatly vary from the law are sometimes suspected of fraud.

    The function returns the Pearson correlation coefficient, also known as
    Pearson's r,  which reports how closely the two datasets are related.

    This function also includes a variation on the classic Benford analysis
    popularized by blogger Nate Silver, who conducted an analysis of the final
    digits of polling data. To use Silver's variation, provide the keyward
    argument `method` with the value 'last_digit'.

    To prevent the function from printing, set the optional keyword argument
    `verbose` to False.

    This function is based upon code from a variety of sources around the web,
    but owes a particular debt to the work of Christian S. Perone.

    h3. Example usage

        >> import calculate
        >> calculate.benfords_law([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        BENFORD'S LAW: FIRST_DIGIT

        Pearson's R: 0.86412304649

        | Number | Count | Expected Percentage | Actual Percentage |
        ------------------------------------------------------------
        | 1      | 2     | 30.1029995664       | 20.0              |
        | 2      | 1     | 17.6091259056       | 10.0              |
        | 3      | 1     | 12.4938736608       | 10.0              |
        | 4      | 1     | 9.69100130081       | 10.0              |
        | 5      | 1     | 7.91812460476       | 10.0              |
        | 6      | 1     | 6.69467896306       | 10.0              |
        | 7      | 1     | 5.79919469777       | 10.0              |
        | 8      | 1     | 5.11525224474       | 10.0              |
        | 9      | 1     | 4.57574905607       | 10.0              |

        >> calculate.benfords_law([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            verbose=False)
        -0.863801937698704

    h3. A Warning

    Not all datasets should be expected to conform to Benford's rules.
    I lifted the following guidance from an academic paper linked
    below.

    Durtschi, Hillison, and Pacini (2004) said Benford "compliance"
    should be expected in the following circumstances:

        1. Numbers that result from mathematical combination of numbers

        2. Transaction-level data (e.g., disbursements, sales)

        3. Large datasets

        4. Mean is greater than median and skew is positive

    And not to expect Benford distributions when:

        1. Numbers are assigned (e.g., check numbers, invoice numbers)

        2. Numbers influence by human thought (e.g. $1.99)

        3. Accounts with a large number of firm-specific numbers

        4. Accounts with a built-in minimum or maximum

        5. Where no transaction is recorded.

    h3. Sources

        "Benford's Law":http://en.wikipedia.org/wiki/Benford%27s_law
        "Applying Benford's Law to CAR":http://www.chasedavis.com/2008/sep/\
28/applying-benfords-law-car/
        "Breaking the (Benford) Law: Statistical Fraud Detection in Campaign \
Finance (pdf)":http://cho.pol.uiuc.edu/wendy/papers/tas.pdf
        "Benford's Law meets Python and Apple Stock Prices":http://pyevolve.\
sourceforge.net/wordpress/?p=457
        "Strategic Vision Polls Exhibit Unusual Patterns, Possibly Indicating \
Fraud":http://www.fivethirtyeight.com/2009/09/strategic-vision-polls-\
exhibit-unusual.html
        "Nate Silver: pollster may be fraud":http://blogs.tampabay.com/buzz/\
2009/09/nate-silver-pollster-may-be-fraud.html
    """
    # Select the appropriate retrieval method
    if method not in ['last_digit', 'first_digit']:
        raise ValueError('The method you\'ve requested is not supported.')

    def _get_first_digit(number):
        return int(str(number)[0])

    def _get_last_digit(number):
        return int(str(number)[-1])

    method_name = '_get_%s' % method
    method_obj = locals()[method_name]

    # Set the typical distributions we expect to find
    typical_distributions = {
        'first_digit': {},
        'last_digit': {}
    }
    for number in range(1, 10):
        log10 = math.log10(1 + 1 / float(number)) * 100.0
        typical_distributions['first_digit'].update({number: log10})

    typical_distributions['last_digit'].update({
        0: 10.0, 1: 10.0, 2: 10.0, 3: 10.0, 4: 10.0,
        5: 10.0, 6: 10.0, 7: 10.0, 8: 10.0, 9: 10.0,
    })

    # Fetch the digits we want to analyze
    digit_list = []
    for number in number_list:
        digit = method_obj(number)
        digit_list.append(digit)

    # Loop through the data set and grab all the applicable numbers
    results = []
    for number in range(0, 10):
        count = digit_list.count(number)
        try:
            expected_percentage = typical_distributions[method][number]
        except KeyError:
            continue
        actual_percentage = count / float(len(digit_list)) * 100.0
        results.append([number, count, expected_percentage, actual_percentage])

    # Run the two percentage figures through
    # Pearson's correlation coefficient to
    # see how closely related they are.
    list_one = [i[2] for i in results]
    list_two = typical_distributions[method]
    pearsons_r = calculate.pearson(list_one, list_two)

    # If the user has asked for verbosity,
    # print out this cutsey table with all
    # of the data.
    if verbose:
        from calculate import ptable
        # Convert results to strings
        results = [list(map(str, i)) for i in results]
        # Print everything out using our pretty table module
        labels = [
            'Number', 'Count', 'Expected Percentage', 'Actual Percentage'
        ]
        print("BENFORD'S LAW: %s" % method.upper().replace('_', ' '))
        print("")
        print("Pearson's r: %s" % (pearsons_r))
        print("")
        print(ptable.indent(
            [labels] + results,
            hasHeader=True,
            separateRows=False,
            prefix='| ', postfix=' |',
        ))

    return pearsons_r
