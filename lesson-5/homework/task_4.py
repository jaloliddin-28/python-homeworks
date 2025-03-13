universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
def enrollment_stats(any_list):
    total_students = []
    tuition = []
    for i in any_list:
        total_students.append(i[1])
        tuition.append(i[2])
    return total_students, tuition

def mean(single_list):
    mean_1 = round((sum(single_list) / len(single_list)), 2)
    return mean_1

def median(single_list):
    single_list.sort()
    median_1 = single_list[3]
    return median_1

l, s = enrollment_stats(universities)
f, g = (mean(l), median(l))
h, o = (mean(s), median(s))
print("Total students: ", sum(l), f'\nTotal tuition: $ {sum(s)}')
print("Student mean: ", f, "\nStudent median: ", g)
print("Tuition mean: $", h, "\nTuition median: $", o)