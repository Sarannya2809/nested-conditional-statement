Medical_cause=input("did you have some medical issues yes or no?")
attendance= int(input("put the attendance of the stdent:"))
if Medical_cause== 'Yes' :
    print("you can come")
else:
    if attendance >=75:
        print("you can come")
    else:
        print("you cant come")
