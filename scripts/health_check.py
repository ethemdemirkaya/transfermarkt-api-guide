"""Checks that every documented endpoint still answers with 200 and valid JSON.

Endpoints are listed in scripts/endpoints.json. Requests are sent one at a
time with a delay between them to respect Transfermarkt's servers.
Exits with a non-zero status if any endpoint fails.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

USER_AGENT = (
    "transfermarkt-api-guide-healthcheck/1.0 "
    "(https://github.com/ethemdemirkaya/transfermarkt-api-guide)"
)
DELAY_SECONDS = 2
TIMEOUT_SECONDS = 20


def check(url):
    request = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            body = response.read()
            status = response.status
    except urllib.error.HTTPError as error:
        return error.code, f"HTTP {error.code}"
    except (urllib.error.URLError, TimeoutError) as error:
        return None, f"Connection error: {error}"

    # Some endpoints (e.g. quickselect/teams) send JSON with a text/html
    # content type, so parse the body instead of trusting the header.
    try:
        json.loads(body)
    except ValueError:
        return status, "Response is not valid JSON"
    return status, None


def main():
    endpoints = json.loads(
        (Path(__file__).parent / "endpoints.json").read_text(encoding="utf-8")
    )

    rows = []
    failures = 0
    for index, endpoint in enumerate(endpoints):
        if index:
            time.sleep(DELAY_SECONDS)
        status, error = check(endpoint["url"])
        ok = error is None
        failures += not ok
        rows.append((ok, endpoint["doc"], endpoint["url"], status, error))
        print(f"{'OK  ' if ok else 'FAIL'} {status or '---'} {endpoint['url']}"
              + (f"  ({error})" if error else ""))

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        lines = [
            "## Endpoint Health Check",
            "",
            f"**{len(rows) - failures}/{len(rows)}** endpoints healthy.",
            "",
            "| | Doc | URL | Status |",
            "|:-|:-|:-|:-|",
        ]
        for ok, doc, url, status, error in rows:
            lines.append(
                f"| {'✅' if ok else '❌'} | `{doc}` | {url} | {error or status} |"
            )
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write("\n".join(lines) + "\n")

    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
