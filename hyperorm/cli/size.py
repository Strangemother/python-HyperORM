import os
from ..settings import *
from blessings import Terminal

t = Terminal()

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def directory_size(path):
    total_size = 0
    seen = set()

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)

            try:
                stat = os.stat(fp)
            except OSError:
                continue

            if stat.st_ino in seen:
                continue

            seen.add(stat.st_ino)

            total_size += stat.st_size

    return total_size  # size in bytes

def human(size):

    B = "B"
    KB = "KB"
    MB = "MB"
    GB = "GB"
    TB = "TB"
    UNITS = [B, KB, MB, GB, TB]
    HUMANFMT = "%f %s"
    HUMANRADIX = 1024.

    for u in UNITS[:-1]:
        if size < HUMANRADIX : return HUMANFMT % (size, u)
        size /= HUMANRADIX

    return HUMANFMT % (size,  UNITS[-1])

def main():
	total = 0
	paths = (
		('data', DATA_DIR),
		('coordinator', COORD_DATA_DIR),
		('daemon', DAEMON_DATA_DIR),
		('logs', LOG_DIR),
		)

	for n, _p in paths:
		p = os.path.abspath(_p)
		size = directory_size(p)
		total += size
		hs = human(size)

		print '{t.green}{hs}: {t.bold}{p}{t.normal}'.format(t=t, hs=hs, p=p)
	print '---'
	print '{t.green}{hs} {t.bold}Total{t.normal}'.format(t=t, hs=human(total))

if __name__ == '__main__':
	main()
