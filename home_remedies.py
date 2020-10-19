def home_remedies():
    print("choose from the following problem")
    print(" 1.cold\n 2.cough\n 3.acidity\n 4.diarrhoea\n 5.vomitings\n 6.fever \n 7.blood pressure\n 8.allergies\n 9.stomach ache\n 10.diabetes \n 11.dehyration\n 12.food poisoning\n 13.itching\n 14.obesity\n 15.toothache")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        print("The general reasons for headache are:\n-strees\n -skipped meals\n -lack of sleep \n-certain foods that produce nitrates")
        print("The home remidies for headache are:")
        print("1.Chicken soup \n2.Ginger \n3.Honey \n4.garlic \n5.vitamin C \n6.vapour rub")

    elif choice == 2:
        print("The general reasons for cough are:\n-damage to the vocal cords\n -postnasal drip\n -bacterial infections \n -smoking")
        print("The home remedies for cough are:")
        print("1.Honey \n2.Probiotics \n3.Bromelain \n4.Peppermint \n5.Marshmallow \n6.Thyme  \n7.Salt and water gargle")
    elif choice == 3:
        print("The general reasons for acidity are:\n-eating heavy meal\n -being overweight\n -snacking close to bedtime")
        print("The home remedies are:")
        print("1.Cold buttermilk \n2.coconut water \n3.cold milk \n4.Herbs such as Ajwain, Tulsi leaves, Saunf, Jeera and Pudina leaves")
        
    elif choice == 4:
        print("The general reasons for diarrhoea are:\n-viruses \n -bacteria and parasites \n -artificial sweeteners \n -other digestive isorders")
        print("The home remeies are:")
        print("1.Safe drinking water \n2.Toilet hygiene \n3.Take extra care when someone in your family is suffering from diarrhoea \n4.Food hygiene")
        
    elif choice == 5:
        print("The general reasons for vomtings are:\n-indigestion \n -migrane headaches \n -food poisioning\n -chemotheraphy")
        print("The home remedies are:")
        print("1.Try deep breathing \n2.Eat bland crackers \n3.Wrist acupressure \n4.Drink more fluids \n5.Try ginger, fennel, or cloves ")
    
    elif choice == 6:
        print("The general reasons for fever are:\n-infections \n -heat exhaustion \n -a virus \n -some injections")
        print("The home remedies are:")
        print("1.Drink fluids \n2.Drink fluids \n3.Try herbal remedies like Moringa and Kudzu root")
        
    elif choice == 7:
        print("The general reasons for blood pressure are:\n-loss of physical activity\n -stress \n -older age\n -genetics")
        print("The home remedies are:")
        print("1.Get moving \n2.Follow the DASH diet \n3.Put down the saltshaker \n4.Lose excess weight \n5.Nix your nicotine addiction \n6.Limit alcohol ")
    elif choice == 8:
        print("The general reasons for allergies are:\n-airborne allergies \n -insect stings\n -medications\n-certain foods")
        print("The home remedies are:")
        print("1.honey\n 2.vitamin c\n 3.peppermint essential oil\n 4.eucalyptus essential oil")
    elif choice == 9:
        print("The general reasons for stomach ache are:\n-food poisoning\n -food allergies\n -gas\n -urinary track infection ")
        print("The home remedies are:")
        print("1.drinking water\n 2.ginger\n 3.mint\n 4.avoiding smoking\n 5.lime or lime juice")
    elif choice ==10:
        print("The general reasons for diabetes are:\n-high alocohol intake\n -obesity\n -high fat\n -sedentary lifestyle")
        print("The home remedies are:")
        print("1.vitamin c\n 2.cinnamon\n 3.bitter gourd\n 4.amla or indian gooseberry\n 5.drumsticks")
    elif choice == 11:
        print("The general reasons for dehydration are:\n-fever\n -vomiting\n -excessive sweating \n -diarrhea")
        print("The home remedies are:")
        print("1.buttermilk\n 2.bananas\n 3.coconut water\n 4.barley water\n 5.oral rehydration solution")
    elif choice == 12:
        print("The general reasons for food poisoning are:\n-weakness\n -loss of appetite\n -headaches\n -abdominal cramps")
        print("The home remedies are:")
        print("1.ginger \n 2.apple cider vinegar\n 3.lemon \n 4.cumin \n 5.honey")
    elif choice == 13:
        print("The general reaons for itching are:\n-internal diseases\n -irritation and allergic reactions\n -nerve disorders\n -pregnancy")
        print("The home remedies are:")
        print("1.moisturize your skin\n 2.oatmeal bath\n 3.applying cooling agents\n 4.apply a cold an wet cloth")
    elif choice == 14:
        print("The general reasons for obesity are:\n-unhealthy diet\n -liquid calories\n -inactivity\n -quitting smoking\n -stress")
        print("The home remedies for obesity are:")
        print("1.lemon\n 2.alovera\n 3.manage your diet\n 4.calorie restricted diets\n 5.intermittent fasting")
    elif choice ==15:
        print("The general reasons for toothache are:\n-tooth decay\n -a damaged filling \n -tooth fracture\n -infected gums")
        print("The home remedies are:")
        print("1.salt water rinse\n 2.hydrogen peroxide rinse\n 3.cold compress\n 4.peppermint tea bags\n 5.garlic ")

    else:
        print("Sorry!, we didn't provide information regarding these health issues")