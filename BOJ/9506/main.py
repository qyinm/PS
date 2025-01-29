while True:
    n = int(input())
    if n == -1:
        break
    el = []
    p = n
    for i in range(1, n):
        if n % i == 0:
            p -= i
            el.append(str(i))
    s = " + ".join(el)
    if p != 0:
        print(f"{n} is NOT perfect.")
    else:
        print(f"{n} = {s}")