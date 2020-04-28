# Usage

## Load Recipes

At first, you instantiate the Recipes. You can either use one of our pre-built ones or use your own.

### Pre-built Recipes
```python
from toponym.recipes import Recipes
from toponym.toponym import Toponym

recipes_russian = Recipes()
recipes.load_from_language(language='russian')

### Load your custom Recipes

Your Recipes must at least contain _default for Toponym to work.

```python
from toponym.recipes import Recipes

custom_recipes = {
     "_default": {
        "nominative": [[""], 0],
        "genitive": [[""], 0],
        "your_case": [[""], 0]
        }
    }

recipes = Recipes(language='your_language', file=custom_recipes)
print(recipes)

>> Recipes(
    language='your_language',
    loaded=True,
    word_endings=['_default',]
    )
```

### Custom Recipes from .json file

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
from toponym.recipes import Recipes

recipes = Recipes()
recipes.load_from_file(language='your_language', filepath="path/to/your_file.json")

print(recipes)

>> Recipes(
    language='your_language',
    loaded=True,
    word_endings=['_default']
    )
```

### Custom Recipes from dictionary

```
your_dictionary = {
    "_default": {
        "nominative": [[""], 0],
        "genitive": [[""], 0],
        "your_case": [[""], 0]
        }
    }
```

```python
from toponym.recipes import Recipes

recipes = Recipes()
recipes.load_from_dict(language='your_language', input_dict=your_dictionary)

print(recipes)

>> Recipes(
    language='your_language',
    loaded=True,
    word_endings=['_default']
    )
```

## Create toponyms

### Input string with a single word

```python
from toponym.recipes import Recipes
from toponym.toponym import Toponym

recipes_russian = Recipes()
recipes_russian.load_from_language(language='russian')

city = "Москва"

t = Toponym(city, recipes_russian)
t.build()

print(t.toponyms)

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
from toponym.recipes import Recipes
from toponym.toponym import Toponym

recipes_russian = Recipes()
recipes_russian.load_from_language(language='russian')

city = "Москва Ломоносовский"

t = Toponym(city, recipes_russian)
t.build()

print(t.toponyms)

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
