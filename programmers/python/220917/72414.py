## https://school.programmers.co.kr/learn/courses/30/lessons/72414
def solution(play_time, adv_time, logs):
    adv_time = convert_to_sec(adv_time)
    play_time = convert_to_sec(play_time)

    max_watch_time = 0

    watch = [0 for _ in range(play_time + 1)]

    for log in logs:
        start, end = log.split('-')
        start = convert_to_sec(start)
        end = convert_to_sec(end)
        watch[start] += 1
        watch[end] -= 1

    for i in range(1, play_time + 1):  ## 각 구간의 시청자 수
        watch[i] = watch[i - 1] + watch[i]

    for i in range(1, play_time + 1):  ## prefix sum
        watch[i] = watch[i - 1] + watch[i]

    ## 누적 시청시간 (a ~ b) : watch[b] - watch[a-1]
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            watch_time = watch[i] - watch[i - adv_time]
            if watch_time > max_watch_time:
                max_watch_time = watch_time
                answer = i - adv_time + 1
        else:
            if watch[i] > max_watch_time:
                max_watch_time = watch[i]
                answer = i - adv_time + 1

    return convert_to_string(answer)


def convert_to_sec(time):  ## hh:mm:ss
    hh, mm, ss = time.split(':')
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


def convert_to_string(second):
    hh = second // 3600
    mm = (second % 3600) // 60
    ss = second % 60
    return str(hh).zfill(2) + ":" + str(mm).zfill(2) + ":" + str(ss).zfill(2)