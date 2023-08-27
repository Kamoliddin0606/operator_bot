import zeep

reasionsReturn = 'http://kit.gloriya.uz:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
client = zeep.Client(wsdl=reasionsReturn)

user = client.service.GetDailyReport('000000267')

print(user)

