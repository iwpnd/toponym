<p align="center">
<a href="https://github.com/iwpnd/toponym/actions" target="_blank">
    <img src="https://github.com/iwpnd/toponym/workflows/build/badge.svg?branch=master" alt="Build Status">
</a>
<a href="https://codecov.io/gh/iwpnd/toponym" target="_blank">
    <img src="https://codecov.io/gh/iwpnd/toponym/branch/master/graph/badge.svg" alt="Coverage">
</a>
</p>


# Toponym

Build grammatical cases for words in Slavic languages from pre-defined recipes.

# Description

## Problem
In Slavic languages a word can change, depending on how and where it is used within a sentence. The city Moscow (`Москва`) changes to `Москве` when used prepositional.
So when you want to eg. know if:

```python
"Москва" in "В Москве с начала года отремонтировали 3 тысячи подъездов"

>> False
```

## Solution
This is where Toponym comes in. Utilizing pre-defined recipes it naively creates grammatical cases depending on the ending of the input word that the user wants to create Toponyms from. The recipe looks as follows:

### Recipe
```python
recipe = {
    "а": { # ending of the input-word
        "nominative": [[""], 0],
        "genitive": [ # case that we need
            ["ы","и"], # ending of the output-word
            1 # chars to be deleted, before ending of output is added
            ],
        "dative": [["е"], 1],
        "accusative": [["у"], 1],
        "instrumental": [...]
}
```

If multiple endings are given, multiple toponyms with that ending will be created. Some of those created toponyms do not make sense, or are not used in the wild. If you have an idea about how to remove those that are unreal please contact me.

With the built toponyms for you can now check:

```python
from toponym.recipes import Recipes
from toponym.toponym import Toponym

recipes_russian = Recipes()
recipes_russian.load_from_language(language='russian')

city = "Москва"

t = Toponym(input_word=city, recipes=recipes_russian)
t.build()

print(t.list_toponyms())
>> ['Москвой', 'Москвы', 'Москви', 'Москве', 'Москву', 'Москва']

any([word in "В Москве с начала года отремонтировали 3 тысячи подъездов" for word in tn.list_toponyms()])
>> True
```


### supported languages:

```
full name		iso code
croatian		hr
russian		    ru
ukrainian		uk
romanian		ro
latvian		    lv
hungarian		hu
greek		    el
polish		    pl
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

for usage:
```
pip install toponym
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
