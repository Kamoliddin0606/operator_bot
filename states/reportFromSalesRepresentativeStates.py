from aiogram.dispatcher.filters.state import StatesGroup, State

class reportSR(StatesGroup):
    territory = State()
    totalClientTerritory = State()
    activeClients = State()
    
    transfer = State()
    cash = State()
    
    hardSoap = State()
    softSoap = State()
    
    evyBaby = State()
    babyOne = State()

    arko = State()
    deoEmotion = State()
    deoBlade = State()