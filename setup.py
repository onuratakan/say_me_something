from setuptools import setup

from setuptools import setup



setup(name='say_something',
version='0.1.0',
description="""Lots of cyber security tool""",
long_description="""
# HACON
Lots of cyber security tool
# Install
```
pip3 install HACON
```
# Using
## In another script
```python
from hacon import HACON

HACON.arguments("-h")
```
## In command line
```python
HACON -h
```

# With docker
## Install 
```
docker pull ghcr.io/onuratakan/hacon:latest
```
## Using
```
docker run -t -i  --network=host ghcr.io/onuratakan/hacon /bin/sh
```
and type
```python
HACON -h
```

# Reminder
Important Information and Reminder Information and programs in all repositories are created for testing purposes. Any legal responsibility belongs to the person or organization that uses it.

""",
long_description_content_type='text/markdown',
url='https://github.com/onuratakan/say_something',
author='Onur Atakan ULUSOY',
author_email='atadogan06@gmail.com',
license='MIT',
packages=["say_something"],
package_dir={'':'src'},
package_data={
    "say_something" : ["cache/*.mp3"],
},
install_requires=[
    "click==8.0.1",
    "gTTS==2.2.3",
    "playsound==1.3.0",
    "pyttsx3==2.90",
],
entry_points = {
    'console_scripts': ['say=say_something.say_something:say'],
},
python_requires='>=3',
zip_safe=False)
