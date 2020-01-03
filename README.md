# Toponym

Build grammatical cases for words in slavic languages from pre-defined recipes.

### supported languages:

```
full name		iso code
  croatian		hr
  russian		ru
  ukrainian		uk
  romanian		ro
  latvian		lv
  hungarian		hu
  greek		    el
  polish		pl
```

# Description

## Problem
In slavic languages a word can change, depending on how and where it is used within a sentence. The city Moscow (`Москва`) changes to `Москве` when used prepositional.
So when you want to eg. know if:

```python
"Москва" in "В Москве с начала года отремонтировали 3 тысячи подъездов"

>> False
```

## Solution
This is where Toponym comes in. Utilizing pre-defined recipes (topodictionaries) it naivly creates grammatical cases depending on the ending of the input word that the user wants to create Toponyms from. The recipe looks as follows:

### Recipe
```python
recipe = {
    "а": { # ending of the input-word
        "nominative": [
            [""], 0
            ],
        "genitive": [ # case that we need
            ["ы","и"], # ending of the output-word
            1 # chars to be deleted, before ending of output is added
            ],
        "dative": [
            ["е"], 1
            ],
        "accusative": [
            ["у"], 1
            ],
        "instrumental": [...]
}
```

If multiple endings are given, multiple toponyms with that ending will be created. Some of those created toponyms do not make sense, or are not used in the wild. If you have an idea on how to remove those that are unreal please contact me.

With the built toponyms for your can now check:

```python
td = topodict.Topodict(language='russian')
td.load()

city = "Москва"

tn = toponym.Toponym(city, td)
tn.build()

print(tn.list_toponyms())
>> ['Москвой', 'Москвы', 'Москви', 'Москве', 'Москву', 'Москва']

any([word in "В Москве с начала года отремонтировали 3 тысячи подъездов" for word in tn.list_toponyms()])
>> True
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

for usage:
```
pip install git+https://github.com/iwpnd/toponym.git
```

for development:
```
git clone https://github.com/iwpnd/toponym.git
pip install -e toponym/
```

## Running the tests

```
python -m pytest toponym/tests/unit
```

## Usage

### 1. Load Topodict

At first you instantiate the topodictionary. You can either use one of our pre-built ones, or use your own.

#### Load pre-built topodictionaries
```python
topodictionary = topodict.Topodict(language='russian')
print(topodictionary)
>> Topodict(
    language='russian',
    filepath='False',
    loaded=True,
    word_endings=['_default', 'й', 'б', 'в', 'г', 'д', ...]
    )
```

#### Load your (topo)dictionaries

Your (topo)dictionaries must atleast contain _default for Toponym to work.

```python
_dictionary = {
     "_default": {
        "nominative": [[""], 0],
        "genitive": [[""], 0],
        "your_case": [[""], 0]
        }
    }

topodictionary = topodict.Topodict(language='your_language', file=_dictionary)
print(topodictionary)

>> Topodict(
    language='your_language',
    filepath='True',
    loaded=True,
    word_endings=['_default']
    )
```

#### Load your (topo)dictionaries from .json file

```
# ././your_file.json
{
     "_default": {
        "nominative": [[""], 0],
        "genitive": [[""], 0],
        "your_case": [[""], 0]
        }
    }
```

```python
topodictionary = topodict.Topodict(language='your_language', file="path/to/your_file.json")
print(topodictionary)

>> Topodict(
    language='your_language',
    filepath='path/to/your_file.json',
    loaded=True,
    word_endings=['_default']
    )
```
### 2. Create toponyms

### Input string with a single word

```python

td = topodict.Topodict(language='russian')
td.load()

city = "Москва"

tn = toponym.Toponym(city, td)
tn.build()

print(tn.topo)

>> {
    'nominative': ['Москва'],
    'genitive': ['Москвы', 'Москви'],
    'dative': ['Москве'],
    'accusative': ['Москву'],
    'instrumental': ['Москвой'],
    'prepositional': ['Москве']
    }
```

### Input string with multiple words

```python
td = topodict.Topodict(language='russian')
td.load()

city = "Москва Ломоносовский"

tn = toponym.Toponym(city, td)
tn.build()

print(tn.topo)

{
    'nominative': [
        'Москва Ломоносовский'
        ],
    'genitive': [
        'Москвы Ломоносовского',
        'Москвы Ломоносовскего',
        'Москви Ломоносовского',
        'Москви Ломоносовскего'
        ],
    'dative': [
        'Москве Ломоносовскому',
        'Москве Ломоносовскему'
        ],
    'accusative': [
        'Москву Ломоносовского',
        'Москву Ломоносовскего',
        'Москву Ломоносовской',
        'Москву Ломоносовскый',
        'Москву Ломоносовский'
        ],
    'instrumental': [
        'Москвой Ломоносовскым',
        'Москвой Ломоносовским'
        ],
    'prepositional': [
        'Москве Ломоносовском',
        'Москве Ломоносовскем'
        ]
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
