"""toolkit"""

import typer

app = typer.Typer()


@app.command()
def doctor(
        formal: bool = typer.Option(
            False,
            help="will check about only python.",
            rich_help_panel="Environment Configuration",
        )
):
    """Show information about the eccenca cmemc and python environment"""
    # TODO: cmemc-information
    if formal:
        print("will check about only python")
    else:
        print("will check about cmemc and python")


@app.command()
def datakit(
        formal: bool = typer.Option(
            False,
            help="will check about only python.",
            rich_help_panel="Environment Configuration",
        )
):
    """Serves fake data to CMEM on file size and type"""
    # TODO: fake-data-fetcher
    if formal:
        print("will check about only python")
    else:
        print("will check about cmemc and python")
