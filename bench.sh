#!/bin/sh

cd $(dirname $0)

# setup DB
chmod u+x db.sh
./db.sh
export DJANGO_SETTINGS_MODULE="simple.settings"
./manage-simple.py migrate -v 0

# Test A → Insert
python -m simple.test_a

# Test B → Transactioned Intsert
python -m simple.test_b

# Test C → Bulk Insert
python -m simple.test_c

# Test D → Filter on level
python -m simple.test_d

# Test E → Filter limit 20
python -m simple.test_e

# Test F → Get
python -m simple.test_f

# Test G → dict
python -m simple.test_g

# Test H → tuple
python -m simple.test_h

# Test I → Update full
python -m simple.test_i

# Test J → Update partial
python -m simple.test_j

# Test K → Delete
python -m simple.test_k
