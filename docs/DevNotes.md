# Notes for developing, building and testing

## Building/Staging

Super useful instructons:
http://peterdowns.com/posts/first-time-with-pypi.html

Test package construction:
`python setup.py test`

Upload to PyPi Test:
`python setup.py register -r pypitest`
`python setup.py sdist upload -r pypitest`

Installing from Pypi Test:
`pip install -i https://testpypi.python.org/pypi pyhoofinance`

Upload to PyPi live:
`python setup.py register`
`python setup.py sdist upload -r pypi`