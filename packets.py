from collections import deque
def process_packets(buffer_size, packets):
    result = []
    buffer = deque()
    current_time = 0
    for arrival, processing in packets:
        while buffer and buffer[0] <= arrival:
            buffer.popleft()
        if len(buffer) < buffer_size:
            start_time = max(arrival, current_time)
            result.append(start_time)
            current_time = start_time + processing
            buffer.append(current_time)
        else:
            result.append(-1)
    return result
S, n = map(int, input().split())
packets = [tuple(map(int, input().split())) for _ in range(n)]
result = process_packets(S, packets)
for res in result:
    print(res)
