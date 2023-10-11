dct = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

stg = input(">>> ")
stg = stg.split()
ls = stg[0].split(".")
text = str()
text += f"{int(ls[0])} {dct[int(ls[1])]} {ls[-1]} year "
text += f"{stg[1].split(':')[0]} hours {stg[1].split(':')[1]} minutes"
print(text)