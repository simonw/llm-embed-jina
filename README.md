# llm-embed-jina

[![PyPI](https://img.shields.io/pypi/v/llm-embed-jina.svg)](https://pypi.org/project/llm-embed-jina/)
[![Changelog](https://img.shields.io/github/v/release/simonw/llm-embed-jina?include_prereleases&label=changelog)](https://github.com/simonw/llm-embed-jina/releases)
[![Tests](https://github.com/simonw/llm-embed-jina/workflows/Test/badge.svg)](https://github.com/simonw/llm-embed-jina/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/llm-embed-jina/blob/main/LICENSE)

Embedding models from Jina AI

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).

    llm install llm-embed-jina

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd llm-embed-jina
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
llm install -e '.[test]'
```
To run the tests:
```bash
pytest
```
