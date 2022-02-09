def employment_pipeline():
    """Function that gets from the user the desired input that will be sent to the model and extracts relevant information."""

    print("="*100)
    print("Employment Income Analysis")
    print("="*100)

    #Opening variables

    name = ""
    residence = ""
    special_rule = ""
    ship_aircraft = ""
    ship_aircraft_source = ""

    #User input

    name = input("\nWhat is the name of the subject?\n\nUser: ")
    residence = input(f"\nWhere is {name} a resident?\n\nUser: ")
    special_rule = input(f"\nIs {name} receiving income from the provisions of Articles 16 to 19 (Director's Fees, Sportsman, Entertainers, Pensions and Civil Servants)?\n\nUser (Yes/No): ")

    if special_rule == "Yes":
        print(f"\nPursuant to Article 15(1), the tax treatment to be afforded to income derived by {name} shall not be taxable in accordance with Article 15 as special rules apply (see Arts. 16 to 19).")
        #END
    else:      
        ship_aircraft = input(f"\nIs {name} receiving income from an employment as a member of the regular complement of a ship or aircraft?\n\nUser (Yes/No): ")
        if ship_aircraft == "Yes":
            ship_aircraft_source = input(f"\nIs the activity exercised aboard a ship or aircraft operated in international traffic, other than aboard a ship or aircraft operated solely within the other Contracting State?\n\nUser (Yes/No): ")
            if ship_aircraft_source == "No":
                print(f"\nPursuant to Article 15(3), income derived by {name} shall be taxable only in {residence}.")
                #END
            else:
                place_of_work = input(f"\nWhere does {name} carry out his/her employment?\n\nUser: ")
                if place_of_work == residence:
                    print(f"\nPursuant to Article 15(1), income derived by {name} shall be taxable only in {residence}.")
                    #END
                else:
                    exception_one = input(f"\nIs {name} present in {place_of_work} for a period or periods exceeding in the aggregate 183 days in any twelve month period commencing or ending in the fiscal year concerned?\n\nUser (Yes/No): ")
                    if exception_one == "Yes":
                        print(f"\nPursuant to Article 15(2), income derived by {name} may be taxed both in {residence} and {place_of_work}.")
                        #END
                    else:
                        exception_two = input(f"\nIs the remuneration paid by, or on behalf of, an employer who is a resident of {place_of_work}?\n\nUser (Yes/No): ")
                        if exception_two == "Yes":
                            print(f"\nPursuant to Article 15(2), income derived by {name} may be taxed both in {residence} and {place_of_work}.")
                            #END
                        else:
                            exception_three = input(f"\nIs the remuneration borne by a permanent establishment which the employer has in {place_of_work}?\n\n User (Yes/No): ")
                            if exception_three == "Yes":
                                print(f"\nPursuant to Article 15(2), income derived by {name} may be taxed both in {residence} and {place_of_work}.")
                                #END
                            else:
                                print(f"\nPursuant to ARticle 15(2), income derived by {name} shall only be taxable in {residence}, since the exceptions of such paragraph are applicable.")
                                #END
        else:
            place_of_work = input(f"\nWhere does {name} carry out his/her employment?\n\nUser: ")
            if place_of_work == residence:
                print(f"\nPursuant to Article 15(1), income derived by {name} shall be taxable only in {residence}.")
            else:
                exception_one = input(f"\nIs {name} present in {place_of_work} for a period or periods not exceeding in the aggregate 183 days in any twelve month period commencing or ending in the fiscal year concerned?\n\nUser (Yes/No): ")
                if exception_one == "Yes":
                    print(f"\nPursuant to Article 15(2), income derived by {name} may be taxed both in {residence} and {place_of_work}.")
                    #END
                else:
                    exception_two = input(f"\nIs the remuneration paid by, or on behalf of, an employer who is a resident of {place_of_work}?\n\nUser (Yes/No): ")
                    if exception_two == "Yes":
                        print(f"\nPursuant to Article 15(2), income derived by {name} may be taxed both in {residence} and {place_of_work}.")
                        #END
                    else:
                        exception_three = input(f"\nIs the remuneration borne by a permanent establishment which the employer has in {place_of_work}?\n\n User (Yes/No): ")
                        if exception_three == "Yes":
                            print(f"\nPursuant to Article 15(2), income derived by {name} may be taxed both in {residence} and {place_of_work}.")
                            #END
                        else:
                            print(f"\nPursuant to ARticle 15(2), income derived by {name} shall only be taxable in {residence}, since the exceptions of such paragraph are applicable.")
                            #END

#####################################

while True:

    employment_pipeline()
