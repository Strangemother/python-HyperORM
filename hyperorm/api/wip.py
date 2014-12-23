from examples.phonebook import phonebook
from examples.phonebook import phonebook_put_many
space = phonebook()
M = space.get_model()
m = M('tom', first='Tomas', last='Thumb', phone=440743566523)

m = space.get('bob')
m.get_attrs()
m.last
m.last = 'foo'
m.save()
m.get()
phonebook_put_many()

m = pb.get_model()()
m.get_def()
