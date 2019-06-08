import re
phoneNumberRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')          #regular expression compiles
mobject=phoneNumberRegex.search('My number is 415-654-9874')    #search() searches for the given re in the entire string
print('Phone number found: '+mobject.group())                   #group(0 gives the matched string


phnregex=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  #first parenthesis is for first group(1) and second parnhesis for second
mob=phnregex.search('My number is 415-654-9874')
print('Area :'+mob.group(1)+'\t Main Phone number :'+mob.group(2))

'''since mob.groups returns tuple we can use as'''
a,b=mob.groups()
print(a,b)

batregex=re.compile(r'Bat(man|mobile|copter)')               #re for batman,batmobile,batcopter(several alternative patterns)
mobj=batregex.search('Batmobile lost a wheel')
print(mobj.group())

print('--optional matching wit question mark--')
optional=re.compile(r'Bat(wo)?man')
vs=optional.search('The adventures of Batman')
print(vs.group())
vd=optional.search('The adventures of Batwoman')
print(vd.group())

print('--matching zero or more with the star--')
opt=re.compile(r'Bat(wo)*man')
vde=opt.search('The adventures of Batman')
print(vde.group())
vdw=opt.search('The adventures of Batwowowowoman')
print(vdw.group())

print('--matching 1 or more with the plus--')
plus=re.compile(r'Bat(wo)+man')
pl=plus.search('The adventures of Batwowoman')
print(pl.group())

print('--matching specific repetition with curly bracket--')
repet=re.compile(r'(Ha){3}')
robj=repet.search('HaHaHaHa')
print(robj.group())


print('--Greedy and Nongreedy matching--')
print('--Greedy--it matches the longest one')
greedy=re.compile(r'(Ha){3,4}')                              #it matches the longest one i.e. 4
grob=greedy.search('Dont do HaHaHaHaHa')
print(grob.group())

print('--NonGreedy--it matches the shortest one')
nongreedy=re.compile(r'(Ha){2,5}?')                          #it is followed by question mark
ngd=nongreedy.search('Dont do HaHaHaHaHa')
print(ngd.group())

print('---findall() method---') #it returns all the matched string while search() method returns only the first match in whole string
phn=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phn.findall('Cell: 415-541-4562 work: 789-954-6547'))  #it does not return object

