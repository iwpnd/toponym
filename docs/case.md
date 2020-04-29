# toponym.case

## DeclineConfig
```python
DeclineConfig(__pydantic_self__, **data: Any) -> None
```
A configuration to handle declinsion

Attributes:
    input_word: Input word
    recipe: topodictionary recipe by grammatical_case

## CaseConfig
```python
CaseConfig(__pydantic_self__, **data: Any) -> None
```
A configuration for a case

Attributes:
    input_word: Input word/words
    new_word_ending: word ending or multiple
    cut_ending_by: amount of characters cut from input_word before new_word_ending is added

## Case
```python
Case(self, decline_config: toponym.case.DeclineConfig)
```
grammatical case up for declinsion

Attributes:
    decline_config: DeclineConfig object
    name: name of grammatical case

### decline
```python
Case.decline(self) -> list
```
Declines a word based on configuration in decline_config

Returns:
    output_words: list of words after declinsion

## get_case_config
```python
get_case_config(decline_config: toponym.case.DeclineConfig) -> toponym.case.CaseConfig
```
Get a CaseConfig object from a DeclineConfig object

Attributes:
    decline_config: DeclineConfig object

Returns:
    case_config: CaseConfig

## decline_input_word
```python
decline_input_word(config: toponym.case.CaseConfig) -> str
```
Use config to construct a word after declinsion

Attributes:
    config: CaseConfig

Returns:
    output_word (str): a new word after declinsion
