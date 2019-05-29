
myCat={'size':'fat','color':'gray','disposition':'loud'}
print(myCat['size'])


#dictionary vs list
#[] is used for list while {} is used for dictionary
#in list order of items matter but it is not so in dictionary

spam=['cats','dogs','rats']
masp=['rats','dogs','cats']
print(spam==masp)           #not equal inspite of having same list items

name={'first':'abhay','middle':'shekhar','last':'yadav'}
eman={'last':'yadav','first':'abhay','middle':'shekhar'}
print(name==eman)           #equal ,order doesnot matter here
