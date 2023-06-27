import sys


def dump():
    accepted = "0123456789ABCDEF"
    counter = 0
    chunk = ""
    with open(sys.argv[1], "a") as out:
        for character in sys.stdin.read():
            if character == " " or character == "=" or character == "\n":
                if any(c not in accepted for c in chunk):
                    pass
                else:
                    if counter == 0:
                        out.write('"')
                    out.write(chunk)
                    if counter > 6:
                        counter = 0
                        out.write(' "\n')
                    else:
                        out.write(" ")
                        counter = counter + 1
                chunk = ""
            else:
                chunk = chunk + character
        if counter != 0:
            out.write('"\n')


def calc(swing, mode):
    l01 = "0000 006D 0037 0000 "
    l02 = "0014 0088 0014 003A "
    l03 = "0014 0014 0015 0013 "
    l04 = "0014 0016 0014 0014 "
    l05 = "0014 0015 0013 003B "
    l06 = "0013 003E 0013 0015 "
    l07 = "0013 0015 0013 0015 "
    l08 = "0013 0018 0013 0015 "
    l09 = "0013 0015 0013 0015 "
    l10 = "0013 0018 0013 0015 "
    l11 = "0013 0015 0013 0015 "
    l12 = "0013 0013 0015 0013 "
    l13 = "0015 0013 0015 0013 "
    l14 = "0018 0013 0015 0013 "
    l15 = "0015 0013 0015 0013 "
    l16 = "0018 0013 0015 0013 "
    l17 = "0015 0013 0015 0013 "
    l18 = "0018 0013 0015 0013 "
    l19_swingoff = "003C 0013 003C 0013 "
    l19_swingon = "003C 0013 0015 0013 "
    l20 = "003E 0013 003C 0013 "
    l21_cool = "0015 0013 0015 0013 "
    l21_dry = "0015 0013 003C 0013 "
    l21_fan = "0015 0013 003C 0013 "
    l22 = "0018 0013 0015 0013 "
    l23_cool = "0015 0013 0015 0013 "
    l23_dry = "003C 0013 0015 0013 "
    l23_fan = "0015 0013 003C 0013 "
    l24_cool = "0018 0013 0015 0013 "
    l24_dry = "0018 0013 0015 0013 "
    l24_fan = "003E 0013 0015 0013 "
    l25 = "0015 0013 003C 0013 "
    # dubious
    l26 = "003E 0013 0015 0013 "
    l27 = "0015 0013 003C 0013 "
    l28 = "0015 0013 0085 0013 "
    # end dubious
    mode = (
        l01
        + l02
        + l03
        + l04
        + l05
        + l06
        + l07
        + l08
        + l09
        + l10
        + l11
        + l12
        + l13
        + l14
        + l15
        + l16
        + l17
        + l18
    )

    if swing == "true":
        mode += l19_swingon
    else:
        mode += l19_swingoff

    mode += l20

    if mode == "cool":
        mode += l21_cool
    elif mode == "dry":
        mode += l21_dry
    elif mode == "fan":
        mode += l21_fan

    mode += l22

    if mode == "cool":
        mode += l23_cool + l24_cool
    elif mode == "dry":
        mode += l23_dry + l24_dry
    elif mode == "fan":
        mode += l23_fan + l24_fan

    mode += l25

    mode += l26 + l27 + l28

    return mode


dump()
# print(calc(sys.argv[1], sys.argv[2]))
