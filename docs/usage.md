# Usage

## 1. Load Topodict

At first, you instantiate the Recipes. You can either use one of our pre-built ones or use your own.

### Load pre-built Recipes
```python
from toponym.recipes import Recipes
from toponym.toponym import Toponym

recipes_russian = Recipes(language='russian')
print(recipes_russian)
>> Topodict(
    language='russian',
    filepath='False',
    loaded=True,
    word_endings=['_default', 'й', 'б', 'в', 'г', 'д', ...]
    )
```

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
    filepath='True',
    loaded=True,
    word_endings=['_default']
    )
```

### Load your custom Recipes from .json file

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

recipes = Recipes(language='your_language', file="path/to/your_file.json")
print(recipes)

>> Recipes(
    language='your_language',
    filepath='path/to/your_file.json',
    loaded=True,
    word_endings=['_default']
    )
```
## 2. Create toponyms

### Input string with a single word

```python
from toponym.recipes import Recipes
from toponym.toponym import Toponym

recipes_russian = Recipes(language='russian')
recipes_russian.load()

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

recipes_russian = Recipes(language='russian')
recipes_russian.load()

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
