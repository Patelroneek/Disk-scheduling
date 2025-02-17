import numpy as np

def fcfs(requests, head):
    seek_time = 0
    for req in requests:
        seek_time += abs(head - req)
        head = req
    return seek_time

def sstf(requests, head):
    requests = requests[:]
    seek_time = 0
    while requests:
        closest = min(requests, key=lambda x: abs(head - x))
        seek_time += abs(head - closest)
        head = closest
        requests.remove(closest)
    return seek_time

def scan(requests, head, disk_size, direction="right"):
    requests.sort()
    seek_time = 0
    if direction == "right":
        right = [r for r in requests if r >= head]
        left = [r for r in requests if r < head]
        seek_time += (max(right) - head) if right else 0
        if left:
            seek_time += (max(right) - min(left))
    else:
        left = [r for r in requests if r <= head]
        right = [r for r in requests if r > head]
        seek_time += (head - min(left)) if left else 0
        if right:
            seek_time += (max(right) - min(left))
    return seek_time

def cscan(requests, head, disk_size):
    requests.sort()
    seek_time = 0
    right = [r for r in requests if r >= head]
    left = [r for r in requests if r < head]
    seek_time += (max(right) - head) if right else 0
    if left:
        seek_time += (disk_size - 1 - min(left)) + (disk_size - 1)
    return seek_time

def look(requests, head, direction="right"):
    requests.sort()
    seek_time = 0
    if direction == "right":
        right = [r for r in requests if r >= head]
        left = [r for r in requests if r < head]
        seek_time += (max(right) - head) if right else 0
        if left:
            seek_time += (max(right) - min(left))
    else:
        left = [r for r in requests if r <= head]
        right = [r for r in requests if r > head]
        seek_time += (head - min(left)) if left else 0
        if right:
            seek_time += (max(right) - min(left))
    return seek_time

def clook(requests, head):
    requests.sort()
    seek_time = 0
    right = [r for r in requests if r >= head]
    left = [r for r in requests if r < head]
    seek_time += (max(right) - head) if right else 0
    if left:
        seek_time += (max(right) - min(left))
    return seek_time

# Example Usage
requests = [98, 183, 37, 122, 14, 124, 65, 67]
head = 53
disk_size = 200

print("Disk Scheduling Analysis:")
print(f"FCFS Seek Time: {fcfs(requests, head)}")
print(f"SSTF Seek Time: {sstf(requests, head)}")
print(f"SCAN Seek Time: {scan(requests, head, disk_size)}")
print(f"C-SCAN Seek Time: {cscan(requests, head, disk_size)}")
print(f"LOOK Seek Time: {look(requests, head)}")
print(f"C-LOOK Seek Time: {clook(requests, head)}")
