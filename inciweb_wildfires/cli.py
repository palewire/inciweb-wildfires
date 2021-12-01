import click
from inciweb_wildfires import get_fires


@click.group()
def cmd():
    """
    A command-line interface for downloading wildfire incidents data from InciWeb.

    Returns GeoJSON.
    """
    pass


@cmd.command(help="Download active fire incidents from InciWeb")
def fires():
    click.echo(get_fires())


if __name__ == '__main__':
    cmd()
