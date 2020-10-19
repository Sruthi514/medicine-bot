def calculations():
    expr=input("Enter your expression :")
    try:
        print("result : ",eval(expr))
    except:
        print("I don't understand that")
