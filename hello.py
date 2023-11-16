#!/usr/bin/env python
import click
import glob


@click.command()
@click.option(
    "--path",
    prompt="Path to search CVS files",
    help="This is the path to search for files: /tmp",
)
@click.option(
    "--ftype", prompt="Pass in the type of file", help="Pass in the type file: i.e csv"
)
def search(path, ftype):
    """This is a tool that searches for patterns like *.csv"""
    results = glob.glob(f"{path}/*.{ftype}")
    click.echo(click.style("Found matches:", fg="red"))
    for result in results:
        click.echo(click.style(f"{result}", bg="blue", fg="white"))


if __name__ == "__main__":
    search()
