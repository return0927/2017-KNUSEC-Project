#  [truncated]Cookie: __cfduid=d230cec387ee659ea5ecb3176cc5e5f151506260007; lc=ko_KR; _gat=1; G_ENABLED_IDPS=google; G_AUTHUSER_H=0; prevpage=http%3A//kkutu.co.kr/; kkutukorea=s%3AK6DmiNnVyWLeBANLOXrogO6bPHmQYezX.fkCwusvA%2F4GgoO%2BEbKyXw51c

_STRING = input()
_STRING = _STRING.replace(" [truncated]Cookie: ","").split("; ")

_COOKIE = {}

for _LINE in _STRING:
    _TEMP = _LINE.split("=")
    _COOKIE[_TEMP[0]] = "=".join(_TEMP[1:])

for n in _COOKIE:
    print(n, _COOKIE[n])

"""
[
{
    "domain": ".kkutu.co.kr",
    "expirationDate": 1537201620,
    "hostOnly": false,
    "httpOnly": true,
    "name": "__cfduid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "d230cec387ee659ea5ecb3176cc5e5f151506260007",
    "id": 1
},
{
    "domain": ".kkutu.co.kr",
    "expirationDate": 1569332160,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_ga",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.3.203387505.1506260014",
    "id": 2
},
{
    "domain": ".kkutu.co.kr",
    "expirationDate": 1506346560,
    "hostOnly": false,
    "httpOnly": false,
    "name": "_gid",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "GA1.3.272047475.1506260163",
    "id": 3
},
{
    "domain": ".kkutu.co.kr",
    "expirationDate": 253402257600,
    "hostOnly": false,
    "httpOnly": false,
    "name": "G_ENABLED_IDPS",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "google",
    "id": 4
},
{
    "domain": ".kkutu.co.kr",
    "expirationDate": 1506346560,
    "hostOnly": false,
    "httpOnly": true,
    "name": "kkutukorea",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": false,
    "storeId": "0",
    "value": "s%3A8x98LFy5yEk0oMpskkx7X6muktltnqWC.fPzlzL8XmrvxXmvVMjln2UGNJEhEzBpIoF6JkdddXFE",
    "id": 5
},
{
    "domain": "kkutu.co.kr",
    "hostOnly": true,
    "httpOnly": false,
    "name": "lc",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "ko_KR",
    "id": 6
},
{
    "domain": "kkutu.co.kr",
    "hostOnly": true,
    "httpOnly": false,
    "name": "test",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": false,
    "session": true,
    "storeId": "0",
    "value": "",
    "id": 7
}
]"""
