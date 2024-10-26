student = {"name":"Arish Ray","age":10,"grade":5,"hobby":"playing cricket"}
print("Everything about Me!")
print("1.name")
print("2.age")
print("3.grade")
print("4.hobby")
choice = input("enter your choice")
if choice =="1":
    print("my name is",student["name"])
elif choice =="2":
    print("my age is",student["age"])
elif choice =="3":
    print("my grade is",student["grade"])
elif choice =="4":
    print("my hobby is",student["hobby"])
else:
    print("invalid option")