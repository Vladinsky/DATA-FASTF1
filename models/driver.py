# models/driver.py

class Driver:
    def __init__(self, name, number, team):
        self.name = name
        self.number = number
        self.team = team

    def __str__(self):
        return f"Driver: {self.name}, Number: {self.number}, Team: {self.team}"

# Example usage
if __name__ == "__main__":
    driver = Driver(name="Lewis Hamilton", number=44, team="Mercedes")
    print(driver)