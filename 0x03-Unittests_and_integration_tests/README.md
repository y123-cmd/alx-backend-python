# Python Utilities Testing Project

This project contains utility functions, a GitHub API client, and their corresponding unit and integration tests. It is written in Python 3.7 and is compliant with Ubuntu 18.04 standards.

## 📁 Project Structure

```
.
├── utils.py                   # Utility module with reusable functions
├── test_utils.py              # Unit tests for utils.py
├── client.py                  # GitHubOrgClient implementation
├── test_client.py             # Unit and integration tests for client.py
├── fixtures.py                # Sample payloads used for integration testing
├── README.md                  # Project documentation
```

## 🛠️ Requirements

- Python 3.7
- `parameterized` module for test expansion
- `pycodestyle` version 2.5
- `requests` for GitHub API access
- Unix-based system (Ubuntu 18.04 LTS recommended)

Install dependencies:

```bash
pip install parameterized pycodestyle==2.5 requests
```

## 📌 Features

- `access_nested_map`: Retrieve a value from a nested dictionary using a sequence of keys.
- `get_json`: Fetch JSON data from a URL.
- `memoize`: Decorator for caching method results.
- `GithubOrgClient`: Client to interact with GitHub Organization APIs.
- Full unit and integration test coverage using `unittest` and `parameterized`.
- PEP8-compliant (`pycodestyle` 2.5).
- All modules, classes, and functions are type-annotated and documented with complete sentences.

## ✅ Running Tests

You can run all tests using the built-in `unittest` module:

```bash
python3 -m unittest discover
```

## 🧪 Sample Test Cases

The test suite includes:

- Unit tests for nested dictionary access, JSON fetching, and memoization
- Mocked GitHub API responses for robust testing of `GithubOrgClient`
- Parameterized tests for license filtering and public repo listing
- Integration tests using fixture-based mocking

## ⚙️ Conventions Followed

- All files begin with a proper shebang (`#!/usr/bin/env python3`)
- All files end with a newline
- All modules, classes, and functions include clear, complete-sentence docstrings
- Executable permissions (`chmod +x`) are applied to scripts
- Type hints are used throughout the codebase
