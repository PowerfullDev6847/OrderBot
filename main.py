from config import API_TOKEN
import logging
from db import add_user
from keyboards import markup_tumanlar, markup_cafelar_Urganch, markup_taomlar_Urganch,\
markup_taomlar_Xonqa, markup_cafelar_Xonqa, markup_cafelar_Xiva, markup_taomlar_Xiva,\
markup_cafelar_Gurlan, markup_taomlar_Gurlan, markup_cafelar_Xazorasp, markup_taomlar_Xazorasp,\
markup_taomlar_Xazorasp, markup_cafelar_Xazorasp, markup_cafelar_Shovvot, markup_taomlar_Shovvot

from aiogram import Bot, Dispatcher, executor, types
from inline_keyboards import inline_markab_Fast_food, inline_markab_baliq, \
inline_markab_ichimliklar, inline_markab_steak,\
inline_markab_shashlik, inline_markab_salat,\
inline_markab_Milly, inline_markab_Shirinlik



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def echo(message: types.Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    try:
        add_user(tg_id=user_id, full_name=full_name, username=username)
        await message.answer(f"Assalomu aleykum {full_name} Hurmatli mijoz 😊",reply_markup=markup_tumanlar)
    except Exception as error:
        logging.error(error)
        
@dp.message_handler(text="Urganch")
async def get_Restoran_Urganch(message: types.Message):
    await message.answer(" Buyirtma berish uchun Royxatdagi Restoranlardan Birini tanlang 😊",reply_markup=markup_cafelar_Urganch)

# Restoranlar
# Urganch shaxar
@dp.message_handler(text="Gavhar milliy taomlari 🌮")
async def get_cafe_gavhar(message: types.Message):
    await message.answer("Assalomu aleykum  Gavhar milliy taomlar Restoraniga. Xush Kelibsiz 😊" , reply_markup=markup_taomlar_Urganch)

@dp.message_handler(text="Saltanat milliy taomlari 🥟")
async def get_cafe_saltanat(message: types.Message):
    await message.answer("Marhabo Saltanat milliy taomlar Restoraniga. Xush kelibsiz 🤩", reply_markup=markup_taomlar_Urganch)

@dp.message_handler(text="Alibobo baliq taomlari 🦈")
async def get_cafe_alibobo(message: types.Message):
    await message.answer("Assalomu aleykum ALibobo baliqlari Siz uchun 👨🏻‍🍳",reply_markup=markup_taomlar_Urganch)

@dp.message_handler(text="Baxrom Xod Dog 🌭")
async def get_cafe_baxrom(message: types.Message):
    await message.reply("Assalomu aleykum Baxrom Xod-Doglari 🧑🏼‍🍳",reply_markup=markup_taomlar_Urganch)
    
@dp.message_handler(text="Anaxon To'rt 🍰")
async def get_cafe_anaxon(message: types.Message):
    await message.reply("Assalomu aleykum Anaxon to'rtlari 🎂",reply_markup=markup_taomlar_Urganch)
    
@dp.message_handler(text="Gold Burger 🍔")
async def get_cafe_goldBurger(message: types.Message):
    await message.answer("Assalomu aleykum Gold Burgerga nima buyrtma qilasiz 🍔",reply_markup=markup_taomlar_Urganch)
# Urganch cafelar bolimi bitdi
# Xonqa Tuman 
    
    
    
@dp.message_handler(text="Xonqa")
async def get_Restoran_Xonqa(message: types.Message):
    await message.answer(" Buyirtma berish uchun Royxatdagi Restoranlardan Birini tanlang 😊",reply_markup=markup_cafelar_Xonqa)
    
@dp.message_handler(text="Yulduz Cafe 🌮")
async def get_cafe_Yulduz(message: types.Message):
    await message.answer("Assalomu aleykum Varohmatulloh Yulduz cafedan nima buyurtma cilasiz 🍽",reply_markup=markup_taomlar_Xonqa)


@dp.message_handler(text="Asl Milliy taomlar 🥟")
async def get_cafe_ASL(message: types.Message):
    await message.answer("Assalom Asl Milliy taomlar 🥟 nima buyurtma cilasiz 🍽",reply_markup=markup_taomlar_Xonqa)


@dp.message_handler(text="Dilshod Cafe 🫔")
async def get_cafe_Dilshod(message: types.Message):
    await message.answer("Assalomu aleykum Dilshod Cafe 🫔 nima buyurtma qilmoqchisiz 🍽",reply_markup=markup_taomlar_Xonqa)


@dp.message_handler(text="Lasvegas 🌭")
async def get_cafe_Lasvegas(message: types.Message):
    await message.answer("Xush kelibsiz Lasvegas 🌭 Siz uchun ",reply_markup=markup_taomlar_Xonqa)


@dp.message_handler(text="Sazanchik 🦈")
async def get_cafe_Sazanchik(message: types.Message):
    await message.answer("<i>Assalomu aleykum Xush kelibsiz Sazanchik 🦈 Siz uchun </i>", parse_mode="html",reply_markup=markup_taomlar_Xonqa )

@dp.message_handler(text="Burger Center 🍔")
async def get_cafe_Burger_Center(message: types.Message):
    await message.answer("<i>Assalomu aleykum Burger Center 🍔 Siz uchun maxsus burgerlar </i>", parse_mode="html",reply_markup=markup_taomlar_Xonqa )

# Xonqa tumani Cafelari bolimi bitti 
#Xiva tuma 




@dp.message_handler(text="Xiva")
async def get_Restoran_Xiva(message: types.Message):
    await message.answer(" Buyirtma berish uchun Royxatdagi Restoranlardan Birini tanlang 😊",reply_markup=markup_cafelar_Xiva)

@dp.message_handler(text="Dilmurad kafe 🍽")
async def get_cafe_Dilmurod(message: types.Message):
    await message.answer("<i>Assalomu aleykum Dilmurad kafe 🍽 Siz uchun maxsus taomlar </i>", parse_mode="html",reply_markup=markup_taomlar_Xiva )


@dp.message_handler(text="Sharof Baliqxona 🐟")
async def get_cafe_Sharof_Baliq(message: types.Message):
    await message.answer("<i>Assalomu aleykum Sharof Baliqxona 🍽 Siz uchun maxsus taomlar </i>", parse_mode="html",reply_markup=markup_taomlar_Xiva )


@dp.message_handler(text="Khiva 🍲")
async def get_cafe_Khiva(message: types.Message):
    await message.answer("Assalomu aleykum Khiva 🍲 Siz uchun maxsus taomlar ", parse_mode="html",reply_markup=markup_taomlar_Xiva )


@dp.message_handler(text="Sofra Restorani 🍴")
async def get_cafe_Sofra(message: types.Message):
    await message.answer("Assalomu aleykum Sofra Restorani 🍴 Siz uchun maxsus taomlar", parse_mode="html",reply_markup=markup_taomlar_Xiva )


@dp.message_handler(text="KHIVA TORT LAKOMOTIV 🎂")
async def get_cafe_Tort_LAKOMATIV(message: types.Message):
    await message.answer("Assalomu aleykum KHIVA TORT LAKOMOTIV 🎂 Siz uchun maxsus taomlar", parse_mode="html",reply_markup=markup_taomlar_Xiva )
    
    
@dp.message_handler(text="Xiva Kafe Milliy taomlar 🥘")
async def get_cafe_Milliy_taom(message: types.Message):
    await message.answer("Assalomu aleykum Xiva Kafe Milliy taomlar 🍽 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Xiva )

# Xiva cafelar Ro'yxati tamomlandi 
# Xazorasp




@dp.message_handler(text="Xazorasp")
async def get_Restoran_Xazorasp(message: types.Message):
    await message.answer(" Buyirtma berish uchun Royxatdagi Restoranlardan Birini tanlang 😊",reply_markup=markup_cafelar_Xazorasp)
    
    
@dp.message_handler(text="Varq Cafe 🍿")
async def get_cafe_Varq_Cafe(message: types.Message):
    await message.answer("Assalomu aleykum Varq Cafe 🍿 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Xazorasp)


@dp.message_handler(text="Center ☕️")
async def get_cafe_Center(message: types.Message):
    await message.answer("Assalomu aleykum Center ☕️ nima buyirtma qilasiz ",reply_markup=markup_taomlar_Xazorasp)


@dp.message_handler(text="Somsahona 🥟")
async def get_cafe_Somsahona(message: types.Message):
    await message.answer("Assalomu aleykum Somsahona 🥟 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Xazorasp)


@dp.message_handler(text="Dunyo Restorani 🍴")
async def get_cafe_Dunyo(message: types.Message):
    await message.answer("Assalomu aleykum Dunyo Restorani 🍴 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Xazorasp)


@dp.message_handler(text="Humo 🍜")
async def get_cafe_Humo(message: types.Message):
    await message.answer("Assalomu aleykum Humo 🍜 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Xazorasp)


@dp.message_handler(text="Globus Kafe 🦪")
async def get_cafe_Globus(message: types.Message):
    await message.answer("Assalomu aleykum Globus Kafe 🦪 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Xazorasp)
    
    
# Xazorasp Cafelar Royxati bitti 
# Shovvot tumani


    
@dp.message_handler(text="Shovvot")
async def get_Restoran_Shovvot(message: types.Message):
    await message.answer(" Buyirtma berish uchun Royxatdagi Restoranlardan Birini tanlang 😊",reply_markup=markup_cafelar_Shovvot)


@dp.message_handler(text="Choyxona 🫖")
async def get_cafe_Choyxona(message: types.Message):
    await message.answer("Assalomu aleykum Choyxona 🫖 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Shovvot)

    
@dp.message_handler(text="Kafe Oqshom ☕️")
async def get_cafe_Kafe_Oqshom(message: types.Message):
    await message.answer("Assalomu aleykum Kafe Oqshom ☕️ nima buyirtma qilasiz ",reply_markup=markup_taomlar_Shovvot)


@dp.message_handler(text="Orom Cafe 🏚")
async def get_cafe_Orom(message: types.Message):
    await message.answer("Assalomu aleykum Orom Cafe 🏚 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Shovvot)


@dp.message_handler(text="Sofra Restorani 🏢")
async def get_cafe_Sofra(message: types.Message):
    await message.answer("Assalomu aleykum Sofra Restorani 🏢 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Shovvot)


@dp.message_handler(text="Lazzat Kafe 🍲")
async def get_cafe_Lazzat(message: types.Message):
    await message.answer("Assalomu aleykum Lazzat Kafe 🍲 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Shovvot)
    
    
@dp.message_handler(text="Qumrixon Milliy taomlar 🍱")
async def get_cafe_Qumrixon(message: types.Message):
    await message.answer("Assalomu aleykum Qumrixon Milliy taomlar 🍱 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Shovvot)
# Shovvot Bitti Cafelar
# Gurlan tumani





@dp.message_handler(text="Gurlan")
async def get_Restaran_Gurlan(message: types.Message):
    await message.answer("Assalomu aleykum Gurlan tumani Cafelar Royxati", reply_markup=markup_cafelar_Gurlan)
    

@dp.message_handler(text="Baliqxona 🍽")
async def get_cafe_Baliqxona(message: types.Message):
    await message.answer("Assalomu aleykum Baliqxona 🍽 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Gurlan)
 
@dp.message_handler(text="To'ksonboy baliqxonasi 🦈")
async def get_cafe_Toksonboy(message: types.Message):
    await message.answer("Assalomu aleykum To'ksonboy baliqxonasi 🦈 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Gurlan)


@dp.message_handler(text="Versal 🍴")
async def get_cafe_Versal(message: types.Message):
    await message.answer("Assalomu aleykum Versal 🍴 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Gurlan)
    

@dp.message_handler(text="Olmos Kafesi 🥘")
async def get_cafe_Olmos(message: types.Message):
    await message.answer("Assalomu aleykum Olmos Kafesi 🥘 nima buyirtma qilasiz ",reply_markup=markup_taomlar_Gurlan)
    



# inline_Buttonlar bolimi

# nline_markab_Fast_food, inline_markab_baliq, \
# inline_markab_ichimliklar, inline_markab_steak,\
# inline_markab_shashlik, inline_markab_salat,\
# # inline_markab_Milly, inline_markab_Shirinlik
# ["fastfood","Shashlik 🥓","Steak 🥩"],
#  ["ichmlik 🍹", "Baliq 🦈", "Milliy taomlar 🥘"],
#  ["Salat 🥗", "", "Shirinlik 🧁"]
@dp.message_handler(text="")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
     