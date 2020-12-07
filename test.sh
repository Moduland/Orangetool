  set -e
  set -x
  python version_check.py
  if [ "$TRAVIS_PYTHON_VERSION" = '3.6' ]
  then
	python -m vulture orangetool/ setup.py version_check.py --min-confidence 65 --sort-by-size 
	python -m bandit -r orangetool -s B607,B603,B404,B311
	python -m pydocstyle -v --match-dir=orangetool
  fi