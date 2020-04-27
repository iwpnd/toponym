# toponym.toponym

## Toponym
```python
Toponym(self, input_word:str, recipes:toponym.recipes.Recipes) -> None
```

### list_toponyms
```python
Toponym.list_toponyms(self) -> list
```
Put all created toponyms in a list

## merge_list_of_case_dictionaries
```python
merge_list_of_case_dictionaries(list_of_case_dictionaries:Generator) -> dict
```
Take a generator of case dictionaries and hash them into a
defaultdict.

If the input_word is a combination of two words, the input_word is split()
and _build_toponym_for_multiple_input_words() is used to build the toponym.
In the process it is possible that one of the input words has more than one
possible new_word_ending, so the possible toponyms are appended as list.

returns

Example:

{
    'nominative': [['Beograq'], ['Begraf']],
    'genitive': [['Beograq'], ['Begrafa']],
    'dative': [['Beograq'], ['Begrafu']],
    'accusative': [['Beograq'], ['Begrafa']],
    'locative': [['Beograq'], ['Begrafu']],
    'instrumental': [['Beograq'], ['Begrafem', 'Begrafom']]
    }

## concat_case_dictionaries
```python
concat_case_dictionaries(merged_toponym_dictionaries:collections.defaultdict) -> dict
```
Take a defaultdict and create products from the dicts values.

In case there are multiple input_words and one of them has multiple possible
new endings, we have to create products of those.

returns
Example:

{
    'nominative': ['Beograq Begraf'],
    'genitive': ['Beograq Begrafa'],
    'dative': ['Beograq Begrafu'],
    'accusative': ['Beograq Begrafa'],
    'locative': ['Beograq Begrafu'],
    'instrumental': ['Beograq Begrafem', 'Beograq Begrafom']
    }

## get_recipes_for_input_word
```python
get_recipes_for_input_word(input_word:str, recipes:toponym.recipes.Recipes) -> dict
```
Get a recipe from a list of recipes based on the longest matching
character sequence found in the input_word that is also in Recipes.keys()

returns recipe

{
    'nominative': [[''], 0],
    'genitive': [['e'], 1],
    'dative': [['i'], 1],
    'accusative': [['u'], 1],
    'locative': [['i'], 1],
    'instrumental': [['om'], 1]
    }

## get_longest_word_ending
```python
get_longest_word_ending(input_word:str, recipes:toponym.recipes.Recipes) -> str
```
Disect word into differnet size shifs and return the longest shif that
is also within recipes.keys()

returns str

Example:

recipes = {
    "_default": {"nominative": [[""], 0], "genitive": [[""], 0]},
    "i": {"nominative": [[""], 0], "genitive": [["o"], 1]},
    "o": {"nominative": [[""], 0], "genitive": [["a"], 1]},
    "ti": {"nominative": [[""], 0], "genitive": [["o"], 1]},
    "esti": {"nominative": [[""], 0], "genitive": [["o", "a"], 1]},
}

input_word = "Testi"
>> "esti"
