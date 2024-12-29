class SurvivalDurationCalculator:
    def __init__(self, age):
        self.age = age

    def calculate_duration(self, unit):
        if unit == "months":
            return self.age * 12
        elif unit == "weeks":
            return self.age * 52.1429
        elif unit == "days":
            return self.age * 365.25
        elif unit == "hours":
            return self.age * 365.25 * 24
        elif unit == "minutes":
            return self.age * 365.25 * 24 * 60
        elif unit == "seconds":
            return self.age * 365.25 * 24 * 60 * 60
        else:
            raise ValueError("Invalid time unit selected!")

    @staticmethod
    def get_time_unit_choice():
        print("\nChoose a time unit: Months, Weeks, Days, Hours, Minutes, Seconds.")
        print("You can enter the first letter or full name of the time unit.")
        unit = input("Enter your choice: ").strip().lower()
        unit_mapping = {
            'm': 'months', 'months': 'months',
            'w': 'weeks', 'weeks': 'weeks',
            'd': 'days', 'days': 'days',
            'h': 'hours', 'hours': 'hours',
            'mi': 'minutes', 'minutes': 'minutes',
            's': 'seconds', 'seconds': 'seconds'
        }
        return unit_mapping.get(unit, None)

    @staticmethod
    def get_age_input():
        while True:
            try:
                age = float(input("What's your age (in years)? "))
                if age < 0:
                    print("Age cannot be negative. Please enter a valid age.")
                else:
                    return age
            except ValueError:
                print("Invalid input. Please enter a numerical value for age.")

def main():
    print("Welcome to the Survival Duration Calculator!")
    age = SurvivalDurationCalculator.get_age_input()
    calculator = SurvivalDurationCalculator(age)
    unit = None
    while not unit:
        unit = SurvivalDurationCalculator.get_time_unit_choice()
        if not unit:
            print("Invalid choice. Please try again.")
    try:
        duration = calculator.calculate_duration(unit)
        print(f"\nYou have lived for approximately {duration:.2f} {unit.capitalize()}!")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
