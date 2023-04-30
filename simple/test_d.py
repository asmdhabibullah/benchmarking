try:
    import django  # noqa

    django.setup()  # noqa
finally:
    pass

import time

from simple.models import Journal

LEVEL_CHOICE = [10, 20, 30, 40, 50]
start = time.time()


count = 0

for _ in range(10):
    for level in LEVEL_CHOICE:
        res = list(Journal.objects.filter(level=level).all())
        count += len(res)

now = time.time()

print(f"Django, D: Rows/sec: {count / (now - start): 10.2f}")
