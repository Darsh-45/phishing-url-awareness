
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    url = raw_url.strip()

    if not url:
        return ["No URL entered."]

    # Add a default scheme if the user did not enter one.
    candidate = url if "://" in url else "http://" + url

    try:
        parsed = urlparse(candidate)
        hostname = (parsed.hostname or "").lower()
    except ValueError:
        return ["This text is not a valid URL format."]

    if not hostname:
        return ["Could not identify a hostname."]

    warnings = []

    # Check 1: @ symbol
    if "@" in candidate:
        warnings.append(
            "Contains an @ symbol. Check the actual destination hostname."
        )

    # Check 2: URL length
    if len(url) > 100:
        warnings.append("URL is longer than 100 characters.")

    # Check 3: IPv4-style hostname
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", hostname):
        warnings.append("Uses an IPv4-style address as the hostname.")

    # Check 4: Five or more hostname segments
    labels = [part for part in hostname.split(".") if part]
    if len(labels) >= 5:
        warnings.append("Hostname contains five or more segments.")

    # Check 5: Punycode marker
    if "xn--" in hostname:
        warnings.append("Hostname contains an xn-- punycode marker.")

    # Check 6: HTTP scheme
    if parsed.scheme.lower() == "http":
        warnings.append("Uses HTTP instead of HTTPS.")

    if not warnings:
        warnings.append(
            "No listed warning signs found. This does NOT prove the URL is safe."
        )

    return warnings


def main():
    print("=" * 50)
    print("     PHISHING URL AWARENESS CHECKER")
    print("=" * 50)

    print("This program checks URL text only.")
    print("It does not open or visit websites.")

    while True:
        url = input("\nEnter URL (or type q to quit): ")

        if url.strip().lower() in ["q", "quit", "exit"]:
            print("Thank you. Stay safe online!")
            break

        results = inspect_url(url)

        print("\nScan Results:")

        for result in results:
            print("-", result)

        errors = [
            "No URL entered.",
            "Could not identify a hostname.",
            "This text is not a valid URL format."
        ]

        if results[0] not in errors and not results[0].startswith(
            "No listed warning signs"
        ):
            print("\nWARNING: Review this URL carefully.")

        print("Remember: Never share passwords or OTPs through unexpected links.")


if __name__ == "__main__":
    main()
