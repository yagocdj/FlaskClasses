# BASIC.PY
# CREATE ENTRIES INTO THE TABLES!
from models import db,Puppy, Owner, Toy

# CREATING 2 PUPPIES
rufus = Puppy('Rufus')
fido = Puppy('Fido')

# ADD PUPPIES TO DB
db.session.add_all([rufus, fido])
db.session.commit()

# Check!
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)
# rufus = Puppy.query.filter_by(name='Rufus').all() -> it returns a list of all the puppies whose name is equal to 'Rufus'
# rufus = Puppy.query.filter_by(name='Rufus').all()[0] -> first occurrence of 'Rufus'

# CREATE OWNER OBJECT
jose = Owner('Jose', rufus.id)

# Give Rufus some toys
toy1 = Toy('Chew Toy', rufus.id)
toy2 = Toy('Ball', rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

# GRAB RUFUS AFTER THOSE ADDITIONS!
rufus = Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rufus.report_toys()
