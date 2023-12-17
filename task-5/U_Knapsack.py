def knapSack(items, W, weight, value):
    if W == 0 or items == 0:
        return 0
    if weight[items - 1] > W:
        return knapSack(items - 1, W, weight, value)
    sum_items = value[items - 1] + knapSack(items - 1, W - weight[items - 1], weight, value)
    sum = knapSack(items - 1, W, weight, value)
    return max(sum_items, sum)

items, W = map(int, input().split())
weight = []
value = []

for i in range(items):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

result = knapSack(items, W, weight, value)
print(result)
