def majority_element(elements):
    candidate = None
    count = 0
    for e in elements:
        if count == 0:
            candidate = e
        count += (1 if e == candidate else -1)
    if elements.count(candidate) > len(elements) / 2:
        return 1
    else:
        return 0
if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))