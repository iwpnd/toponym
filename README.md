# Toponym

build grammatical cases for words in slavic languages from pre-defined recipes.

```python
recipe = {
    "а": {
        "nominative": ["", 0],
        "genitive": [["ы","и"], 1],
        "dative": [["е"], 1],
        "accusative": [["у"], 1],
        "instrumental": [["ой"], 1],
        "prepositional": [["е"], 1]
        }
}
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


### Installing


```
pip install git+https://github.com/iwpnd/toponym.git
```

or

```
git clone https://github.com/iwpnd/toponym.git
pip install -e ./toponym
```

## Running the tests

```
pytest toponym/test/unit
```

## Usage

```python
city = "Москва"

td = topodict.Topodict(language='russian')
td.load()

tn = toponym.Toponym(city, td)
tn.build()

print(tn.topo)

>> {
    'nominative': 'Москва',
    'genitive': ['Москвы', 'Москви'],
    'dative': ['Москве'],
    'accusative': ['Москву'],
    'instrumental': ['Москвой'],
    'prepositional': ['Москве']
    }
```

## Authors

* **Benjamin Ramser** - *Initial work* - [iwpnd](https://github.com/iwpnd)

See also the list of [contributors](https://github.com/iwpnd/toponym/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

