set_cardealer1 = {"BMW 3 series", "BMW 5 series", "BMW ix", "BMW i8", "Range Rover Sport", "Range Rover Velar"}
set_cardealer2 = {"BMW 7 series", "BMW 5 series", "Range Rover Evoque", "Range Rover Velar"}
set_cardealer3 = {"BMW 8", "Range Rover Sport SVR", "BMW x6"}

set_union = set_cardealer1.union(set_cardealer2, set_cardealer3)
print("Car selection after dealer merge: ", set_union)

set_cardealer2_new = set_cardealer2.add("BMW i3")

intersection = set_cardealer1.intersection(set_cardealer2)
print("Intersection: ", intersection)


