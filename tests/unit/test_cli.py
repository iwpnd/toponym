import csv
import json
from os import path

from typer.testing import CliRunner

from toponym.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["build", "--help"])

    assert result.exit_code == 0


def test_app_integration(tmpdir):

    with runner.isolated_filesystem():
        with open("test.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Москва"])
            writer.writerow(["Москва Ломоносовский"])

        result = runner.invoke(
            app,
            [
                "build",
                "--language",
                "russian",
                "--inputfile",
                "test.csv",
                "--outputfile",
                "test.json",
            ],
        )

        assert result.exit_code == 0
        assert path.exists("test.json")
        assert "Done" in result.stdout
        assert "Saved to" in result.stdout

        with open("test.json") as f:
            output = json.loads(f.read())

        assert "Москва" in output.keys()
        assert isinstance(output["Москва"], list)
        assert "Москве" in output["Москва"]


def test_app_integration_language_fails():
    with runner.isolated_filesystem():
        with open("test.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["Москва"])
            writer.writerow(["Москва Ломоносовский"])

        result = runner.invoke(
            app,
            [
                "build",
                "--language",
                "kaudawelsh",
                "--inputfile",
                "test.csv",
                "--outputfile",
                "test.json",
            ],
        )

        assert result.exit_code == 11
        assert "not supported" in result.stdout


def test_app_integration_input_fails(tmpdir):
    result = runner.invoke(
        app,
        [
            "build",
            "--language",
            "russian",
            "--inputfile",
            "test2.csv",
            "--outputfile",
            "test.json",
        ],
    )

    assert result.exit_code == 12
    assert "not in path" in result.stdout
