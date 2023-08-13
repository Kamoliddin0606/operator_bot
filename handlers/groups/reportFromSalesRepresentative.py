from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command  
from aiogram.dispatcher.filters.state import State
from keyboards.default.menuReports import menuReports
from keyboards.default.menuKeyboard import menu
import zeep
from datetime import datetime

from loader import dp
from states.reportFromSalesRepresentativeStates import reportSR

@dp.message_handler(text='📊 Send a report')
async def startGettingReport(message: types.Message):
    reasionsReturn = 'http://kit.gloriya.uz:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
    client = zeep.Client(wsdl=reasionsReturn)
    try:
        user = client.service.GetUserByTelegramID(message.from_user.id)
    except:
        user = None
    
    if user:
        await message.reply("<b>📈 Уважаемый "+message.from_user.full_name+', приступаем к созданию отчета!!!</b> \n\n  ‼️ Ответьте на вопросы бота, чтобы правильно сгенерировать отчет \n\n <b>Введите территории (через запятую):</b>',reply_markup=menuReports)
        await reportSR.territory.set()
    else:
        # await message.reply_photo(photo="https://drive.google.com/file/d/1sa7LwhCITfX9CRpyYh6ZnMm1ixRgJxah/view?usp=sharing", caption='test')
        await message.reply("‼️ Вы не можете отправить отчет: \n\n 1️⃣ Вы не торговый представитель \n\n 2️⃣ Вы не зарегистрированы в программе")
# previous

@dp.message_handler(text='⬅️ previous', state = reportSR.territory)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()


@dp.message_handler(text='⬅️ previous', state = reportSR.totalClientTerritory)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("<b>📈 Уважаемый "+message.from_user.full_name+', приступаем к созданию отчета!!!</b> \n\n  ‼️ Ответьте на вопросы бота, чтобы правильно сгенерировать отчет \n\n <b>Введите территории (через запятую):</b>',reply_markup=menuReports)
    await reportSR.territory.set()

@dp.message_handler(text='⬅️ previous', state = reportSR.activeClients)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.answer("<b>ОКБ по территории:</b>")
    await reportSR.totalClientTerritory.set()

@dp.message_handler(text='⬅️ previous', state = reportSR.transfer)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.answer("<b>АБК сработанно:</b>")
    await reportSR.activeClients.set()

@dp.message_handler(text='⬅️ previous', state = reportSR.cash)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.answer("<b>Сумма заказа (перечислением UZS):</b>")
    await reportSR.transfer.set()

@dp.message_handler(text='⬅️ previous', state = reportSR.hardSoap)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.answer("<b>Сумма заказа (налом UZS):</b>")
    await reportSR.cash.set()


@dp.message_handler(text='⬅️ previous', state = reportSR.softSoap)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.answer("<b>Твердое мыло (АКБ):</b>")
    await reportSR.hardSoap.set()

@dp.message_handler(text='⬅️ previous', state = reportSR.evyBaby)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.answer("<b>Жидкое мыло (АКБ):</b>")
    await reportSR.softSoap.set()

@dp.message_handler(text='⬅️ previous', state = reportSR.babyOne)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.answer("<b>EVY BABY (АКБ):</b>")
    await reportSR.evyBaby.set()

@dp.message_handler(text='⬅️ previous', state = reportSR.arko)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.answer("<b>BABY ONE (АКБ):</b>")
    await reportSR.babyOne.set()
@dp.message_handler(text='⬅️ previous', state = reportSR.deoEmotion)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.answer("<b>ARKO (АКБ):</b>")
    await reportSR.arko.set()

@dp.message_handler(text='⬅️ previous', state = reportSR.deoBlade)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.answer("<b>DEO EMOTION (АКБ):</b>")
    await reportSR.deoEmotion.set()

# previous
# cencel

@dp.message_handler(text='❌ Cancel report', state = reportSR.territory)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()


@dp.message_handler(text='❌ Cancel report', state = reportSR.totalClientTerritory)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()

@dp.message_handler(text='❌ Cancel report', state = reportSR.activeClients)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()

@dp.message_handler(text='❌ Cancel report', state = reportSR.transfer)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()

@dp.message_handler(text='❌ Cancel report', state = reportSR.cash)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()

@dp.message_handler(text='❌ Cancel report', state = reportSR.hardSoap)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()


@dp.message_handler(text='❌ Cancel report', state = reportSR.softSoap)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()

@dp.message_handler(text='❌ Cancel report', state = reportSR.evyBaby)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()

@dp.message_handler(text='❌ Cancel report', state = reportSR.babyOne)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()

@dp.message_handler(text='❌ Cancel report', state = reportSR.arko)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()
@dp.message_handler(text='❌ Cancel report', state = reportSR.deoEmotion)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()

@dp.message_handler(text='❌ Cancel report', state = reportSR.deoBlade)
async def cencelReport(message: types.Message, state:FSMContext):
    await message.reply("Отчет отменен", reply_markup=menu)
    await state.finish()

# cencel

@dp.message_handler(state = reportSR.territory)
async def answer_territory(message:types.Message, state:FSMContext):
    territory = message.text
    await state.update_data(
        {'territory': territory}
        )   
    
    await message.answer("<b>ОКБ по территории:</b>")
    await reportSR.next()
    

@dp.message_handler(state = reportSR.totalClientTerritory)
async def answer_totalClient(message:types.Message, state:FSMContext):
    totalClientTerritory = message.text
    if str(totalClientTerritory).isnumeric():

        await state.update_data(
            {'totalClientTerritory': totalClientTerritory}
            )   
        
        await message.answer("<b>АБК сработанно:</b>")
        await reportSR.next()
    else:
        await message.reply("❌ <i>"+totalClientTerritory+ "</i> \n<b>Вводить нужно только цифрами!! \n\n Повторно введите:</b>")

@dp.message_handler(state = reportSR.activeClients)
async def answer_activeClient(message:types.Message, state:FSMContext):
    activeClient = message.text
    if str(activeClient).isnumeric():

        await state.update_data(
            {'activeClient': activeClient}
            )   
        
        await message.answer("<b>Сумма заказа (перечислением UZS):</b>")
        await reportSR.next()
    else:
        await message.reply("❌ <i>"+activeClient+ "</i> \n<b>Вводить нужно только цифрами!! \n\n Повторно введите:</b>")

@dp.message_handler(state = reportSR.transfer)
async def answer_transfer(message:types.Message, state:FSMContext):
    transfer = message.text
    if str(transfer).isnumeric():

        await state.update_data(
            {'transfer': transfer}
            )   
        
        await message.answer("<b>Сумма заказа (налом UZS):</b>")
        await reportSR.next()
    else:
        await message.reply("❌ <i>"+transfer+ "</i> \n<b>Вводить нужно только цифрами!! \n\n Повторно введите:</b>")


@dp.message_handler(state = reportSR.cash)
async def answer_transfer(message:types.Message, state:FSMContext):
    cash = message.text
    if str(cash).isnumeric():

        await state.update_data(
            {'cash': cash}
            )   
        
        await message.answer("<b>Твердое мыло (АКБ):</b>")
        await reportSR.next()
    else:
        await message.reply("❌ <i>"+cash+ "</i> \n<b>Вводить нужно только цифрами!! \n\n Повторно введите:</b>")


@dp.message_handler(state = reportSR.hardSoap)
async def answer_transfer(message:types.Message, state:FSMContext):
    hardSoap = message.text
    if str(hardSoap).isnumeric():

        await state.update_data(
            {'hardSoap': hardSoap}
            )   
        
        await message.answer("<b>Жидкое мыло (АКБ):</b>")
        await reportSR.next()
    else:
        await message.reply("❌ <i>"+hardSoap+ "</i> \n<b>Вводить нужно только цифрами!! \n\n Повторно введите:</b>")

@dp.message_handler(state = reportSR.softSoap)
async def answer_transfer(message:types.Message, state:FSMContext):
    softSoap = message.text
    if str(softSoap).isnumeric():

        await state.update_data(
            {'softSoap': softSoap}
            )   
        
        await message.answer("<b>EVY BABY (АКБ):</b>")
        await reportSR.next()
    else:
        await message.reply("❌ <i>"+softSoap+ "</i> \n<b>Вводить нужно только цифрами!! \n\n Повторно введите:</b>")

@dp.message_handler(state = reportSR.evyBaby)
async def answer_transfer(message:types.Message, state:FSMContext):
    evyBaby = message.text
    if str(evyBaby).isnumeric():

        await state.update_data(
            {'evyBaby': evyBaby}
            )   
        
        await message.answer("<b>BABY ONE (АКБ):</b>")
        await reportSR.next()
    else:
        await message.reply("❌ <i>"+evyBaby+ "</i> \n<b>Вводить нужно только цифрами!! \n\n Повторно введите:</b>")


@dp.message_handler(state = reportSR.babyOne)
async def answer_transfer(message:types.Message, state:FSMContext):
    babyOne = message.text
    if str(babyOne).isnumeric():

        await state.update_data(
            {'babyOne': babyOne}
            )   
        
        await message.answer("<b>ARKO (АКБ):</b>")
        await reportSR.next()
    else:
        await message.reply("❌ <i>"+babyOne+ "</i> \n<b>Вводить нужно только цифрами!! \n\n Повторно введите:</b>")

@dp.message_handler(state = reportSR.arko)
async def answer_transfer(message:types.Message, state:FSMContext):
    arko = message.text
    if str(arko).isnumeric():

        await state.update_data(
            {'arko': arko}
            )   
        
        await message.answer("<b>DEO EMOTION (АКБ):</b>")
        await reportSR.next()
    else:
        await message.reply("❌ <i>"+arko+ "</i> \n<b>Вводить нужно только цифрами!! \n\n Повторно введите:</b>")


@dp.message_handler(state = reportSR.deoEmotion)
async def answer_transfer(message:types.Message, state:FSMContext):
    deoEmotion = message.text
    if str(deoEmotion).isnumeric():

        await state.update_data(
            {'deoEmotion': deoEmotion}
            )   
        
        await message.answer("<b>DEO BLADE (АКБ):</b>")
        await reportSR.next()
    else:
        await message.reply("❌ <i>"+deoEmotion+ "</i> \n<b>Вводить нужно только цифрами!! \n\n Повторно введите:</b>")
@dp.message_handler(state = reportSR.deoBlade)
async def answer_transfer(message:types.Message, state:FSMContext):
    deoBlade = message.text
    # name = None
    # totalPlan = None
    # totalFact = None
    # totalPercent = None
    # totalForecast = None
    # totalpercentForecast = None

    # okb = None
    # akbplan = None
    # akbfact = None
    # akbpercent = None
    if str(deoBlade).isnumeric():
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
       
        await state.update_data(
            {'deoBlade': deoBlade}
            )   
        
        
        
        data = await state.get_data()
        territory = data.get("territory")
        totalClientTerritory = data.get("totalClientTerritory")
        activeClient = data.get("activeClient")
        transfer = data.get("transfer")
        cash = data.get("cash")
        hardSoap = data.get("hardSoap")
        softSoap = data.get("softSoap")
        evyBaby = data.get("evyBaby")
        babyOne = data.get("babyOne")
        arko = data.get("arko")
        deoEmotion = data.get("deoEmotion")
        deoBlade = data.get("deoBlade")

        answer =f"""
#dailyReport
📅 Дата: {str(datetime.now().day)+'-'+str(datetime.now().month)+"-"+str(datetime.now().year)+"  "+str(datetime.now().hour)+':'+ str(datetime.now().minute)+':'+str(int(datetime.now().second))}
🙎🏻‍♂️ ФИО: {name}

<b>Территория</b> : <i>{territory}</i> 

<i>ОКБ по территории -- {totalClientTerritory} т.т.</i>
<i>АБК сработанно       -- {activeClient} т.т.</i>

<b>Заказ принят на сумму:</b>

<i>Перечислением -- {transfer} UZS</i> 
<i>Налом              -- {cash} UZS</i>
<i>Общая сумма заказа за день -- {float(transfer)+float(cash)} UZS</i>

<b>АКБ за день</b>:

<i>Твердое Мыло -- {hardSoap} т.т.</i>
<i>Жидкое мыло  -- {softSoap} т.т. </i>

<b>Подгузники</b>:

<i>EVY BABY        -- {evyBaby} т.т</i>
<i>BАBY ONE       -- {babyOne} т.т.</i>
<i>ARKO              -- {arko} т.т.</i>
<i>DEO EMOTION -- {deoEmotion} т.т.</i>
<i>DEO BLADE     -- {deoBlade} т.т.</i>

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
        await message.answer(answer, reply_markup=menu)
        await state.finish()
    else:
        await message.reply("❌ <i>"+deoBlade+ "</i> \n<b>Вводить нужно только цифрами!! \n\n Повторно введите:</b>")


