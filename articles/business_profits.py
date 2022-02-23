def get_variables():
    """Function to define all variables that will be used across the program."""

    #Global variables

    global confirmation, negation, options

    confirmation = ["Yes", "yes", "Yes.", "yes.", "YES"]
    negation = ["No", "no", "No.", "no.", "NO"]
    options = confirmation + negation

    #Question variables

    other_income = "\nQuestion: Is this item of income dealt with separately in other Articles (different from Article 7) of the Convention for the Avoidance of Double Taxation?\n\nUser (Yes/No): "
    permanent_establishment_exists = "\nQuestion: Does the enterprise carry on business in the other Contracting State through a permanent establishment situated therein?\n\nUser (Yes/No): "
    income_attributed = "\nQuestion: Are the items of income attributed to the permanent establishment in accordance with Article 7(2) OECD MTC (2017)?\n\nUser (Yes/No): "
    taxed_accordingly = "\nQuestion: Is the permanent establishment taxed accordingly for the profits that have been attributed?\n\nUser (Yes/No): "

    return other_income, permanent_establishment_exists, income_attributed, taxed_accordingly
    

def check(item):
    """Function that serves to check whether a certain item is true or false. Returns a boolean"""

    #Get input

    question = input(item)

    #Process input

    while question not in options:
        question = input("\nSorry, I didn't quite get that. Please type your answer in the desired format. \nUser (Yes/No): ")

    if question in confirmation:
        return True
    else:
        return False


def main():

    print("="*70)
    print("""\nFor the purpose of this program, it has been assumed that the taxpayer is a resident of a Contracting State and has obtained an item of income pursuant to\
 a Convention for the Avoidance of Double Taxation based on the OECD Model Tax Convention (2017).""")

    other_income, permanent_establishment_exists, income_attributed, taxed_accordingly = get_variables()

    if not check(other_income):
        if check(permanent_establishment_exists):
            if check(income_attributed):
                if check(taxed_accordingly):
                    print(f"""\nConclusion:

[+] In accordance with the information provided, the taxpayer obtains income not dealt with in a separate article of the Convention for the Avoidance of Double Taxation.
\n[+] Pursuant to Article 7(2) and 7(3) of the OECD MTC (2017), the enterprise carries on its activities through a permanent establishment in the State of Source.
\n[+] Hence, pursuant to Article 7(1) of the OECD MTC (2017) profits that are attributable to the permanent establishment may be taxed in the State of Source.
\n[+] Profits attributable to the permanent establishment are the profits it might be expected to make, \
in particular in its dealings with other parts of the enterprise, if it were a separate and independent enterprise engaged in the same or similar activities under the same or similar conditions, \
taking into account the functions performed, assets used and risks assumed by the enterprise through the permanent establishment.
\n[+] Moreover, since a Contracting State has adjusted the profits that are attributable to the permanent establishment and has taxed accordingly, the other State shall, to the extent necessary to\
eliminate double taxation on these profits, make an appropriate adjustment to the amount of the tax charged on those profits.""")
                    #END
                else:
                    print("""\nConclusion:

[+] In accordance with the information provided, the taxpayer obtains income not dealt with in a separate article of the Convention for the Avoidance of Double Taxation.
\n[+] Pursuant to Article 7(2) of the OECD MTC (2017), the enterprise carries on its activities through a permanent establishment in the State of Source.
\n[+] Hence, profits attributable in each Contracting State to the permanent establishment are the profits it might be expected to make, \
in particular in its dealings with other parts of the enterprise, if it were a separate and independent enterprise engaged in the same or similar activities under the same or similar conditions, \
taking into account the functions performed, assets used and risks assumed by the enterprise through the permanent establishment.""")
                    #END
            else:
                print("""\nConclusion:

[+] In accordance with the information provided, while the taxpayer carries on its activities through a permanent establishment, there are no profits \
to be attributed to the permanent establishment.

[+] Pursuant to Article 7(1) of the OECD MTC (2017), profits of the enterprise shall only be taxable only in the state in which it is a resident.""")
                #END
        else:
            print("""\nConclusion:

[+] In accordance with the information provided, the taxpayer obtains income not dealt with in a separate article of the \
Convention for the Avoidance of Double Taxation and does not carry on its activities through a permanent establishment.\n

[+] Pursuant to Article 7(1) of the OECD MTC (2017), profits of the enterprise shall only be taxable only in the state in which it is a resident.""")
            #END
    else:
        print("""\nConclusion:

[+] Article 7 is not applicable to the present case pursuant to Article 7(4) of the OECD MTC (2017), since the item of income is dealt with in a separate article of the Convention for the Avoidance of Double Taxation.""")
        #END

while True:
    main()
