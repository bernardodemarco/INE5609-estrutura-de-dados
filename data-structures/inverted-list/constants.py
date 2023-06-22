from enum import Enum


JSON_FILE_PATH = 'data.json'


# Each salary category maps to an interval, in which the first
# value is inclusive and the second one is exclusive.
# For example: [first_value; second_value[
# None" means +(infinite).
SALARY_CATEGORIES = {
    'beginner_salary': (0, 5000),
    'intermediate_salary': (5000, 10000),
    'advanced_salary': (10000, None)
}


class SimpleQuery(Enum):
    COURSE = 1
    SOCCER_TEAM = 2
    SALARY = 3

class CompositeQuery(Enum):
    COURSE_AND_SOCCER_TEAM = 1
    COURSE_AND_SALARY = 2
    SOCCER_TEAM_AND_SALARY = 3
