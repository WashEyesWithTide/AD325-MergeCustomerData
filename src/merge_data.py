def merge_data(customer_data1: list[int], m: int, customer_data2: list[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    pos = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if customer_data1[p1] >= customer_data2[p2]:
            customer_data1[pos] = customer_data1[p1]
            p1 -= 1
        else:
            customer_data1[pos] = customer_data2[p2]
            p2 -= 1
        pos -= 1
    while p2 >= 0:
        customer_data1[pos] = customer_data2[p2]
        p2 -= 1
        pos -= 1

if __name__ == "__main__":
    customer_data1 = [1, 3, 5, 7, 0, 0, 0]
    m = 4
    customer_data2 = [2, 4, 6]
    n = 3
    merge_data(customer_data1, m, customer_data2, n)
    print(customer_data1)