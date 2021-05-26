

>##### Dependencies:
- The application requires python version `3.7` and `pipenv`

- Install python for ubuntu and mac
  1. https://phoenixnap.com/kb/how-to-install-python-3-ubuntu
  2. https://docs.python-guide.org/starting/install3/osx/

- Install pip
  1. https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/

- Install Pipenv `$ pip3 install pipenv`

- Or, if you’re using Ubuntu 17.10:
```
$ sudo apt install software-properties-common python-software-properties
$ sudo add-apt-repository ppa:pypa/ppa
$ sudo apt update
$ sudo apt install pipenv
```

- Otherwise, if you’re on MacOS, you can install Pipenv easily with Homebrew:

    `$ brew install pipenv`


>#####  Instructions:
- Clone the repository `ParkingLot`
- Change the directory to `ParkingLot`
- On the terminal run `pipenv install` and `pipenv install --dev`


>##### Unit test:
- `sh pipenv run unit-test `

>##### Run the application:
- `python main.py`
-  Application takes input from `parking_lot/data/input.txt` file
