from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
"""Tugma qo'shish birinchi usul""" 
markup_tumanlar = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Urganch"), KeyboardButton("Xonqa"),KeyboardButton(text="Xiva")],
    [KeyboardButton("Xazorasp"),KeyboardButton(text="Shovvot"), KeyboardButton("Gurlan")],
],resize_keyboard=True)
"""Tugma qo'shish ikkinchi usul"""
"""Urganch uchun"""
markup_cafelar_Urganch = ReplyKeyboardMarkup(resize_keyboard=True)
markup_cafelar_Urganch.row("Gavhar milliy taomlari 🌮", "Saltanat milliy taomlari 🥟")
markup_cafelar_Urganch.row("Alibobo baliq taomlari 🦈", "Baxrom Xod Dog 🌭")
markup_cafelar_Urganch.row("Anaxon To'rt 🍰", "Gold Burger 🍔")
markup_cafelar_Urganch.row("Orqaga ↩️")

markup_taomlar_Urganch=ReplyKeyboardMarkup(resize_keyboard=True)
markup_taomlar_Urganch.row("Fast Food 🍔","Shashlik 🥓","Steak 🥩")
markup_taomlar_Urganch.row("ichmlik 🍹", "Baliq 🦈", "Milliy taomlar 🥘")
markup_taomlar_Urganch.row("Salat 🥗", "Mevalar 🍉", "Shirinlik 🧁")
markup_taomlar_Urganch.row("Orqaga ↩️")


"""Xonqa uchun"""
markup_cafelar_Xonqa = ReplyKeyboardMarkup(resize_keyboard=True)
markup_cafelar_Xonqa.row("Yulduz Cafe 🌮", "Asl Milliy taomlar 🥟")
markup_cafelar_Xonqa.row("Dilshod Cafe 🫔", "Lasvegas 🌭")
markup_cafelar_Xonqa.row("Sazanchik 🦈", "Burger Center 🍔")
markup_cafelar_Xonqa.row("Orqaga ↩️")

markup_taomlar_Xonqa = ReplyKeyboardMarkup([
 ["Fast Food 🍔","Shashlik 🥓","Steak 🥩"],
 ["ichmlik 🍹", "Baliq 🦈", "Milliy taomlar 🥘"],
 ["Salat 🥗", "", "Shirinlik 🧁"]
],resize_keyboard=True)

"""Xazorasp uchun"""
markup_cafelar_Xazorasp = ReplyKeyboardMarkup(resize_keyboard=True)
markup_cafelar_Xazorasp.row("Varq Cafe 🍿", "Center ☕️")
markup_cafelar_Xazorasp.row("Somsahona 🥟", "Dunyo Restorani 🍴")
markup_cafelar_Xazorasp.row("Humo 🍜", "Globus Kafe 🦪")
markup_cafelar_Xazorasp.row("Orqaga ↩️")

markup_taomlar_Xazorasp = ReplyKeyboardMarkup([
 ["Fast Food 🍔","Shashlik 🥓","Steak 🥩"],
 ["ichmlik 🍹", "Baliq 🦈", "Milliy taomlar 🥘"],
 ["Salat 🥗", "", "Shirinlik 🧁"]
],resize_keyboard=True)

"""Xiva uchun"""
markup_cafelar_Xiva = ReplyKeyboardMarkup(resize_keyboard=True)
markup_cafelar_Xiva.row("Dilmurad kafe 🍽", "Sharof Baliqxona 🐟")
markup_cafelar_Xiva.row("Khiva 🍲", "Sofra Restorani 🍴")
markup_cafelar_Xiva.row("KHIVA TORT LAKOMOTIV 🎂", "Xiva Kafe Milliy taomlar 🥘")
markup_cafelar_Xiva.row("Orqaga ↩️")

markup_taomlar_Xiva = ReplyKeyboardMarkup([
 ["Fast Food 🫔","Shashlik 🍤","Steak 🥩"],
 ["ichmlik 🥃", "Baliq 🦈", "Milliy taomlar 🌯"],
 ["Salat 🥗", "", "Shirinlik 🌰"]
],resize_keyboard=True)

"""Shovvot uchun"""
markup_cafelar_Shovvot = ReplyKeyboardMarkup(resize_keyboard=True)
markup_cafelar_Shovvot.row("Choyxona 🫖", "Kafe Oqshom ☕️")
markup_cafelar_Shovvot.row("Orom Cafe 🏚", "Sofra Restorani 🏢")
markup_cafelar_Shovvot.row("Lazzat Kafe 🍲", "Qumrixon Milliy taomlar 🍱")
markup_cafelar_Shovvot.row("Orqaga ↩️")

markup_taomlar_Shovvot = ReplyKeyboardMarkup([
 ["","Shashlik 🥓","Steak 🥩"],
 ["ichmlik 🍹", "Baliq 🦈", "Milliy taomlar 🥘"],
 ["Salat 🥗", "", "Shirinlik 🧁"]
],resize_keyboard=True)

"""Gurlan"""
markup_cafelar_Gurlan = ReplyKeyboardMarkup(resize_keyboard=True)
markup_cafelar_Gurlan.row("Baliqxona 🍽")
markup_cafelar_Gurlan.row("To'ksonboy baliqxonasi 🦈", "Versal 🍴")
markup_cafelar_Gurlan.row("Olmos Kafesi 🥘")
markup_cafelar_Gurlan.row("Orqaga ↩️")

markup_taomlar_Gurlan = ReplyKeyboardMarkup([
 ["Fast Food 🫔","Shashlik 🍤","Steak 🍗"],
 ["ichmlik 🥃", "Baliq 🦈", "Milliy taomlar 🌯"],
 ["Salat 🥗", "", "Shirinlik 🌰"]
],resize_keyboard=True)