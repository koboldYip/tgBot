# keyboards.py (название файла должно быть именно таким, чтобы работало "import keyboards")

from telebot import types # Правильный импорт для объектов типов Telegram

# --- Функции для создания различных клавиатур ---

def main_menu():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="• Финансы", callback_data="button1")
    button2 = types.InlineKeyboardButton(text="• Быт и хозяйство", callback_data="button2")
    button3 = types.InlineKeyboardButton(text="• Юридическая безопасность", callback_data="button3")
    button4 = types.InlineKeyboardButton(text="• С чего начать?", callback_data="button4")
    # Добавляем кнопки в один ряд или в отдельные, как требуется.
    # Если хотим в один ряд (например, 3 кнопки), можно так:
    # keyboard.row(button1, button2, button3)
    # Или по одной, как было изначально (они будут на разных строках):
    keyboard.add(button4)
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    return keyboard



def podkategory1():
    markup = types.InlineKeyboardMarkup(row_width=1) # Каждая кнопка на новой строке
    button1_2 = types.InlineKeyboardButton("• Работа/подработка", callback_data="button1_2")
    button1_3 = types.InlineKeyboardButton("• Оплата ЖКХ", callback_data="button1_3")
    button1_4 = types.InlineKeyboardButton("• Оплата налогов", callback_data="button1_4")
    back_button = types.InlineKeyboardButton("Назад", callback_data="back_to_main")
    markup.add(button1_2, button1_3, button1_4, back_button)
    return markup

def podkategory2():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button2_1 = types.InlineKeyboardButton("• Стирка", callback_data="button2_1")
    button2_2 = types.InlineKeyboardButton("• Уборка", callback_data="button2_2")
    button2_3 = types.InlineKeyboardButton("• Готовка", callback_data="button2_3")
    button2_4 = types.InlineKeyboardButton("• Глаженье", callback_data="button2_4")
    back_button = types.InlineKeyboardButton("Назад", callback_data="back_to_main")
    markup.add(button2_1, button2_2, button2_3, button2_4, back_button)
    return markup

def podkategory3():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button3_1 = types.InlineKeyboardButton("• Договоры", callback_data="button3_1")
    button3_2 = types.InlineKeyboardButton("• Аренда", callback_data="button3_2") # Исправлен текст кнопки
    back_button = types.InlineKeyboardButton("Назад", callback_data="back_to_main")
    markup.add(button3_1, button3_2, back_button)
    return markup


def podkategoryGKH_FIN():
    markup = types.InlineKeyboardMarkup(row_width=1) # Каждая кнопка на новой строке
    buttonKAK_SNIM = types.InlineKeyboardButton("• Как снимать показания?", callback_data="buttonKAK_SNIM")
    button_OPL = types.InlineKeyboardButton("• Как оплачивать?", callback_data="button_OPL")
    back_button = types.InlineKeyboardButton("Назад", callback_data="button1")
    markup.add(buttonKAK_SNIM, button_OPL, back_button)
    return markup


def podkategory_WORK():
    markup = types.InlineKeyboardMarkup(row_width=1) # Каждая кнопка на новой строке
    buttonPOISK_WORK = types.InlineKeyboardButton("• Поиск работы", callback_data="buttonPOISK_WORK")
    buttonOBAZ_W = types.InlineKeyboardButton("• Права и обязанности", callback_data="buttonOBAZ_W")
    buttonYVOL_WORK = types.InlineKeyboardButton("• Увольнение", callback_data="buttonYVOL_WORK")
    back_button = types.InlineKeyboardButton("Назад", callback_data="button1")
    markup.add(buttonPOISK_WORK, buttonOBAZ_W, buttonYVOL_WORK, back_button)
    return markup


def podkategoryO_NALOG():
    markup = types.InlineKeyboardMarkup(row_width=1) # Каждая кнопка на новой строке
    buttonV_NALOG = types.InlineKeyboardButton("• Виды налогов", callback_data="buttonV_NALOG")
    buttonOPL_NALOG = types.InlineKeyboardButton("• Оплата налогов", callback_data="buttonOPL_NALOG")
    back_button = types.InlineKeyboardButton("Назад", callback_data="button1")
    markup.add(buttonV_NALOG, buttonOPL_NALOG, back_button)
    return markup

def podkategory_GLAGKA():
    markup = types.InlineKeyboardMarkup(row_width=1) # Каждая кнопка на новой строке
    buttonGL_PODGOT = types.InlineKeyboardButton("• Подготовка", callback_data="buttonGL_PODGOT")
    button_POSLED = types.InlineKeyboardButton("• Последовательность", callback_data="button_POSLED")
    button_TEXNIKA = types.InlineKeyboardButton("• Техника", callback_data="button_TEXNIKA")
    button_SOVETIKS = types.InlineKeyboardButton("• Советы", callback_data="button_SOVETIKS")
    back_button = types.InlineKeyboardButton("Назад", callback_data="button2")
    markup.add(buttonGL_PODGOT, button_POSLED, button_TEXNIKA, button_SOVETIKS, back_button)
    return markup


def podkategory_STIRKA():
    markup = types.InlineKeyboardMarkup(row_width=1) # Каждая кнопка на новой строке
    button_PODGOT = types.InlineKeyboardButton("• Подготовка вещей", callback_data="button_PODGOT")
    button_SORT = types.InlineKeyboardButton("• Сортировка вещей", callback_data="button_SORT")
    button_MOU_SRED = types.InlineKeyboardButton("• Моющие средстава", callback_data="button_MOU_SRED")
    button_REGIM = types.InlineKeyboardButton("• Режимы стирки", callback_data="button_REGIM")
    button_RYKAMI = types.InlineKeyboardButton("• Ручная стирка", callback_data="button_RYKAMI")
    button_POSLE = types.InlineKeyboardButton("• После стирки", callback_data="button_POSLE")
    button_SOVETIKI = types.InlineKeyboardButton("• Советы", callback_data="button_SOVETIKI")
    back_button = types.InlineKeyboardButton("Назад", callback_data="button2")
    markup.add(button_PODGOT, button_SORT, button_MOU_SRED, button_REGIM, button_RYKAMI, button_POSLE, button_SOVETIKI, back_button)
    return markup

def podkategory_FOOD():
    markup = types.InlineKeyboardMarkup(row_width=1) # Каждая кнопка на новой строке
    button_PODGOT_PROD = types.InlineKeyboardButton("• Планирование и подготовка продуктов", callback_data="button_PODGOT_PROD")
    button_PRIGOT = types.InlineKeyboardButton("• Процесс приготовления", callback_data="button_PRIGOT")
    button_OSTATKI = types.InlineKeyboardButton("• Хранение остатков", callback_data="button_OSTATKI")
    button_PROBLEM = types.InlineKeyboardButton("• Проблемы", callback_data="button_PROBLEM")
    back_button = types.InlineKeyboardButton("Назад", callback_data="button2")
    markup.add(button_PODGOT_PROD, button_PRIGOT, button_OSTATKI, button_PROBLEM, back_button)
    return markup

def podkategory_YBORKA():
    markup = types.InlineKeyboardMarkup(row_width=1) # Каждая кнопка на новой строке
    button_PODGOT_YBORKA = types.InlineKeyboardButton("• Подготовка к уборке", callback_data="button_PODGOT_YBORKA")
    button_KITCHEN = types.InlineKeyboardButton("• Кухня", callback_data="button_KITCHEN")
    button_KOMNATA = types.InlineKeyboardButton("• Жилые комнаты", callback_data="button_KOMNATA")
    button_PIL = types.InlineKeyboardButton("• Санузел (ванная и туалет)", callback_data="button_PIL")
    button_FLOOR = types.InlineKeyboardButton("• Пол", callback_data="button_FLOOR")
    button_SOVETI = types.InlineKeyboardButton("• Советы", callback_data="button_SOVETI")
    back_button = types.InlineKeyboardButton("Назад", callback_data="button2")
    markup.add(button_PODGOT_YBORKA, button_KITCHEN, button_KOMNATA, button_PIL, button_FLOOR, button_SOVETI, back_button)
    return markup


def podkategory_ARENDA():
    markup = types.InlineKeyboardMarkup(row_width=1) # Каждая кнопка на новой строке
    buttonPRAVILA_ARENDI = types.InlineKeyboardButton("• Как правильно арендовать", callback_data="buttonPRAVILA_ARENDI")
    buttonDOGOVOR = types.InlineKeyboardButton("• Подписание договора", callback_data="buttonDOGOVOR")
    buttonKLCH_MOMENT = types.InlineKeyboardButton("• Ключевые моменты", callback_data="buttonKLCH_MOMENT")
    buttonNEDVIG = types.InlineKeyboardButton("• Недвижимость", callback_data="buttonNEDVIG")
    buttonTRANSPORT = types.InlineKeyboardButton("• Транспорт", callback_data="buttonTRANSPORT")
    buttonOBORUD = types.InlineKeyboardButton("• Оборудование и инструменты", callback_data="buttonOBORUD")
    back_button = types.InlineKeyboardButton("Назад", callback_data="button3")
    markup.add(buttonPRAVILA_ARENDI, buttonDOGOVOR, buttonKLCH_MOMENT, buttonNEDVIG, buttonTRANSPORT, buttonOBORUD, back_button)
    return markup


def podkategoryOplVid_NALOG():
    markup = types.InlineKeyboardMarkup(row_width=1) # Каждая кнопка на новой строке
    button_SAMOZAN = types.InlineKeyboardButton("• Самозанятый", callback_data="button_SAMOZAN")
    buttonNALOG_IMYH = types.InlineKeyboardButton("• на Имущество", callback_data="buttonNALOG_IMYH")
    buttonNALOG_NEPLAT = types.InlineKeyboardButton("• Неуплата", callback_data="buttonNALOG_NEPLAT")
    back_button = types.InlineKeyboardButton("Назад", callback_data="button1_4")
    markup.add(button_SAMOZAN, buttonNALOG_IMYH, buttonNALOG_NEPLAT, back_button)
    return markup


def podkategoryOplVid_GKH():
    markup = types.InlineKeyboardMarkup(row_width=1) # Каждая кнопка на новой строке
    button_BANK = types.InlineKeyboardButton("• Банковское приложение", callback_data="button_BANK")
    button_GOSYS = types.InlineKeyboardButton("• Госуслуги или ГИС ЖКХ", callback_data="button_GOSYS")
    button_SAIT = types.InlineKeyboardButton("• Сайт управляющей компании (УК)", callback_data="button_SAIT")
    back_button = types.InlineKeyboardButton("Назад", callback_data="button1_3")
    markup.add(button_BANK, button_GOSYS, button_SAIT, back_button)
    return markup