import click

from CS_test.config import Config


@click.command()
def cs_test() -> None:
    """Entry point to CS test tool."""
    config = Config()
    config.config_test()


if __name__ == "__main__":
    cs_test()
