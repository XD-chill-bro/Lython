import requests
urlp3 = "http://www.molottery.com/gameHistory.do?method=p3Printout&order=desc"
urlp4 = "http://www.molottery.com/gameHistory.do?method=p4Printout&order=desc"
urlpb = "http://www.molottery.com/gameHistory.do?method=pbPrintout&order=desc"
urlmm = "http://www.molottery.com/gameHistory.do?method=mmPrintout&order=desc"
urll4l = "http://www.molottery.com/gameHistory.do?method=lflPrintout&order=desc"
urllt = "http://www.molottery.com/gameHistory.do?method=loPrintout&order=desc"
urlsmc = "http://www.molottery.com/gameHistory.do?method=s5Printout&order=desc"
r1 = requests.get(urlp3, allow_redirects=True)
r2 = requests.get(urlp4, allow_redirects=True)
r3 = requests.get(urlpb, allow_redirects=True)
r4 = requests.get(urlmm, allow_redirects=True)
r5 = requests.get(urll4l, allow_redirects=True)
r6 = requests.get(urllt, allow_redirects=True)
r7 = requests.get(urlsmc, allow_redirects=True)
open('p3.xlsx', 'wb').write(r1.content)
open('p4.xlsx', 'wb').write(r2.content)
open('pb.xlsx', 'wb').write(r3.content)
open('mm.xlsx', 'wb').write(r4.content)
open('l4l.xlsx', 'wb').write(r5.content)
open('plt.xlsx', 'wb').write(r6.content)
open('smc.xlsx', 'wb').write(r7.content)