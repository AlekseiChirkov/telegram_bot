from aiogram import types

from loader import dp


@dp.message_handler(commands=['what_for'])
async def main_questions(message: types.Message):
    await message.reply(
        'Зачем нужна система маркировки?\n\n'
        'Будущее — это цифровые технологии, системы объединения данных, которые будут использоваться для'
        'отслеживания и диагностики проблем в здравоохранении, сельском хозяйстве, легкой промышленности и окружающей' 
        'среде, а также для выполнения повседневных задач. Технологии, функционирующие на основе анализа данных,' 
        'будут способны обеспечить расширение прав и возможностей людей, улучшение благосостояния человека.\n\nПроблема' 
        'нелегальной продукции остается крайне острой для России: доля незаконного оборота в легкой промышленности' 
        'достигает 35%, на парфюмерном рынке 20%, на рынке лекарственных средств до 10%.\n\nВ этом году обязательная'
        'маркировка коснётся шести категорий товаров: лекарства, обувь, фототовары, шины и покрышки, парфюмерия и'
        'табак. Маркировка призвана защитить покупателей от контрафактной продукции и помочь повысить уплату налогов,' 
        'поскольку вытеснит с рынка недобросовестных налогоплательщиков.\n\nВ декабре 2017 г. Президент РФ В. Путин'
        'одобрил решение правительства о создании до 2024 г. национальной системы цифровой маркировки товаров на базе' 
        'Центра развития перспективных технологий (ЦРПТ).\n\nЦРПТ является совместным проектом ЮСМ («ЮэСэМ Технологии»,' 
        '50%), госкорпорации Ростех (концерн «Автоматика», 25%) и «Элвис-Плюс групп» (25%).\n\nЦифровая маркировка'
        'позволит бизнесу повысить производительность, совершенствовать логистические схемы, нарастить долю рынка и в'
        'конечном счете увеличить выручку:\n\n1. За счет снижения доли контрабанды и контрафакта легальные '
        'производители'
        'увеличат долю и объемы производства на 5-50% в зависимости от товарной группы.\n2. Бизнес сможет перевести'
        'производство на Индустрию 4.0, на работу по принципу Just-in-Time. Получая в режиме онлайн данные о движении'
        'продукции, он будет оптимально планировать производство, снижать запасы и повышать оборачиваемость продукции.' 
        '\n3. Подключение к оператору электронного документооборота (если в ЭДО ранее не работали).\n4. Бизнес сможет' 
        'существенно экономить на логистике: при внедрении полного прослеживания получение производителем или'
        'логистической компанией актуального статистического материала о географии, интенсивности, сезонности продаж'
        'позволит перестроить логистические схемы, оптимизировать поставки и складские запасы.\n5. Бизнес наладит учет.' 
        'Сейчас многие предприниматели не имеют собственных данных об остатках и кодах товаров на складах и в'
        'магазинах. Без правильного учета невозможно считать прибыль или планировать закупки, поэтому автоматизация' 
        'поможет в будущем предпринимателям навести порядок в своем бизнесе. \n6. Бизнес перейдет на электронный'
        'документооборот. ЭДО радикально сокращает объем бумажных документов, которыми до сих пор активно обмениваются'
        'между собой российские компании, снизит издержки бизнеса и повысит производительность труда.'
    )
