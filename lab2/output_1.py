class Person:
    def __init__(self, name, age, gender, height, weight, scores):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.scores = scores

    def calculate_total_score(self):
        total_score = sum(self.scores)
        return total_score

    def is_adult(self):
        return self.age >= 18

    def display_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Height:", self.height)
        print("Weight:", self.weight)
        print("Total Score:", self.calculate_total_score())
        print("Adult:", self.is_adult())

person_info = {
    "name": "John",
    "age": 25,
    "gender": "Male",
    "height": 175,
    "weight": 70,
    "scores": [85, 90, 75, 88, 92]
}

john = Person(**person_info)
john.display_information()
