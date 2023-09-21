from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Notown"]

col_array=['Musican','Instrument','Album','Song']

Musician=db['musician']
Instrument=db['instrument']
Album=db['album']
Song=db['song']

def insert(Collection,doc):
 Collection.insert_one(doc) 


def insertMusician():
 doc={}
 doc['ssn'] =input("Enter Ssn:")
 doc['name']=input("Enter Name:")
 doc['addr']=input("Enter Address:")
 doc['ph_no']=input("Enter Ph_No:")
 doc['instru']=list(input("Enter instru:").split(" "))
 doc['sid']=list(input("Enter sid:").split(" "))
 insert(Musician,doc)

def insertInstru():
 doc={}
 doc['iuin']=input("Enter Id:")
 doc['name']=input("Enter Name:")
 doc['key']=input("Enter key:")
 insert(Instrument,doc)
 

def insertAlbum():
 doc={}
 doc['auin']=input("Enter Id:")
 doc['title']=input("Enter Title:")
 doc['date']=input("Enter Date:")
 doc['format']=input("Enter Format:")
 doc['sid']=list(input("Enter sid:").split(" "))
 doc['producer']=input("Enter Producer:")
 insert(Album,doc)

def insertSong():
 doc={}
 doc['sid']=input("Enter sid:")
 doc['author']=input("Enter Author:")
 doc['stitle']=input("Enter Title:")
 insert(Song,doc)

def display(Collection):
 cursor = Collection.find()
 for document in cursor:
    print("-----"*20)
    print(document)
    print("-----"*20)

def update(Collection,filter,setField):
 Collection.update_one(filter,{'$set':setField})

def updateMusician():
 ssn=input("Enter ssn:")
 new_name=input("Enter new Name:")
 filter={'ssn':ssn}
 field ={'name':new_name}
 update(Musician,filter,field)
 
def updateInstru():
 iuin=int(input("Enter Id:"))
 new_name=input("Enter new Name:")
 filter={'iuin':iuin}
 field ={'name':new_name}
 update(Instrument,filter,field)

def updateAlbum():
 auin=input("Enter Id:")
 new_name=input("Enter title:")
 filter={'auin':auin}
 field ={'title':new_name}
 update(Album,filter,field)

def updateSong():
 sid=input("Enter Id:")
 new_name=input("Enter title:")
 filter={'sid':sid}
 field ={'stitle':new_name}
 update(Song,filter,field)

def delete(Collection,doc):
  Collection.delete_one(doc)

def deleteMusician():
 ssn=input("Enter ssn:")
 doc={'ssn':ssn}
 delete(Musician,doc)

def deleteInstru():
 iuin=int(input("Enter Id:"))
 doc={'iuin':iuin}
 delete(Instrument,doc)

def deleteAlbum():
 auin=input("Enter Id:")
 doc={'auin':auin}
 delete(Album,doc)

def deleteSong():
 sid=input("Enter Id:")
 doc={'sid':sid}
 delete(Song,doc)

try:
 while True:
  print("1.Musician\n2.Instrument\n3.Album\n4.Song\n5.Exit")
  ch=int(input("Enter your choice:"))
  if ch>=1 and ch<=4:
   while True:
    print("1.Insert",col_array[ch-1])
    print("2.Read",col_array[ch-1])
    print("3.Update",col_array[ch-1])
    print("4.Delete",col_array[ch-1])
    print("5.Exit")
    c=int(input("Enter Your Choice:"))
    if c==5:
     break
    if c>=1 and c<=4:
     if ch==1:
      if c==1:
       insertMusician()
      elif c==2:
       display(Musician)
      elif c==3:
       updateMusician()
      elif c==4:
       deleteMusician()

     elif ch==2:
      if c==1:
       insertInstru()
      elif c==2:
       display(Instrument)
      elif c==3:
       updateInstru()
      elif c==4:
       deleteInstru()

     elif ch==3:
      if c==1:
       insertAlbum()
      elif c==2:
       display(Album)
      elif c==3:
       updateAlbum()
      elif c==4:
       deleteAlbum()

     elif ch==4:
      if c==1:
       insertSong()
      elif c==2:
       display(Song)
      elif c==3:
       updateSong()
      elif c==4:
       deleteSong()
    else:
      print("Invalid Input...")
  elif ch==5:
    break
  else:
    print("Invalid Input:")
except:
 print("Something went Wrong...")
  
