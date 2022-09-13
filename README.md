# DOMAIN CHECK SCRIPT

Simple python script to get domain status and registrar information.

### Prerequisite

You should create a virtual environment to install the required modules and run the script in:
```
python3 -m venv .env
```

Then activate your virtual environment:
#### Windows
```
.env\Scripts\activate
```
#### Linux
```
. .env/bin/activate
```

And finally, install the modules in the `requirements` file:
```
pip install -r requirements
```

To use this script you must provide a CSV file with a single column of domain names.

Edit `line 6` to point to your CSV file:
```python
with open('myDomains.csv', 'r') as domains:
```

Then run:
```
python -m domaincheck.py
```

Output is sent to console, or can be redirected to a file:
```shell
python -m domaincheck.py > output_file.csv
```