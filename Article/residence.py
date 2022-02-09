from transformers import pipeline

def input_extraction(task):
    """Function that gets from the user the desired input that will be sent to
    the model and extracts relevant information."""

    print("="*100)
    context = input("\nPlease provide the case facts (subject name, individual or entity, residence, permanent home, CIV, habitual abode and nationality).\n\nUser: ")
    print("="*100)

    #Preparing the questions for extraction

    name_extraction = "What is the name of the subject?"
    subject_extraction = "Is he/she an individual or an entity?"
    residence_extraction = "Where is he/she a resident?"
    permanent_home_exist_extraction = "Does he/she have a permanent home?"
    permanent_home_extraction = "Where does he/she have a permanent home?"
    civ_extraction = "Where is his/her center of vital interests?"
    habitual_abode_extraction = "Where does he/she have its habitual abode?"
    nationality_extraction = "Where does he/her have nationality or citizenship?"

    #Process user input

    name = task(question=name_extraction, context=context)["answer"]
    subject = task(question=subject_extraction, context=context)["answer"]
    residence = task(question=residence_extraction, context=context)["answer"]
    permanent_home_exist = task(question=permanent_home_exist_extraction, context=context)["answer"]
    permanent_home = task(question=permanent_home_extraction, context=context)["answer"]
    civ = task(question=civ_extraction, context=context)["answer"]
    habitual_abode = task(question=habitual_abode_extraction, context=context)["answer"]
    nationality = task(question=nationality_extraction, context=context)["answer"]

    return name, subject, residence, permanent_home_exist, permanent_home, civ, habitual_abode, nationality

def single_or_double_residence(name, residence):
    """Function that receives as input the name of the subject as well as its residence to
    determine which paragraph of Article 4 OECD MTC (2017) applies."""

    double_residence = False
    single_residence = False

    if " and " in residence:
        double_residence = True
    else:
        single_residence = True

    return double_residence, single_residence

def single_residence_pipeline(name, residence):
    """Function that provides pipeline when a subject has only one residence."""

    exception_rule = input(f"\n{name} is a resident of {residence}. \
However, is {name} liable to tax in {residence} in respect ONLY of income from sources in {residence} or capital situated therein?\n\nUser (Yes/No): ")

    if exception_rule == "Yes":
        print(f"\n{name} cannot be a resident of {residence} for treaty purposes subject to Article 4(1), second paragraph.")
    else:
        print(f"\n{name} is a resident of {residence} for treaty purpsoes subject to Article 4(1).")

def entity_residence_pipeline(name, subject, residence):
    """Pipeline for entities with more than one residence."""

    #Get residences

    residences = residence.split(" and ")

    print(f"\n{name} is not an individual and is resident both in {residences[0]} and {residences[1]}.")

    #Get MAP

    mutual_agreement_procedure = input(f"\nPlease indicate whether the tax authorities determined by mutual agreement procedure whether {name} is a resident for treaty purposes.\n\nUser ({residences[0]}, {residences[1]} or None): ")

    if mutual_agreement_procedure != "None":
        print(f"\n{name} is a resident for treaty purposes of {mutual_agreement_procedure} pursuant to Article 4(3).")
    else:
        print(f"\n{name} shall not be entitled to any relief or exemption from tax provided by the tax convention pursuant to Article 4(3), second sentence.")

def individual_residence_pipeline(name, subject, residence, permanent_home_exist, permanent_home, civ, habitual_abode, nationality):
    """Pipeline for individuals with more than one residence."""

    #Opening variables

    counter = 0
    
    homes = permanent_home.split(" and ")
    civs = civ.split(" and ")
    habitual_abodes = habitual_abode.split(" and ")
    nationalities = nationality.split(" and ")

    #Get residences

    residences = residence.split(" and ")

    print(f"\n{name} is an individual and is resident both in {residences[0]} and {residences[1]}. The tiebreaker rules from Article 4(2) are applicable.")

    #Tiebreaker rules

    if len(homes) > 1 and permanent_home_exist != "no":
        counter += 1
        print(f"\n({counter}) According to the information provided, {name} has a permanent home both in {residences[0]} and {residences[1]}.")
        print("Hence, pursuant to Article 4(2)(a), it must be determined where his center of vital interests lie.")
        if len(civs) > 1:
            counter += 1
            print(f"\n({counter}) According to the information provided, it cannot be determined where {name} has his center of vital interests.")
            print("Hence, pursuant to Article 4(2)(b), it must be determined whether the subject has an habitual abode.")
            if len(habitual_abodes) > 1 or len(habitual_abodes) == 0:
                counter += 1
                print(f"\n({counter}) According to the information provided, {name} has either an habitual abode both in {residences[0]} and {residences[1]} or neither of them.")
                print(f"Hence, pursuant to Article 4(2)(c), {name} shall be deemed to be a resident only of the State in which he is a national.")
                if len(nationalities) > 1:
                    counter += 1
                    print(f"\n({counter}) According to the information provided, {name} is a national of both {residences[0]} and {residences[1]}.")
                    print(f"Hence, pursuant to Article 4(2)(d), {name} shall be deemed to be a resident only of the State that is settled by a mutual agreement procedure.")
                    #END
                elif len(nationalities) == 1:
                    counter += 1
                    print(f"\n({counter}) According to the information provided, {name} is a national only of {nationalities[0]}.")
                    print(f"Hence, pursuant to Article 4(2)(c), {name} shall be deemed to be a resident of {nationalities[0]}.")
                    #END
                else:
                    counter += 1
                    print(f"\n({counter}) According to the information provided, {name} is a national of neither {residences[0]} and {residences[1]}.")
                    print(f"Hence, pursuant to Article 4(2)(d), {name} shall be deemed to be a resident only of the State that is settled by a mutual agreement procedure.")
                    #END
            elif len(habitual_abodes) == 1:
                counter += 1
                print(f"\n({counter}) According to the information provided, {name} has his/her habitual abode only in {habitual_abodes[0]}.")
                print(f"Hence, pursuant to Article 4(2)(b), {name} shall be considered to be a resident of {habitual_abodes[0]}.")
                #END
        elif len(civs) == 1:
            counter += 1
            print(f"\n({counter}) According to the information provided, {name} has his/her center of vital interests only in {civs[0]}.")
            print(f"Hence, pursuant to Article 4(2)(a), {name} shall be considered to be a resident of {civs[0]}.")
            #END
    elif len(homes) == 1 and permanent_home_exist != "no":
        counter += 1
        print(f"\n({counter}) According to the information provided, {name} has a permanent home only in {homes[0]}.")
        print(f"Hence, pursuant to Article 4(2)(a), {name} shall be considered to be a resident of {homes[0]}.")
        #END
    else:
        counter += 1
        print(f"\n({counter}) According to the information provided, {name} does not have any permanent homes.")
        print("Hence, pursuant to Article 4(2)(b), it must be determined whether the subject has an habitual abode.")
        if len(habitual_abodes) > 1 or len(habitual_abodes) == 0:
            counter += 1
            print(f"\n({counter}) According to the information provided, {name} has either an habitual abode both in {residences[0]} and {residences[1]} or neither of them.")
            print(f"Hence, pursuant to Article 4(2)(c), {name} shall be deemed to be a resident only of the State in which he is a national.")
            if len(nationalities) > 1:
                counter += 1
                print(f"\n({counter}) According to the information provided, {name} is a national of both {residences[0]} and {residences[1]}.")
                print(f"Hence, pursuant to Article 4(2)(d), {name} shall be deemed to be a resident only of the State that is settled by a mutual agreement procedure.")
                #END
            elif len(nationalities) == 1:
                counter += 1
                print(f"\n({counter}) According to the information provided, {name} is a national only of {nationalities[0]}.")
                print(f"Hence, pursuant to Article 4(2)(c), {name} shall be deemed to be a resident of {nationalities[0]}.")
                #END
            else:
                counter += 1
                print(f"\n({counter}) According to the information provided, {name} is a national of neither {residences[0]} and {residences[1]}.")
                print(f"Hence, pursuant to Article 4(2)(d), {name} shall be deemed to be a resident only of the State that is settled by a mutual agreement procedure.")
                #END
        elif len(habitual_abodes) == 1:
            counter += 1
            print(f"\n({counter}) According to the information provided, {name} has his/her habitual abode only in {habitual_abodes[0]}.")
            print(f"Hence, pursuant to Article 4(2)(b), {name} shall be considered to be a resident of {habitual_abodes[0]}.")
            #END

def main():
    
    task = pipeline("question-answering")
    yes_list = ["Yes", "yes", "Yes.", "yes."]

    while True:
    
        name, subject, residence, permanent_home_exist, permanent_home, civ, habitual_abode, nationality = input_extraction(task)
        double_residence, single_residence = single_or_double_residence(name, residence)

        liable_to_tax = input("\nPlease indicate whether your subject is liable to tax or not.\n\nUser (Yes/No): ")

        if liable_to_tax in yes_list:
            if single_residence:
                single_residence_pipeline(name, residence)
            elif double_residence:
                if subject == "individual":
                    individual_residence_pipeline(name, subject, residence, permanent_home_exist, permanent_home, civ, habitual_abode, nationality)
                else:
                    entity_residence_pipeline(name, subject, residence)
        else:
            print(f"\n{name} cannot be a resident of {residence} for treaty purposes subject to Article 4(1), first paragraph, as he is not liable to tax.")
            
main()
