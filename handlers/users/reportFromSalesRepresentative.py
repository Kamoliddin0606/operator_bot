from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandPrivacy
from aiogram.dispatcher.filters.state import State
from keyboards.default.menuReports import menuReports
from keyboards.default.menuKeyboard import menu
import zeep
from filters import IsPrivate, IsGroup
from datetime import datetime
from filters.private_chat import IsPrivate
from loader import dp, bot
from states.reportFromSalesRepresentativeStates import reportSR
from data.config import CHATS

@dp.message_handler(IsPrivate(),text='📊 Отправить отчет')
async def startGettingReport(message: types.Message):
   
    reasionsReturn = 'http://kit.gloriya.uz:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
    client = zeep.Client(wsdl=reasionsReturn)
    try:
        user = client.service.GetUserByTelegramID(message.from_user.id)
    except:
        user = None
    
    if user:
        
   
        reasionsReturn = 'http://kit.gloriya.uz:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
        client = zeep.Client(wsdl=reasionsReturn)
        
            
        telegramuser = client.service.GetUserByTelegramID(message.from_user.id)
        
        name  = telegramuser["Name"]
        
        userCode = telegramuser['Code']

        kpi = client.service.GetKPI(userCode)
        totalPlan = kpi["TotalPlan"]
        totalFact = kpi["TotalFact"]
        totalPercent = kpi["TotalPercent"]
        totalForecast = kpi["TotalForecast"]
        totalpercentForecast = kpi["TotalPercentForecastFact"]

        okb = kpi["OKB"]
        akbplan = kpi["AKBPlan"]
        akbfact = kpi["AKBFact"]
        akbpercent = kpi["AKBPercent"]

        #AKB

        reportData = client.service.GetDailyReport(userCode)
        biznesRegionlar = ""
        bizregionlarnomlari = ""

        for dict in reportData['BusinessRegionReportRow']:
            biznesRegionlar+="\n<i>"+dict['Name']+"  --  "+str(int(dict['AKB']))+"т.т.</i>"
            bizregionlarnomlari+=f'{dict["Name"], }'

        akbKotegory = ''
        for dict in reportData['AKBByCotegoriesRow']:
            akbKotegory+="\n<i>"+dict['Name']+"  --  "+str(int(dict['AKB']))+"т.т.</i>"
           

        okb = int(reportData["CountOKB"])
        akb = int(reportData["CountAKB"])
        if reportData['CountVisited']:
            countVisited = int(reportData['CountVisited'])
        else: 
            countVisited=0
        cash = reportData['Cash']
        transfer = reportData['Transfer']
        sum = reportData['Sum']
        
        if cash ==None:
            cash = 0
        if transfer == None:
            transfer = 0
        if sum==None:
            sum = 0


        answer =f"""
#dailyReport
📅 Дата: {str(datetime.now().day)+'-'+str(datetime.now().month)+"-"+str(datetime.now().year)+"  "+str(datetime.now().hour)+':'+ str(datetime.now().minute)+':'+str(int(datetime.now().second))}
🙎🏻‍♂️ ФИО: {name}

<b>Территория</b> : {bizregionlarnomlari}<i></i> 

<b>ОКБ и АКБ:</b>

<i>ОКБ по территории --  {okb} т.т.</i>
<i>Количество посещенных торговых точек  --  {countVisited} т.т.</i>
<i>Активные клиенты сегодня  --  {akb} т.т.</i>


<b>Разделение АКБ по регионам:</b>
{biznesRegionlar}

<b>Общая стоимость заказов:</b>

<i>Наличные  --  {cash} Сум</i>
<i>Безналичка  --  {transfer} Cум</i>
<i>Общая сумма заказов  --  {sum} Cум</i>

<b>АКБ по категориям товаров:</b>
{
    akbKotegory
}


✿•┈┈┈┈••ৡ❀ৡ•┈┈┈┈•✿

📊 <b>Ежемесячный план и общие результаты на {str(datetime.now().day)+'-'+str(datetime.now().month)+"-"+str(datetime.now().year)+"  "+str(datetime.now().hour)+':'+ str(datetime.now().minute)+':'+str(int(datetime.now().second))}</b>

<b>План и факт:</b>

<i>План  --  {round(totalPlan,2)} Cум</i>
<i>Факт  --  {round(totalFact,2)} Cум</i>
<i>Факт в процентах  --  {round(totalPercent,2)}%</i>
<i>Прогноз  --  {round(totalForecast,2)} Cум</i>
<i>Прогноз в процентах  --  {round(totalpercentForecast,2)}%</i>

<b>ОКБ и АКБ:</b>

<i>ОКБ  --  {okb} т.т.</i>
<i>АКБ план  --  {akbplan} т.т.</i>
<i>АКБ факт  --  {akbfact} т.т.</i>
<i>АКБ в процентах --  {round(akbpercent,2)}%</i>

"""
        if IsPrivate():
           chat =await bot.get_chat(-1001910673296)
           
           if chat.username:
               await message.answer(f'Ваш отчет отправлен в группу "{chat.title} @{chat.username}".\n\n {answer}')
           else:    
                await message.answer(f'Ваш отчет отправлен в группу "{chat.title}".\n\n {answer}')
           
           await bot.send_message(chat_id=-1001910673296, message_thread_id=2,text=answer, reply_markup=menu)
        
    else:
        # await message.reply_photo(photo="https://drive.google.com/file/d/1sa7LwhCITfX9CRpyYh6ZnMm1ixRgJxah/view?usp=sharing", caption='test')
        await message.reply("‼️ Вы не можете отправить отчет: \n\n 1️⃣ Вы не торговый представитель \n\n 2️⃣ Вы не зарегистрированы в программе")

       