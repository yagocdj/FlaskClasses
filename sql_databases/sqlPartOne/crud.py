from basic import db, Puppy

###### IMPORTANT - I can run this script only once ######
###### If I want to run it again, then I should delete the data.sqlite and recreate the db running setupdatabase.py ######

## CREATE ##
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

## READ ##
# ORM -> Object Relational Mapper
all_puppies = Puppy.query.all()  # list of puppies objects in the table!
print(all_puppies)

# SELECT BY ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

# FILTERS
# PRODUCE SOME SQL CODE FOR US!
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())  # print a list of all the puppies that have the name == 'Frankie'
# ["Frankie is 3 year/s old"]

## UPDATE ##
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()

## DELETE ## 
second_pup = Puppy.query.get(2)
db.session.delete(second_pup)
db.session.commit()

#
all_puppies = Puppy.query.all()
print(all_puppies)
