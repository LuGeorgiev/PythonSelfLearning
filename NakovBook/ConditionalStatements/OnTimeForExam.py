def calculate_time(exam_minutes_int, arrival_minutes_int):
    time_diff = exam_minutes_int - arrival_minutes_int
    if time_diff == 0:
        return 0, ''
    elif 0 < time_diff <= 30:
        return 0, time_span(time_diff)
    elif time_diff > 30:
        return -1, time_span(time_diff)
    else:
        return 1, time_span(time_diff)


def time_span(time_diff_int):
    hour = abs(int(time_diff_int / 60))
    minutes = abs(time_diff_int) - 60 * hour
    if time_diff_int == 0:
        return ''
    elif hour >= 1:
        return f'{hour}:{minutes:02} hours'
    else:
        return f'{minutes} minutes'


exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())
exam_in_minutes = exam_hour * 60 + exam_minute
arrival_in_minutes = arrival_hour * 60 + arrival_minute

is_Late, time_span = calculate_time(exam_in_minutes, arrival_in_minutes)
if is_Late == 0:
    if time_span == '':
        print('On time')
    else:
        print(f'On time\n{time_span} before the start')
elif is_Late == -1:
    print(f'Early\n{time_span} before the start')
else:
    print(f'Late\n{time_span} after the start')

