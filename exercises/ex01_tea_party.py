"""Planning a fun tea party in class COMP110!"""

__author__: str = "730715920"


def main_planner(guests: int) -> None:
    """Main planner."""
    print("A cozy tea party for " + str(guests) + " people")
    print("Tea bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), (treats(guests)))))


def tea_bags(people: int) -> int:
    """Calculate the number of bags of tea."""
    return people * 2


def treats(people: int) -> int:
    """Calculate the number of treats."""
    return int((tea_bags(people=people) * 3) / 2)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculate the cost of tea and treats."""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))


print(main_planner(guests=5))
