
def common_area(N, rectangles):
    max_x1, max_y1, min_x2, min_y2 = rectangles[0]
    
    for i in range(1, N):
        x1, y1, x2, y2 = rectangles[i]
        max_x1 = max(max_x1, x1)
        max_y1 = max(max_y1, y1)
        min_x2 = min(min_x2, x2)
        min_y2 = min(min_y2, y2)

    if min_x2 > max_x1 and min_y2 > max_y1:
        return (min_x2 - max_x1) * (min_y2 - max_y1)
    else:
        return 0


T = int(input())

for i in range(1,T+1):
    N = int(input())
    rectangles = [list(map(int, input().split())) for _ in range(N)]

    
    result = common_area(N, rectangles)
    print(f"Case #{i}: {result}")
