import socket


def checkInternet(host="8.8.8.8", port=53, timeout=30):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        print(ex)
        return False


def inTolerance(num1, num2, tolerance) -> bool:
    return abs(num1 - num2) <= tolerance


def inPercentTolerance(num1, num2, tolerance) -> bool:
    return abs(1 - (num1 / num2)) <= tolerance


def ProRateValue(value, inRange, outRange):
    return value * abs(outRange[1] - outRange[0]) / abs(inRange[1] - inRange[0])


def Bind(val, inRange):
    return min(inRange[1], max(inRange[0], val))


def UtilsUnitTest():
    print(inTolerance(100, 110, 15))
    print(inPercentTolerance(100, 110, 0.15))
    print(ProRateValue(5, (0, 10), (0, 100)))
    print(Bind(110, (0, 100)))


def sign(num):
    return int(num / abs(num)) if num != 0 else 0


if __name__ == "__main__":
    UtilsUnitTest()
