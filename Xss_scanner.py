import requests


def XSScanner(url) :

    target = url
    Payloads = ["<image/src/onerror=prompt(8)>",
    "<img/src/onerror=prompt(8)",
    "<script>alert(XSS);</script>"
    ]

    mes = ""
    for payload in Payloads :

        req = requests.post(target + payload)
        if payload in req.text:
            mes += "XSS vulnerability discovered" + " >> Attacking payload : "+ payload + "\n"
            return mes
        else:
            mes += "testing payload : "+ payload +">>> Secure"+"\n"
    return mes
