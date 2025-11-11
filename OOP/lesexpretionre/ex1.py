import re

##compile##
#1
mbre = '1234'
ex=re.compile(r'\d{1,3}')
ser = ex.search(mbre)
print(ser)

#############
# #2
# ch = 'OUAMNI'#'OUMNI'
# ex = re.compile(r'[a-z]+')
# res = ex.search(ch)
# print(res)
###############

# #3
# ch = 'developement'
# ex = re.compile(r'(?i)[a-z]+')
# res = ex.search(ch)
# print(res)
############
####findall######
#4
# nbrsh = "ayoub ouahidi 21ans loubna barouk 2002 code postal 42000"
# ex = re.findall(r'\d{1,3}',nbrsh)
# print(ex)
#5
# carshe = "Ayoub Ouahidi 21ans Loubna barouk 2002 code postal 42000"
# ex = re.findall(r'[A-Z]*',carshe)#[A-Z][a-z]
# print(ex)


#6
# carshe = "Ayoub Ouahidi 21ans Loubna barouk 2002 code postal 42000"
# ex = re.findall(r'[a-z]*',carshe)#[A-Z][a-z]
# print(ex)

# #7
# list = []
# for x in nbrsh:
#     if x!='':
#         list.append(x)
# print(list)
#8

# age = '34a'
# exp = re.findall(r'[0-9]+',age)
# # print(exp)

# exp = re.findall(r'[A-Za-z]+',age)
# # print(exp)

# age = '12 Rue 2 Quartier '
# exp = re.findall(r'\d*',age)
# print(exp)

#9
# ch = '12 Rue 2 Quartier'
# exp = re.split(r'[0-9]*',ch)
# print(exp)

# exp = re.split('\s',ch)
# print(exp)


# #10
# ch = '12 Rue 2 Quartier'
# exp = re.sub('\s',";",ch)
# print(exp)  
# ###ectration des sous-groupes####
# motif = re.compile(r"(\d\d ?)(\w+) (\d{4})")
# crps = motif.search("bastill le 14 juillet 1989")
# print("crps.group() :", crps.group())
# print("crps.group() :", crps.group(1))
# print("crps.group() :", crps.group(2))
# print("crps.group() :", crps.group(3))
# print("crps.group() :", crps.group(1,3))
# print("crps.group() :", crps.group())
###################autre##3
# import re
# motif_date = re.compile(r"(?P<jour>\d\d ?) (?P<mois>\w+) (?P<anne>\d{4})")
# corresp = motif_date.search("Bastille le 14 juillet 1789")
# print(corresp.groupdict()) #{'jour': '14', 'mois': 'juillet'}
# print(corresp.group('jour')) #14
# print(corresp.group('mois')) #juille
# print(corresp.group('anne')) 
 



 #ghaalaaat 
# import re
# s = "Bastille le 14 juillet 1789"
# # motif_date = re.search(r"(?P<jour>\d\d ?) (?P<mois>\w+) (?P<anne>\d{4})")
# corresp = re.match(r"(?P<jour>\d\d ?) (?P<mois>\w+) (?P<anne>\d{4})",s)
# print(corresp.group()) #{'jour': '14', 'mois': 'juillet'}
# print(corresp.group('jour')) #14
# print(corresp.group('mois')) #juille
# print(corresp.group('anne')) 






