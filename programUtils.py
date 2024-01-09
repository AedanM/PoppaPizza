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
        
def inTolerance(num1,num2, tolerance):
    return abs(num1-num2) <= tolerance

def inPercentTolerance(num1,num2, tolerance):
    return abs(1-(num1/num2)) <= tolerance


