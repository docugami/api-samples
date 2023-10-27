from pathlib import Path
import typer
import requests

app = typer.Typer()


@app.command()
def upload_file(
    access_token: str,
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

    :param file_path: Path to the file you want to upload.
    :param access_token: Docugami API access token.
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
            else:
                typer.echo(f"Error uploading file: {response.status_code}")
    except FileNotFoundError:
        typer.echo(f"File not found: {file_path}")
    except Exception as e:
        typer.echo(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    app()
