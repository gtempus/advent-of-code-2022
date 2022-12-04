import typer

app = typer.Typer(add_completion=False)


@app.command()
def day(
    num: int,
    part: int = typer.Option(1, "-p", "--part"),
    test_input: str = typer.Option(None, "-i", "--input-file")
):
    print(f"Answer (day {num} [part {part}] - with input from {test_input}):")


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    aoc2022 is a small command line tool for running the puzzles
    """
    if ctx.invoked_subcommand is None:
        print("Hi!")

if __name__ == "__main__":
    app()