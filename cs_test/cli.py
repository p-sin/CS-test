import click

from cs_test.config import Config
from cs_test.project import Project


@click.command()
def cs_test() -> None:
    """Entry point to CS test tool."""
    config = Config()
    config.config_test()

    project = Project(
        project_name=config.project_name,
        project_folder=config.project_path,
        test_path=config.test_path,
        ignored_files=config.ignored_files,
    )

    project.test_project()


if __name__ == "__main__":
    cs_test()
