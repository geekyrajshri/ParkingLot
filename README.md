

>##### Dependencies:
- The application requires python version `3.7` and `pipenv`

- Install Pipenv `$ pip install pipenv`

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
