print("=====Holiday Aactivity Planner=====")

print("Enter 1 for Beach holiday")
print("Enter 2 for Mountain holiday")

choice=int(input("Enter 1 or 2 : "))
print()

if choice==1:
    print("yay!,You chose Beach holiday!")
    print("select your Beach activiyty")
    print("enter 1 for Swimming")
    print("enter 2 for Sandcastle Building")

    beach_activity=int(input("Enter 1 or 2 :  "))

    if beach_activity==1:
        print("Good choice! you chose Swimming!")
        print("Best in morning.")
        print("Remember to bring Sunscreen and Water.")

    elif beach_activity==2:
        print("Good choice! you chose Sandcastle Building!")
        print("Best in evening.")
        print("Remember to carry a Bucket and Spade.")

    else:
        print("Invalid input.\nPlease check it again")

elif choice==2:
    print("yay!,You chose Mountain holiday holiday!")
    print("select your Mountain activiyty")

    print("Enter 1 for Hiking.")
    print("Enter 2 for camping")

    mountain_activity=int(input("Enter 1 or 2: "))

    if mountain_activity==1:
        print("Good choice! you chose Hiking!")
        print("Best for exploring Trails.")
        print("Remember to wear Comfortable Shoes.")
    
    elif mountain_activity==2:
        print("Good choice! you chose Camping!")
        print("best for staying close to Nature")
        print("Remember to carry Tent and Flashlight")
    
    else:
        print("Invalid input.\nPlease check it again")

else:
    print("Invalid input.\nPlease check it again")