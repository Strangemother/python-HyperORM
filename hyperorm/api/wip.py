from hyperorm import spaces, Service
a = spaces.Accounts(Service())
am = a.load_model(1, name='eric', balance=2)
am.save(secret='apples')
p = spaces.Phonebook(Service())
pm = p.load_model('eric', first='Entrice', last='Foolsaf', phone=12345678)
