import os
from pathlib import Path
import typer
import requests

app = typer.Typer()

access_token = os.environ.get("DOCUGAMI_API_KEY")
if not access_token:
    raise Exception("Please set Docugami API key environment variable")


@app.command()
def upload_file(
    file_path: Path = typer.Option(
        file_okay=True,
        dir_okay=False,
        resolve_path=True,
        exists=True,
        help="Path to file that should be uploaded",
    ),
):
    """
    Upload a file to Docugami.
    """

    try:
        with open(file_path, "rb") as file:
            files = [("file", (file_path.name, file))]
            headers = {"Authorization": f"Bearer {access_token}"}

            response = requests.post(
                "https://api.docugami.com/v1preview1/documents/content",
                headers=headers,
                data={},
                files=files,
            )

            if response.ok:
                typer.echo("File uploaded successfully!")
                typer.echo(response.text)
            else:
                typer.echo(f"Error uploading file: {response.status_code}")
    except FileNotFoundError:
        typer.echo(f"File not found: {file_path}")
    except Exception as e:
        typer.echo(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app()
