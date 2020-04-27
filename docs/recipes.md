# toponym.recipes

## Recipes
```python
Recipes(self) -> None
```
Loads and provides access to recipes

Load Recipes from either file, dictionary or from stored
 default Recipes

Attributes:
    language (str): language the recipe is for
    file (Union[bool, str, dict]): if str load from
         file, if dict load from dict, defaults to bool
