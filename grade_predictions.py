import numpy
import matplotlib.pyplot as plt
class GradePrediction:
    def __init__(self, name, grades, degree, test_to_predict):
        self.name = name
        self.grades = grades
        self.degree = degree
        # Approximating a function of the grades
        self.prediction = numpy.poly1d(numpy.polyfit([i for i in range(len(grades))], grades, degree))
        self.percent_error = 0
        self.test_to_predict = test_to_predict
        self.average = 0
        self.lower_range = 0
        self.upper_range = 100


    @staticmethod
    def zero_to_hundred(x) -> float:
        if x > 100:
            return 100.00
        elif x < 0:
            return 0.00
        else:
            return x

    def output(self):
        for i in range(len(self.grades)):
            self.percent_error += abs(self.prediction(i) - self.grades[i])
        self.percent_error = (self.percent_error / len(self.grades)) / 100

        for i in range(self.test_to_predict - len(self.grades)):
            self.grades.append(self.zero_to_hundred(self.prediction(i + len(self.grades))))

        total_grades = 0
        for i in self.grades:
            total_grades += i
        self.average = total_grades / self.test_to_predict

        my_line = numpy.linspace(1, self.test_to_predict, 100)
        plt.scatter([i for i in range(len(self
                                          .grades))], self.grades)
        plt.plot(my_line, self.prediction(my_line), "g")
        plt.title(self.name)
        plt.ylim(ymin=0)
        plt.ylim(ymax=100)

        plt.suptitle("Grades")
        plt.show()

        self.lower_range = self.zero_to_hundred(round((1 - self.percent_error) * self.prediction(self.test_to_predict), 2))
        self.upper_range = self.zero_to_hundred(round((1 + self.percent_error) * self.prediction(self.test_to_predict), 2))

        print(f"{self.name}'s next grade would be in between {self.lower_range} "
              f"and {self.upper_range}. His new average would be about {round(self.average, 2)}.")

Ethan = GradePrediction("Ethan", [100, 92.5, 80, 62.8, 60, 54], 2, 5)
Ethan.output()