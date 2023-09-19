import zeep
from zeep import settings

settings =  settings.Settings(strict=False, xml_huge_tree=True, xsd_ignore_sequence_order=True)
reasionsReturn = 'http://kit.gloriya.uz:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
client = zeep.Client(wsdl=reasionsReturn)

user = client.service.GetDailyReport('000000429')

print(user)

