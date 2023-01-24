<h1 id="header" align="center">
    ChatXGPT
    <div id="badge">
        <img id="code-size" src="https://img.shields.io/github/languages/code-size/BugReportOnWeb/ChatXGPT" />
        <img id="last-commit" src="https://img.shields.io/github/last-commit/BugReportOnWeb/ChatXGPT" />
    </div>
</h1>

## Installation
Clone the repository to a desired destination and head inside the same.
```bash
$ git clone https://github.com/BugReportOnWeb/ChatXGPT.git
$ cd ChatXGPT
```

Make a `.env` file and store your bot token in it.
```bash
$ vim .env
----------------------------
OPENAI_API_KEY=<YOUR-TOKEN-GOES-HERE>
```

Install the dependencies and run the main script.
```bash
$ python3 -m pip install -U requirements.txt
$ python3 src/main.py
```

## Dependencies
* [openai](https://pypi.org/project/openai/) (Python client library for the OpenAI API)
* [python-dotenv](https://pypi.org/project/python-dotenv/) (Read key-value pairs from a .env file and set them as environment variables)
