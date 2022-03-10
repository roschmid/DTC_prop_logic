def get_variables():
    """Function to define all variables that will be used across the program."""

    #Global variables

    global confirmation, negation, options

    confirmation = ["yes", "yes."]
    negation = ["no", "no."]
    options = confirmation + negation

    #Question variables

    enterprise_control = "\nQuestion: Does an enterprise of a Contracting State participate directly or indirectly in the management, control or capital of an enterprise of the other Contracting State?\n\nUser (Yes/No): "
    group_control = "\nQuestion: Do the same persons participate directly or indirectly in the management, control or capital of an enterprise of a Contracting State and an enterprise of the other Contracting State?\n\nUser (Yes/No): "
    arms_length = "\nQuestion: Are conditions made or imposed between the two enterprises in their commercial or financial relations which differ from those which would be made between independent enterprises?\n\nUser (Yes/No): "

    #Check conditions

    if check(enterprise_control):
        if check(arms_length):
            return [True, None, True, True]
        else:
            return [True, None, False, False]
    else:
        if check(group_control):
            if check(arms_length):
                return [False, True, True, True]
            else:
                return [False, True, False, False]
        else:
            return [False, False, None, False]    

def check(item):
    """Function that serves to check whether a certain item is true or false. Returns a boolean"""

    #Get input and lower its caption

    question = input(item).lower()

    #Process input

    while question not in options:
        question = input("\nSorry, I didn't quite get that. Please type your answer in the desired format. \nUser (Yes/No): ")

    if question in confirmation:
        return True
    else:
        return False

def main():

    print("="*70)
    print("""\nFor the purpose of this program, it has been assumed that the taxpayer is a resident of a Contracting State and has obtained an item of income through business carried out in other contracting state pursuant to \
 a Convention for the Avoidance of Double Taxation based on the OECD Model Tax Convention (2017).""")

    conditions = get_variables()    
    true_conditions = ["In accordance with the information provided, the condition established in Article 9(1)(a) of the OECD Model Tax Convention (2017) is met as an enterprise of a Contracting State participates \
directly or indirectly in the management, control or capital of an enterprise of the other Contracting State.",
                      "In accordance with the information provided, the condition established in Article 9(1)(b) of the OECD Model Tax Convention (2017) is met as the same persons participate directly or indirectly \
in the management, control or capital of an enterprise of a Contracting State and an enterprise of the other Contracting State.",
                      "Additionally, the condition established in Article 9(1), second paragraph, is met since the conditions made or imposed between the two enterprises in their commercial or financial relations differ \
from those which would be made between independent enterprises.",
                      """Pursuant to Article 9 of the OECD Model Tax Convention (2017), all conditions set forth in said article are met. Thus, any profits which would, but for those conditions, have accrued \
to one of the enterprises, but, by reason of those conditions, have not so accrued, may be included in the profits of that enterprise and taxed accordingly. Moreover, the other State shall make an appropriate \
adjustment to the amount of the tax charged therein on those profits. In determining such adjustment, due regard shall be had to the other provisions of this Convention and the competent authorities of the \
Contracting States shall if necessary consult each other."""]
    false_conditions = ["In accordance with the information provided, the condition established in Article 9(1)(a) of the OECD Model Tax Convention (2017) is not met as an enterprise of a Contracting State would not participates \
directly or indirectly in the management, control or capital of an enterprise of the other Contracting State.",
                        "In accordance with the information provided, the condition established in Article 9(1)(b) of the OECD Model Tax Convention (2017) is not met as the same persons would not participate directly or indirectly \
in the management, control or capital of an enterprise of a Contracting State and an enterprise of the other Contracting State.",
                        "The condition established in Article 9(1), second paragraph, is not met since the conditions made or imposed between the two enterprises in their commercial or financial relations would not differ \
from those which would be made between independent enterprises.",
                        "Considering the foregoing, the provisions under Article 9 of the OECD Model Tax Convention (2017) would not apply since the conditions aforementioned are not met."]

    for condition in range(0, len(conditions)):
        if conditions[condition] is True:
            print(f"\n[+] {true_conditions[condition]}")
        elif conditions[condition] is False:
            print(f"\n[+] {false_conditions[condition]}")
            
while True:
    main()
