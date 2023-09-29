import zeep
from zeep import settings
import time

from zeep.plugins import HistoryPlugin
from zeep import Client, Settings
from zeep.transports import Transport
from lxml import etree

settings = Settings(strict=False, xml_huge_tree=True)
history = HistoryPlugin()
transport = Transport(timeout=10)
reasionsReturn = 'http://192.168.1.241:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
# client = zeep.Client(wsdl=reasionsReturn)
client = Client(wsdl=reasionsReturn, transport=transport, plugins=[history], settings=settings)

users = [
"000000062",
"000000291",
"000000115",
"000000333",
"000000266",
"000000185",
"000000279",
"000000281",
"000000330",
"000000230",
"000000331",
"000000348",
"000000336",
"000000326",
"000000082",
"000000338",
"000000211",
"000000429",
"000000346",
"000000351",
"000000058",
"000000089",
"000000340",
"000000226",
"000000248",
"000000327",
"000000186",
"000000242",
"000000267",
"000000245",
"000000144",
"000000272",
"000000282",
"000000243",
"000000117",
"000000060",
"000000166",
"000000274",
"000000350",
"000000059",
"000000298",
"000000137",
"000000219",
"000000294",
"000000329",
"000000347",
"000000237",
"000000174",
"000000220",
"000000328",
"000000168",
"000000334",
"000000149",
"000000116",
"000000303",
"000000167",
"000000368",
"000000370",
"000000118",
"000000258",
"000000339",
"000000221",
"000000214",
"000000396",
"000000349",
"000000335",
"000000227",
"000000337",
"000000286",
"000000188",
"000000055",
"000000324",
"000000311",
"000000325",
"000000332",
"000000189",
"000000436",
"000000423",
"000000184",


"000000146",

"000000061"
]
users_clean =[]
count = 0
for userkod in users:
    count+=1
    try:
        
        user = client.service.GetDailyReport(userkod)

        
        print(user, "\n count: "+str(count))
        
        time.sleep(1)
    except Exception as e:
        print( "count: "+str(count),e)
        users_clean.append(userkod)
# for userkod in users:
#     count+=1
#     try:
        
#         user = client.service.GetDailyReport(userkod)

        
#         print(user['Cash'], "count: "+str(count))
        
#         # time.sleep(1)
#     except Exception as e:
#         print( "count: "+str(count),e)
#         users_clean.append(userkod)
    
print(users_clean)

