
# Phishing URL Awareness Checker

**Author:** Darshan Devidas Jadhav

## Project Overview
This project is a Python-based command-line tool that checks URL text for common phishing warning signs.

## Features
- Detects @ symbol.
- Checks URL length.
- Detects IPv4-style hostnames.
- Checks hostname segments.
- Detects punycode markers.
- Identifies HTTP URLs.
- Supports multiple URL checks.
- Handles empty and malformed input.

## Requirements
- Python 3.10 or newer.
- No external packages required.

## How to Run
```bash
python phishing_checker.py
```

## How to Test
```bash
python -m unittest discover -s tests -v
```

## Improvements
- Added a repeat and quit option.
- Added clear warning messages.
- Added basic invalid-input handling.

## Limitations
This tool checks URL text only. It does not visit websites or verify whether a website is safe.

## Ethical Use
Use this project for cybersecurity awareness and educational purposes only.
