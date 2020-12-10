#!/usr/bin/python

#import pyWars
import local_pyWars as pyWars
import codecs

def answer0(datasample):
    return datasample

def answer1(datasample):
    return datasample+5

def answer2(datasample):
    return 16 ** datasample

def answer3(datasample):
    return float(datasample)

def answer4(datasample):
    return datasample >> 4

def answer5(datasample):
    return datasample.decode()

def answer6(datasample):
    return bytes(datasample, 'utf-8')

def answer7(datasample):
    return ord(datasample[4])

def answer8(datasample):
    return len(datasample.encode('utf-8'))

def answer9(datasample):
    return codecs.encode(datasample, 'rot-13')

def answer10(datasample):
    return codecs.decode(datasample, 'base-64')

def answer11(datasample):
    return datasample.upper()

def answer12(datasample):
    return datasample.find('SANS')

def answer13(datasample):
    return datasample[::-1]

def answer14(datasample):
    return datasample + datasample[::-1] + datasample

def answer15(datasample):
    return datasample[1] + datasample[4] + datasample[8]

def answer16(datasample):
    return datasample[-1] + datasample[1:-1] + datasample[0]

def answer17(datasample):
    return (datasample[0:len(datasample)//2])[::-1] + datasample[len(datasample)//2:]

def answer18(datasample):
    #E->3,A->4,T->7,S->5,G->6
    finaldata = ""
    for i in datasample:
        if i.isupper():
            if i == "E":
                finaldata += "3"
            elif i == "A":
                finaldata += "4"
            elif i == "T":
                finaldata += "7"
            elif i == "S":
                finaldata += "5"
            elif i == "G":
                finaldata += "6"
            else:
                finaldata += i
        else:
            finaldata += i
    
    return finaldata

def answer19(datasample):
    return datasample[2]


def main():
    print("#0", d.answer( 0, answer0(d.data(0))))
    print("#1", d.answer( 1, answer1(d.data(1))))
    print("#2", d.answer( 2, answer2(d.data(2))))
    print("#3", d.answer( 3, answer3(d.data(3))))
    print("#4", d.answer( 4, answer4(d.data(4))))
    print("#5", d.answer( 5, answer5(d.data(5))))
    print("#6", d.answer( 6, answer6(d.data(6))))
    print("#7", d.answer( 7, answer7(d.data(7))))
    print("#8", d.answer( 8, answer8(d.data(8))))
    print("#9", d.answer( 9, answer9(d.data(9))))
    print("#10", d.answer( 10, answer10(d.data(10))))
    print("#11", d.answer( 11, answer11(d.data(11))))
    print("#12", d.answer( 12, answer12(d.data(12))))
    print("#13", d.answer( 13, answer13(d.data(13))))
    print("#14", d.answer( 14, answer14(d.data(14))))
    print("#15", d.answer( 15, answer15(d.data(15))))
    print("#16", d.answer( 16, answer16(d.data(16))))
    print("#17", d.answer( 17, answer17(d.data(17))))
    print("#18", d.answer( 18, answer18(d.data(18))))
    print("#19", d.answer( 19, answer19(d.data(19))))

if __name__ == "__main__":
    d = pyWars.exercise()
    d.login("ninja","ninja")
    main()
    d.logout()