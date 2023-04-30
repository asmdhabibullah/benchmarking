try:
    import django  # noqa

    django.setup()  # noqa
finally:
    pass

import os
import time
from random import randrange

from simple.models import Journal

LEVEL_CHOICE = [10, 20, 30, 40, 50]
iters = int(os.environ.get("ITERATIONS", "1000"))
start = time.time()


count = 0

for _ in range(iters // 10):
    for level in LEVEL_CHOICE:
        offset = randrange(iters - 20)
        res = list(Journal.objects.filter(level=level).all()[offset : 20 + offset])
        count += len(res)

now = time.time()

print(f"Django, E: Rows/sec: {count / (now - start): 10.2f}")
