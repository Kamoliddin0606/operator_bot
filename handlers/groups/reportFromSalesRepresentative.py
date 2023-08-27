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
@dp.message_handler(IsGroup(),commands='report')
@dp.message_handler(IsGroup(),text='📊 Отправить отчет')
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
            biznesRegionlar+="\n<i>"+dict['Name']+" --  "+str(int(dict['AKB']))+"т.т.</i>"
            bizregionlarnomlari+=f'{dict["Name"], }'

        akbKotegory = ''
        for dict in reportData['AKBByCotegoriesRow']:
            akbKotegory+="\n<i>"+dict['Name']+" --  "+str(int(dict['AKB']))+"т.т.</i>"
           

        okb = int(reportData["CountOKB"])
        akb = int(reportData["CountAKB"])

        cash = reportData['Cash']
        transfer = reportData['Transfer']
        sum = reportData['Sum']


        answer =f"""
#dailyReport
📅 Дата: {str(datetime.now().day)+'-'+str(datetime.now().month)+"-"+str(datetime.now().year)+"  "+str(datetime.now().hour)+':'+ str(datetime.now().minute)+':'+str(int(datetime.now().second))}
🙎🏻‍♂️ ФИО: {name}

<b>Территория</b> : {bizregionlarnomlari}<i></i> 

<b>Общее количество ОКБ и АКБ по вышеуказанным направлениям деятельности:</b>

<i>ОКБ по территории --  {okb}т.т.</i>
<i>АКБ сработанно       --  {akb}т.т.</i>

<b>Разделение АКБ по регионам:</b>
{biznesRegionlar}

<b>Общая стоимость заказов:</b>

<i>Наличные       --  {cash}т.т.</i>
<i>Безналичка       --  {transfer}т.т.</i>
<i>Общая сумма заказов       --  {sum}т.т.</i>

<b>АКБ по категориям товаров:</b>
{
    akbKotegory
}


✿•┈┈┈┈••ৡ❀ৡ•┈┈┈┈•✿

📊 <b>Ежемесячный план и общие результаты на {str(datetime.now().day)+'-'+str(datetime.now().month)+"-"+str(datetime.now().year)+"  "+str(datetime.now().hour)+':'+ str(datetime.now().minute)+':'+str(int(datetime.now().second))}</b>

<b>План и факт:</b>

<i>План                -- {totalPlan}</i>
<i>Факт                -- {totalFact}</i>
<i>Факт в процентах    -- {totalPercent}%</i>
<i>Прогноз             -- {totalForecast}</i>
<i>Прогноз в процентах -- {totalpercentForecast}%</i>

<b>ОКБ и АКБ:</b>

<i>ОКБ             -- {okb}</i>
<i>АКБ план        -- {akbplan}</i>
<i>АКБ факт        -- {akbfact}</i>
<i>АКБ в процентах -- {akbpercent}%</i>

"""
        if message.is_topic_message:

            await bot.send_message(chat_id=message.chat.id, message_thread_id=message.message_thread_id,text=answer, reply_markup=menu)
        elif IsGroup():
            await message.answer(answer)
    else:
        # await message.reply_photo(photo="https://drive.google.com/file/d/1sa7LwhCITfX9CRpyYh6ZnMm1ixRgJxah/view?usp=sharing", caption='test')
        await message.reply("‼️ Вы не можете отправить отчет: \n\n 1️⃣ Вы не торговый представитель \n\n 2️⃣ Вы не зарегистрированы в программе")

    