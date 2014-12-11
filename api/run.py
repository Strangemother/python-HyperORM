from service import HypreAPI
s = HypreAPI()
is_installed = s.installed()
print 'installed', is_installed

if is_installed is not True:
	installed = s.install()
	print 'installed', installed
