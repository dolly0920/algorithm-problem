import sys
from collections import defaultdict
import heapq

sys.stdin = open("../input.txt", "rt")

def solution(genres, plays):
    answer = []

    genres_heap = []
    play_time_genres = defaultdict(int)
    play_time_file = defaultdict(list)

    for i in range(len(genres)):
        play_time_genres[genres[i]] += plays[i]
        heapq.heappush(play_time_file[genres[i]], (-plays[i], i))

    for g, p in play_time_genres.items():
        heapq.heappush(genres_heap, (-p, g))

    while genres_heap:
        play_all_time, genre = heapq.heappop(genres_heap)
        count = 0
        while play_time_file[genre] and count < 2:
            count += 1
            play_file_time, index = heapq.heappop(play_time_file[genre])
            answer.append(index)

    return answer

if __name__ == "__main__" :
    genres = list(input().split())
    plays = list(map(int, input().split()))
    print(solution(genres, plays))