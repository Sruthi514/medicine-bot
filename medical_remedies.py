def medical_remedies():
    print("choose from the following problem")
    print(" 1.cold\n 2.caugh\n 3.acidity\n 4.diarrhea \n 5.vomitings\n 6.fever\n 7.blood pressure\n 8.allergies\n 9.stomach ache\n 10.diabetes \n 11.dehyration\n 12.food poisoning\n 13.itching\n 14.obesity\n 15.toothache")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        print("The general reasons for headache are:\n-strees\n -skipped meals\n -lack of sleep \n-certain foods that produce nitrates")
        print("The medical remedies for cold are:")
        print("1.Vicks DayQuil Cough Cold and Flu Relief \n2.Theraflu Daytime Severe Cold & Cough Packets with Menthol & Green Tea Flavors \n3.Sambucol Black Elderberry Cold & Flu Relief Tablets \n4.Mucinex Sinus-Max Pressure and Pain Caplets \n5.Genexa Cold Crush Tablets \n6.Tylenol Cold + Head Congestion Severe")
        
    elif choice == 2:
        print("The general reasons for cough are:\n-damage to the vocal cords\n -postnasal drip\n -bacterial infections \n -smoking")
        print("The medical remedies for cough are:")
        print("1.Pseudoephedrine \n2.Guaifenesin \n3.Dextromethorphan \n4.Tylenol \n5.Advil")
        
    elif choice == 3:
        print("The general reasons for acidity are:\n-eating heavy meal\n -being overweight\n -snacking close to bedtime")
        print("The medical remedies for acidity are:")
        print("1.Dexlansoprazole (Dexilant) \n2.Esomeprazole (Nexium) \n3.Lansoprazole (Prevacid) \n4.Omeprazole (Prilosec, Zegerid) \nOmeprazole (Prilosec, Zegerid)")
    
    elif choice == 4:
        print("The general reasons for diarrhea are:\n-viruses \n -bacteria and parasites \n -artificial sweeteners \n -other digestive isorders")
        print("The medical remedies are:")
        print("1.Loperamide \n2.Diphenoxylate \n3.Cholestyramine \n4.Codeine sulfate")
        
    elif choice == 5:
        print("The general reasons for vomitings are:\n-indigestion \n -migrane headaches \n -food poisioning\n -chemotheraphy")
        print("The medical remedies for vomitings are:")
        print("1.Aprepitant \n2.Dolasetron \n3.Granisetron \n4.Ondansetron \n5.Palonosetron")
        
    elif choice == 6:
        print("The general reasons for fever are:\n-infections \n -heat exhaustion \n -a virus \n -some injections")
        print("The medical remedies for fever are:")
        print("1.Acetaminophen \n2.ibuprofen \n3.naproxen \n4.aspirin")
    
    elif choice == 7:
        print("The general reasons for blood pressure are:\n-loss of physical activity\n -stress \n -older age\n -genetics")
        print("The medical reasons for blood pressure are:")
        print("1.Thiazide diuretics \n2.Calcium channel blockers - CCBs. \n3.Angiotensin receptor blockers - ARBs \n4.Angiotensin-converting enzyme inhibitors -ACEIs.")
    elif choice ==8:
        print("The general reasons for allergies are:\n-airborne allergies \n -insect stings\n -medications\n-certain foods")  
        print("The medical remedies for allergies are:")
        print("1.cetrizine\n 2.fexofenadine\n 3.levocetrizine\n 4.loratadine\n 5.chlorpheniramine") 
    elif choice == 9:
        print("The general reasons for stomach ache are:\n-food poisoning\n -food allergies\n -gas\n -urinary track infection")
        print("The medical remedies for stomach ache are:")
        print("1.acetaminophen \n 2.simethicone \n 3.docusates\n 4.bisacodyl\n 5.promethazine theolate")
    elif choice == 10:
        print("The general reasons for diabetes are:\n-high alocohol intake\n -obesity\n -high fat\n -sedentary lifestyle")
        print("The medical remedies for diabates are:")
        print("1.humulin \n 2.flexpen \n 3.apidra\n 4.levemir\n 5.tersiba")
    elif choice == 11:
        print("The general reasons for dehydration are:\n-fever\n -vomiting\n -excessive sweating \n -diarrhea")
        print("The medical remedies for dehydration are:")
        print("1.plasma-lyte 148\n 2.normosol\n 3.isolyte S\n 4.ivp solution \n 5.ringer's injection")
    elif choice == 12:
        print("The general reasons for food poisoning are:\n-weakness\n -loss of appetite\n -headaches\n -abdominal cramps")
        print("The medical remedies for food poisoning are:")
        print("1.imodium\n 2,pepto-bismol\n 3.imotil\n 4.chloropromazine\n 5.metoclopramide")
    elif choice == 13:
        print("The general reaons for itching are:\n-internal diseases\n -irritation and allergic reactions\n -nerve disorders\n -pregnancy")
        print("The medical remedies are:")
        print("1.pramoxine\n 2.diphenhyramine\n 3.corticosteroid\n 4.kenalog\n 5.temovate")
    elif choice == 14:
        print("The general reasons for obesity are:\n-unhealthy diet\n -liquid calories\n -inactivity\n -quitting smoking\n -stress")
        print("The medical remedies for obesity are:")
        print("1.phentermine \n 2.topiramate systemic \n 3.phentermine systemic\n 4.lorcaserin\n 5.naltrexone")
    elif choice == 15:
        print("The general reasons for toothache are:\n-tooth decay\n -a damaged filling \n -tooth fracture\n -infected gums")
        print("The medical remedies for toothache are:")
        print("1.acetaminophen \n 2.ibuprofen\n 3.advil liqui gels\n 4.amoxicillin\n 5.pencillin")
    else:
        print("Sorry!, we didn't provide information regarding these health issues")