if birth_year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    zodiac_number = (birth_year - 1900) % 12

    if zodiac_number == 0:
        zodiac = "Rat (鼠 / Shǔ)"
    elif zodiac_number == 1:
        zodiac = "Ox (牛 / Nǐu)"
    elif zodiac_number == 2:
        zodiac = "Tiger (虎 / Hǔ)"
    elif zodiac_number == 3:
        zodiac = "Rabbit (兔 / Tù)"
    elif zodiac_number == 4:
        zodiac = "Dragon (龍 / Lóng)"
    elif zodiac_number == 5:
        zodiac = "Snake (蛇 / Shé)"
    elif zodiac_number == 6:
        zodiac = "Horse (马 / Mǎ)"
    elif zodiac_number == 7:
        zodiac = "Goat (羊 / Yáng)"
    elif zodiac_number == 8:
        zodiac = "Monkey (猴 / Hóu)"
    elif zodiac_number == 9:
        zodiac = "Rooster (鸡 / Jī)"
    elif zodiac_number == 10:
        zodiac = "Dog (狗 / Gǒu)"
    else:
        zodiac = "Pig (猪 / Zhū)"
