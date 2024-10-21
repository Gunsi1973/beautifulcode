Budget = int(input("Enter your Budget."))
transport = int(input("Enter costs for Transport."))
unterkunft = int(input("Enter costs for Accommodation."))
verpflegung = int(input("Enter costs for Catering."))

Costs = (transport + unterkunft + verpflegung)


if Costs > Budget:
    print("the planned trip is not within the budget! :(.")
else:
    print("the planned trip is within the budget!:).")
