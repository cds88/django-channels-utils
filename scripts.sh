source ./.env/bin/activate
python setup.py sdist bdist_wheel
twine upload dist/* --verbose