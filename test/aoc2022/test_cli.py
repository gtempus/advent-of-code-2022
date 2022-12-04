from typer.testing import CliRunner
from src.aoc2022.cli import app


def test_day_command_runs_without_error():
    runner = CliRunner()
    result = runner.invoke(app, ["day", "1", "--part", "1", "--input-file", "/some/test/input.txt"])
    assert result.exit_code == 0


def test_day_command_runs_with_default_for_part():
    runner = CliRunner()
    result = runner.invoke(app, ["day", "1"])
    output = result.stdout.rstrip()
    assert 'part 1' in output


def test_day_command_runs_with_default_for_test_input():
    runner = CliRunner()
    result = runner.invoke(app, ["day", "1"])
    output = result.stdout.rstrip()
    assert 'with input from None' in output


def test_specific_day_shows_answer():
    runner = CliRunner()
    result = runner.invoke(app, ["day", "1", "--part", "1", "--input-file", "/some/test/input.txt"])
    output = result.stdout.rstrip()
    assert 'Answer (day 1 [part 1] - with input from /some/test/input.txt):' in output
