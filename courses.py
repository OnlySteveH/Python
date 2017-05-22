COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topic):
    courses = []
    for keys, values in COURSES.items():
        if topic.intersection(values):
            courses.append(keys)
    return courses

def covers_all(topics):
    courses = []
    for keys, values in COURSES.items():
        if topics.issubset(values):
            courses.append(keys)
    return courses




print(covers({"integers"}))
print(covers_all({"conditions", "input"}))
