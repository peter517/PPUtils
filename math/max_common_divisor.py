def gcd(a, b):
    if a < b:
        a, b = b, a

    while b != 0:
        temp = a % b
        a = b
        b = temp

    return a

(a, b) = (1280, 800)

(a, b) = (1920, 1200)
(a, b) = (1366, 768)

mcd = gcd(a, b)

print str(a / mcd) + " " + str(b / mcd)
