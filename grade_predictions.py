import numpy
import matplotlib.pyplot as plt

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Establishing the test grades, and the order the tests were taken
test_number = [1, 2, 3, 4, 5, 6, 7, 8]
alex_grades = [15, 32, 37, 31, 29, 34, 0, 0]
ethan_grades = [90, 75, 70, 40, 66.7, 39.5, 0, 60]
oliver_grades = [50, 75, 57, 95, 58, 66, 0, 0]
sam_grades = [77, 72, 92.3, 61.9, 80.8, 74]
lawrence_grades = [60, 90, 87.5, 100, 87.5, 79, 0, 0]
roen_grades = [100, 92.5, 80, 62.8, 60, 54]
# thing = GradePrediction(1, 2, 3)
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Approximating a function of the grades
alex_prediction = numpy.poly1d(numpy.polyfit(test_number, alex_grades, 1))
ethan_prediction = numpy.poly1d(numpy.polyfit(test_number, ethan_grades, 2))
oliver_prediction = numpy.poly1d(numpy.polyfit(test_number, oliver_grades, 1))
sam_prediction = numpy.poly1d(numpy.polyfit(test_number, sam_grades, 1))
lawrence_prediction = numpy.poly1d(numpy.polyfit(test_number, lawrence_grades, 3))
roen_prediction = numpy.poly1d(numpy.polyfit(test_number, roen_grades, 2))

#
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creating function to make sure no value is above 100, or below 0
def zero_to_hundred(x):
    if x > 100:
        return 100.00
    elif x < 0:
        return 0.00
    else:
        return x
#
#
# # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Calculating %Error of approximated function to real data
alex_percent_error = 0
ethan_percent_error = 0
oliver_percent_error = 0
sam_percent_error = 0
lawrence_percent_error = 0
roen_percent_error = 0

for i in range(len(test_number)):
    alex_percent_error += abs(alex_prediction(i)-alex_grades[i])
    roen_percent_error += abs(roen_prediction(i) - roen_grades[i])
    ethan_percent_error += abs(ethan_prediction(i) - ethan_grades[i])
    oliver_percent_error += abs(oliver_prediction(i) - oliver_grades[i])
    sam_percent_error += abs(sam_prediction(i) - sam_grades[i])
    lawrence_percent_error += abs(lawrence_prediction(i) - lawrence_grades[i])
alex_percent_error = (alex_percent_error/len(test_number))/100
ethan_percent_error = (ethan_percent_error/len(test_number))/100
oliver_percent_error = (oliver_percent_error/len(test_number))/100
sam_percent_error = (sam_percent_error/len(test_number))/100
lawrence_percent_error = (lawrence_percent_error/len(test_number))/100
roen_percent_error = (roen_percent_error/len(test_number))/100

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Adding the desired predictions to the list of grades
tests_to_predict = int(input(f"What test do you want to predict? (They have already taken {len(test_number)} tests): "))
for i in range(tests_to_predict-len(test_number)):
    alex_grades.append(zero_to_hundred(alex_prediction(i+len(test_number))))
    ethan_grades.append(zero_to_hundred(ethan_prediction(i+len(test_number))))
    oliver_grades.append(zero_to_hundred(oliver_prediction(i+len(test_number))))
    sam_grades.append(zero_to_hundred(sam_prediction(i+len(test_number))))
    lawrence_grades.append(zero_to_hundred(lawrence_prediction(i + len(test_number))))
    roen_grades.append(zero_to_hundred(roen_prediction(i + len(test_number))))
# Adding the number of tests predicted to test_number list (the x and y values need to be equal in length)
    test_number.append(1+len(test_number))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Calculating the average of the grades including predicted grades
alex_total_grades = 0
for i in alex_grades:
    alex_total_grades += i
alex_average = alex_total_grades/tests_to_predict
ethan_total_grades = 0
for i in ethan_grades:
    ethan_total_grades += i
ethan_average = ethan_total_grades/tests_to_predict
oliver_total_grades = 0
for i in oliver_grades:
    oliver_total_grades += i
oliver_average = oliver_total_grades/tests_to_predict
oliver_total_grades = 0
sam_total_grades = 0
for i in sam_grades:
    sam_total_grades += i
sam_average = sam_total_grades/tests_to_predict
lawrence_total_grades = 0
for i in lawrence_grades:
    lawrence_total_grades += i
lawrence_average = lawrence_total_grades/tests_to_predict
roen_total_grades = 0
for i in roen_grades:
    roen_total_grades += i
roen_average = roen_total_grades/tests_to_predict

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Asking user whether to show the graphs
if input("Show graphs?: ").lower() == "yes":
    my_line = numpy.linspace(1, tests_to_predict, 100)
    # Alex's graph
    plt.subplot(2, 3, 1)
    plt.scatter(test_number, alex_grades)
    plt.plot(my_line, alex_prediction(my_line), "g")
    plt.title("Alex")
    plt.ylim(ymin=0)
    plt.ylim(ymax=100)
    # Ethan's graph
    plt.subplot(2, 3, 2)
    plt.scatter(test_number, ethan_grades)
    plt.plot(my_line, ethan_prediction(my_line), "c")
    plt.title("Ethan")
    plt.ylim(ymin=0)
    plt.ylim(ymax=100)
    # Oliver's graph
    plt.subplot(2, 3, 3)
    plt.scatter(test_number, oliver_grades)
    plt.plot(my_line, oliver_prediction(my_line), "m")
    plt.title("Oliver")
    plt.ylim(ymin=0)
    plt.ylim(ymax=100)
    # Sam's graph
    plt.subplot(2, 3, 4)
    plt.scatter(test_number, sam_grades)
    plt.plot(my_line, sam_prediction(my_line), "r")
    plt.title("Sam")
    plt.ylim(ymin=0)
    plt.ylim(ymax=100)
    # lawrence's graph
    plt.subplot(2, 3, 5)
    plt.scatter(test_number, lawrence_grades)
    plt.plot(my_line, lawrence_prediction(my_line), "g")
    plt.title("lawrence")
    plt.ylim(ymin=0)
    plt.ylim(ymax=100)
    # roen's graph
    plt.subplot(2, 3, 6)
    plt.scatter(test_number, roen_grades)
    plt.plot(my_line, roen_prediction(my_line), "g")
    plt.title("roen")
    plt.ylim(ymin=0)
    plt.ylim(ymax=100)

    plt.suptitle("Grades")
    plt.show()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Creating a range of possible estimated grades, calculated using %Error
alex_lower_range = zero_to_hundred(round((1-alex_percent_error)*alex_prediction(tests_to_predict), 2))
alex_upper_range = zero_to_hundred(round((1+alex_percent_error)*alex_prediction(tests_to_predict), 2))
ethan_lower_range = zero_to_hundred(round((1-ethan_percent_error)*ethan_prediction(tests_to_predict), 2))
ethan_upper_range = zero_to_hundred(round((1+ethan_percent_error)*ethan_prediction(tests_to_predict), 2))
oliver_lower_range = zero_to_hundred(round((1-oliver_percent_error)*oliver_prediction(tests_to_predict), 2))
oliver_upper_range = zero_to_hundred(round((1+oliver_percent_error)*oliver_prediction(tests_to_predict), 2))
sam_lower_range = zero_to_hundred(round((1-sam_percent_error)*sam_prediction(tests_to_predict), 2))
sam_upper_range = zero_to_hundred(round((1+sam_percent_error)*sam_prediction(tests_to_predict), 2))
lawrence_lower_range = zero_to_hundred(round((1-lawrence_percent_error)*lawrence_prediction(tests_to_predict), 2))
lawrence_upper_range = zero_to_hundred(round((1+lawrence_percent_error)*lawrence_prediction(tests_to_predict), 2))
roen_lower_range = zero_to_hundred(round((1-roen_percent_error)*roen_prediction(tests_to_predict), 2))
roen_upper_range = zero_to_hundred(round((1+roen_percent_error)*roen_prediction(tests_to_predict), 2))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Output
print(f"Alex's next math test grade would be in between {alex_lower_range} "
      f"and {alex_upper_range}. His new average would be approximately {round(alex_average, 2)}. He's ass lmao.")
print(f"Ethan's next math test grade would be in between {ethan_lower_range} "
      f"and {ethan_upper_range}. His new average would be approximately {round(ethan_average, 2)}.")
print(f"Oliver's next math test grade would be in between {oliver_lower_range} "
      f"and {oliver_upper_range}. His new average would be approximately {round(oliver_average, 2)}.")
print(f"Sam's next french test grade would be in between {sam_lower_range} "
      f"and {sam_upper_range}. His new average would be approximately {round(sam_average, 2)}.")
print(f"Lawrence's next physics test grade would be in between {lawrence_lower_range} "
      f"and {lawrence_upper_range}. His new average would be approximately {round(lawrence_average, 2)}.")
print(f"Roen's next math test grade would be in between {roen_lower_range} "
      f"and {roen_upper_range}. His new average would be approximately {round(roen_average, 2)}.")
