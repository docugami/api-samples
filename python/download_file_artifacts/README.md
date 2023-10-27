# Download File Artifacts

Sample python command-line tool that downloads artifacts for a file processed by Docugami.

## Dependencies

1. Make sure you have [Python](https://www.python.org/downloads/) installed.

1. Install python dependencies, e.g. via `pip3 install -r requirements.txt` in this dir or in a virtual env (recommended).

## Auth

Make sure your Docugami access token is set as the `DOCUGAMI_API_KEY` environment variable.

## Instructions

To download processed artifacts for a file from Docugami, use the following command:

```shell
python3 cli.py download-file <docset_id> <document_id>
```

1. <docset_id>: The document set ID of a file that has previously been uploaded and processed.
1. <document_id>: The file ID of a file that has previously been uploaded and processed.

The latest XML artifact for the file will be downloaded and printed to standard out. You can modify the code to download other artifacts, see API docs for details.

