class Exercise:
    def __init__(self, topic, course, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course
        self.judge_contest_link = judge_contest_link
        self.problems_list = problems


exercise_list = []
data_list = input().split(' -> ')
while not data_list[0] == 'go go go':
    topic_name = data_list[0]
    course_name = data_list[1]
    judge_link = data_list[2]
    problem_list = data_list[3].split(', ')

    exercise = Exercise(topic_name, course_name, judge_link, problem_list)
    exercise_list.append(exercise)

    data_list = input().split(' -> ')

for exercise in exercise_list:
    print(f'Exercises: {exercise.topic}')
    print(f'Problems for exercises and homework for the "{exercise.course_name}" course @ SoftUni.')
    print(f'Check your solutions here: {exercise.judge_contest_link}')
    for index in range(len(exercise.problems_list)):
        print(f'{index + 1}. {exercise.problems_list[index]}')
