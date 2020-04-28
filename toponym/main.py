import json

import safer
import typer

from toponym.recipes import Recipes
from toponym.settings import LANGUAGE_DICT
from toponym.toponym import Toponym
from toponym.utils import file_exists
from toponym.utils import lazy_load_csv

app = typer.Typer()


@app.callback()
def callback():
    """
    Build toponyms via CLI

    Use it with build command.

    Create a toponym json file (--outputfile) from an input csv file (--inputfile).
    """
    pass


@app.command()
def build(
    language: str = typer.Option(...),
    inputfile: str = typer.Option(...),
    outputfile: str = typer.Option(...),
):

    if language not in LANGUAGE_DICT.keys():
        typer.echo(
            f"🔥 {language} not supported. Use one of these instead: {list(LANGUAGE_DICT.keys())}"
        )
        raise typer.Exit(code=11)

    if not file_exists(filename=inputfile):
        typer.echo(f"🔥 {inputfile} not in path")
        raise typer.Exit(code=12)

    output = dict()
    processed = 0
    recipes = Recipes()
    recipes.load_from_language(language=language)

    with safer.open(outputfile, "a", encoding="utf8") as fp:
        with typer.progressbar(
            lazy_load_csv(inputfile), label=f"🚀 Processing {inputfile}", length=100
        ) as progress:

            for word in progress:
                t = Toponym(input_word=word[0], recipes=recipes)
                t.build()
                output[word[0]] = t.list_toponyms()
                processed += 1

            json.dump(output, fp)

    typer.echo(f"🙀 Done! Processed: {processed} words")
    typer.echo(f"Saved to: {outputfile}")
