
import zeep


def divide_and_split(number):
  """
  Разделяет многозначное число на 3 с пробелами.

  Args:
    number: Число.

  Returns:
    Строка с разделенным числом.
  """

  number_str = str(number)
  number_strlist = number_str.split(".")
  number_str1 = number_strlist[0][::-1]
  number_str2 = number_strlist[1]

  numbers = []
  for i in range(0, len(number_str1), 3):
    numbers.append(number_str1[i:i + 3])
  numbersRevorse = []
  
  for i in range(len(numbers)-1,-1,-1):
    numbersRevorse.append(numbers[i][::-1])
  
  final =  " ".join(numbersRevorse)
  final+="."+number_str2
  return final


reasionsReturn = 'http://kit.gloriya.uz:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
client = zeep.Client(wsdl=reasionsReturn)

userReport = client.service.GetDailyReport('000000429')
cash = str(userReport['Cash'])
print(divide_and_split(userReport['Cash']))
print(cash)