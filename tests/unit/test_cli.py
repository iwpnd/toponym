from os import path

from typer.testing import CliRunner

from toponym.main import app

runner = CliRunner()


def test_app():
    result = runner.invoke(app, ["build", "--help"])

    assert result.exit_code == 0


def test_app_integration(tmpdir):
    file = tmpdir.join("test.csv")

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


def test_app_integration_language_fails(tmpdir):
    file = tmpdir.join("test.csv")

    result = runner.invoke(
        app,
        [
            "build",
            "--language",
            "test",
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
