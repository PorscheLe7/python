province = input( "Please enter your city/province: ")
postalCode = input( "Please enter your postal code: ")



ontarioList = { "L", "K", "M", "N", "P"}
Alberta = "T"
BritishColumbia = "V"
Manitoba = "R"
NewBrunswick = "E"
Newfoundland = "A"
NWT = "X"
NovaScotia = "B"
Nunavut = "X"
PE = "C"
QuebecList = { "G","H","J" }
SK = "S"
YK = "Y"

provinceFlag = False
postalCodeFlag = False
consistentFlag = False
consistentFlag2 = False
province = province.upper()
postalCode = postalCode.upper()
result = False

#CHECK LAST 4 CHARACTERS OF STRING INPUT FOR A COMMA FOLLOWED BY A SPACE AND FOLLOWED BY 2 LETTERS AFTER#
if (province[-4 : -2] == ", "
and province[-2 : len(province)].isalpha()):
    provinceFlag = True
    #THIS IS TO CHECK IF THIS IF STATEMENT WORKS
    print(" It works!")

elif (province[-4 : -2] == ","
and province[ - 2 : len(province)].isalpha()):
    print( "I'm sorry your city and province is incorrectly formatted")

elif (province[-4 : -2] != ", "
and province[-2 : len(province)].isalpha()):
    print( "Sorry that is not a valid city/province" )

if len(postalCode) == 7:        
    if (postalCode[0].isalpha
    and postalCode[1].isdecimal
    and postalCode[2].isalpha
    and postalCode[3].isspace
    and postalCode[4].isalpha
    and postalCode[5].isdecimal
    and postalCode[6].isalpha):
        postalCodeFlag = True
        print( "It works 2!")
else:
    print( "I'm sorry, your postal code is not valid" )


#What I'm trying to accomplish here is to check the last 2 digits of province input ( which should always be 2 letters) and associate a value with that.
# I tried to use lists to accomplish this but it didn't work.
#EDIT: This statement seems to work but I have to edit the rest 
if province [-4 : -2 ] == "ON" and postalCode[0] == "L":
    consistentFlag2 = True
else:
    print( "I'm sorry, no postal codes in ON start with " + str(postalCode[0]))
if province [-4 : -2 ] == "AB" and postalCode[0] in Alberta :
    consistentFlag2 = True
else:
    print( "I'm sorry, no postal codes in AB start with " + str(province[-2 : len(province)]))
if province [-4 : -2 ] == "BC" and postalCode[0] in BritishColumbia:
    consistentFlag2 = True
if province [-4 : -2 ] == "MB" and postalCode[0] in Manitoba:
    consistentFlag2 = True
if province [-4: -2 ] == "NB" and postalCode[0] in NewBrunswick:
    consistentFlag2 = True
if province [-4: -2 ] == "NL" and postalCode[0] in Newfoundland:
    consistentFlag2 = True    
if province [-4: -2 ] == "NT" and postalCode[0] in NWT:
    consistentFlag2 = True
if province [-4: -2 ] == "NS" and postalCode[0] in NovaScotia:
    consistentFlag2 = True    
if province [-4: -2 ] == "NU" and postalCode[0] in Nunavut:
    consistentFlag2 = True    
if province [-4: -2 ] == "PE" and postalCode[0] in PE:
    consistentFlag2 = True
if province [-4: -2 ] == "QC" and postalCode[0] in Quebec:
    consistentFlag2 = True    
if province [-4: -2 ] == "SK" and postalCode[0] in SK:
    consistentFlag2 = True    
if province [-4: -2 ] == "YK" and postalCode[0] in YK:
    print( " It works 3!")
    consistentFlag2 = True    

#This is buggy when you run it I think
result = provinceFlag + consistentFlag2 + postalCodeFlag
if result == True:
    print( "Thank you! Your data is validated!")
elif provinceFlag == False:
    print( "I'm sorry, your city and province are incorrectly formatted" )
elif postalCodeFlag == False:
    print( "I'm sorry, your postal code is incorrectly formatted" )
