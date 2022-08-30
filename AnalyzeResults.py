"""
AnalyzeResults class. Response to make the analysis of the people in the car.
"""


def is_child_alone(age_results: list):
    """
    Make the analysis of the age classification. if there is only
    children in the car return False.
    :return: True if there is only children in the car.
    """

    if not age_results:
        return False

    ages_in_car = extract_ages(age_results)

    minimum_age = min(ages_in_car)
    maximum_age = max(ages_in_car)
    print(minimum_age)
    print(maximum_age)
    if minimum_age < 8 and maximum_age < 8:
        return True

    return False


def extract_ages(age_results: list[str]) -> list[int]:
    return [int(age.strip("()").split("-")[0]) for age in age_results]


# if __name__ == '__main__':
#     ages = ["(0-2)", "(4-6)", "(8-12)", "(15-20)",
#             "(25-32)", "(48-56)", "(60-65)", "(80-100)"]
#     ages2 = ["(0-2)", "(4-6)"]
#     print(is_child_alone(ages))

