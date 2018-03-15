# Two Way Sync Database

<p><b>Django Project for synchromizing two different poject that run in different environments.
 </b></p>
 
 ## How the project work?
do following steps in two different environment

<p><h3>#1</h3></p>

```commandline
git clone https://github.com/IsmoilovMuhriddin/TwoWaySync.git
cd TwoWaySync
```

<p><h3>#2</h3></p>

**create virtual environment and activate**

```commandline
virutalenv venv -p python3
source  venv/bin/activate
pip install -r requirements.txt
```
<p><h3>#3</h3></p>

**database** and **create superuser**
```commandline
python manage.py migrate
python manage.py createsuperuser
```

<p><h3>#4</h3></p>
change the PORT and OTHER_HOST  to second projects' configuration



```python
# Integration/sync.py
PORT = ':9000'          # this Should be Changed
OTHER_HOST = '127.0.0.1'    # this Should be changed
```


