import pytest
from unittest import mock
from unittest.mock import MagicMock
from typer.testing import CliRunner

from src.aoc2022.cli import app
from src.aoc2022 import cli
from src.aoc2022.puzzle_factory import Solver


@pytest.fixture()
def mock_puzzle_factory():
    with mock.patch.object(cli, "PuzzleFactory", autospec=True) as Factory:
        Factory.return_value.create.return_value = MagicMock(spet_set=Solver(), answer=5)
        yield Factory.return_value

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


def test_specific_day_shows_answer_context():
    runner = CliRunner()
    result = runner.invoke(app, ["day", "1", "--part", "1", "--input-file", "/some/test/input.txt"])
    output = result.stdout.rstrip()
    assert 'Answer (day 1 [part 1] - with input from /some/test/input.txt):' in output


# @pytest.mark.xfail
def test_specific_day_shows_answer(mock_puzzle_factory):
    runner = CliRunner()
    result = runner.invoke(app, ["day", "1", "--part", "1", "--input-file", "/some/test/input.txt"])
    output = result.stdout.rstrip()
    assert output.endswith(': 5')


def test_puzzle_factory_called_with_info(mock_puzzle_factory):
    runner = CliRunner()
    runner.invoke(app, ["day", "1", "--part", "2", "--input-file", "/some/test/input.txt"])
    mock_puzzle_factory.create.assert_called_with(day_num=1, part=2, test_input="/some/test/input.txt")


def test_solver_commanded_to_solve(mock_puzzle_factory):
    runner = CliRunner()
    runner.invoke(app, ["day", "1", "--part", "2", "--input-file", "/some/test/input.txt"])
    mock_solver = mock_puzzle_factory.create(day_num=1, part=2, test_input="/some/test/input.txt")
    mock_solver.solve.assert_called()
