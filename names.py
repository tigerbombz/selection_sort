users = {
 'Students': [
     {'id':1, 'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'id':2, 'first_name' : 'John', 'last_name' : 'Rosales'},
     {'id':3, 'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'id':4, 'first_name' : 'KB', 'last_name' : 'Tonel'}
  ]
}

users2 ={
  'Instructors': [
     {'id':1, 'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'id':2, 'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


print "Students"
for key, data in users.items():
  for value in data:
    print value["id"], "-", value["first_name"], value["last_name"], "-", str(len(value["first_name"]) + (len(value["last_name"])))


print "Instructors"
for key, data in users2.items():
  for value in data:
    print value["id"], "-", value["first_name"], value["last_name"], "-", str(len(value["first_name"]) + (len(value["last_name"])))
