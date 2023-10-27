import os
from pathlib import Path
import typer
import requests

app = typer.Typer()

access_token = os.environ.get("DOCUGAMI_API_KEY")
if not access_token:
    raise Exception("Please set Docugami API key environment variable")


@app.command()
def download_file(docset_id: str, document_id: str):
    """
    Downloads the latest XML artifact for a file processed by Docugami.
    """
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(
        f"https://api.docugami.com/v1preview1/docsets/{docset_id}/documents/{document_id}/dgml",
        headers=headers,
    )

    if response.ok:
        typer.echo(response.text)
    else:
        raise Exception(f"Failed to download artifacts (status: {response.status_code})")


if __name__ == "__main__":
    app()
