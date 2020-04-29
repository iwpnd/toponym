# Usage as CLI

You can use `toponym` via CLI to generate toponyms from a `.csv` of words.

```bash
> toponym build --help

Usage: toponym build [OPTIONS]

Options:
  --language TEXT    language to build toponyms for  [required]
  --inputfile TEXT   input csv with list of words to create toponyms for
                     [required]

  --outputfile TEXT  output file to store resulting toponyms to [required]
  --help             Show this message and exit.
```

```python
# inputfile.csv
Москва
Москва Ломоносовский
```

```bash
> toponym build --language russian --inputfile inputfile.csv --outputfile output.json
```

```bash
# output.json
{
    'Москва': ['Москва', 'Москву', 'Москвой', 'Москвы', 'Москве', 'Москви'],
    'Москва Ломоносовский': [
        'Москва Ломоносовский',
        'Москвой Ломоносовским',
        'Москву Ломоносовского',
        'Москви Ломоносовского', [...]]
}
```
