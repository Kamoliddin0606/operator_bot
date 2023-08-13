import zeep

reasionsReturn = 'http://kit.gloriya.uz:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
client = zeep.Client(wsdl=reasionsReturn)
try:
    user = client.service.GetUserByTelegramID('65946981')
except:
    user = None
print(user)

