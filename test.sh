  set -e
  set -x

  python -m vulture --min-confidence 80 --exclude=orangetool,build,.eggs --sort-by-size .
  python -m bandit -r orangetool -s B607,B603,B404,B311
  python -m pydocstyle --match-dir=orangetool