# toponym.utils

## get_available_language_codes
```python
get_available_language_codes() -> list
```
Get available/supported language codes

Return
    ISO_639_1_codes (list): all available/supported languages

## get_language_code
```python
get_language_code(language:str) -> str
```
Get a single ISO_639_1 language code

Attributes:
    language (str): language to get a code for

Return
    ISO_639_1_codes (list): all available/supported languages

## print_available_languages
```python
print_available_languages() -> None
```
Prints available languages with their full names

## get_recipes
```python
get_recipes(language_code:str) -> dict
```
Get recipes for a specific ISO_639_1 language code

Attributes:
    language_code (str): ISO_639_1 language code

Returns:
    recipes (dict): collection of recipes for input language

## get_recipes_from_dict
```python
get_recipes_from_dict(input_dict:dict) -> dict
```
Get recipes from dict

Attributes:
    input_dict (dict): ISO_639_1 language code

Returns:
    recipes (dict): collection of recipes for input language

## get_recipes_from_file
```python
get_recipes_from_file(file_input:str) -> dict
```
Get recipes from file

Attributes:
    file_input (str): filepath

Returns:
    recipes (dict): collection of recipes for input language

## is_consistent_recipes
```python
is_consistent_recipes(filepath:str)
```
validate if recipes in /resources/*.json are valid

Attributes:
    filepath (str): filepath

Returns:
    bool

## is_json
```python
is_json(myjson:dict)
```
validate if input is json serializable

Attributes:
    myjson (dict): input to validate

Returns:
    bool
