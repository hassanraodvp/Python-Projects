room_Rent = int(input("Enter the room rent: "))
Food = int(input("Enter the food cost: "))
Electricity_unit = int(input("Enter the electricity unit consumed: "))
elect_charge_per_unit = int(input("Enter the electricity charge per unit: "))
Internet = int(input("Enter the internet cost: "))
sharing_person = int(input("Enter the number of persons in the room: "))

total_bill = Electricity_unit * elect_charge_per_unit

output = (room_Rent + Food + total_bill + Internet) // sharing_person

print("The total bill on each person is: ", output)
