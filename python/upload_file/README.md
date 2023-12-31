# Upload a File

Sample python command-line tool that uploads a file to Docugami.

## Dependencies

1. Make sure you have [Python](https://www.python.org/downloads/) installed.

1. Install python dependencies, e.g. via `pip3 install -r requirements.txt` in this dir or in a virtual env (recommended).

## Auth

Make sure your Docugami access token is set as the `DOCUGAMI_API_KEY` environment variable.

## Instructions

To upload a file to Docugami, use the following command:

```shell
python3 cli.py upload-file <file_path>
```

<file_path>: The path to the file you want to upload.

The file ID of the uploaded file will be printed to standard out.
