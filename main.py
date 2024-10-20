set_cardealer1 = {"BMW 3 series", "BMW 5 series", "BMW ix", "BMW i8", "Range Rover Sport", "Range Rover Velar"}

set_cardealer3 = {"BMW 8", "Range Rover Sport SVR", "BMW x6"}

set_union = set_cardealer1.union(set_cardealer2, set_cardealer3)
print("Car selection after dealer merge: ", set_union)

intersection = set_cardealer1.intersection(set_cardealer2)
print("Intersection: ", intersection)


