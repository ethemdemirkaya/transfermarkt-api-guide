"""Checks that every documented endpoint still answers with 200 and valid JSON.

Endpoints are listed in scripts/endpoints.json. Requests are sent one at a
time with a delay between them to respect Transfermarkt's servers.

Each endpoint ends up in one of these states:
  ok       - 200 with a valid JSON body
  broken   - 404, 5xx, invalid JSON, connection error
  blocked  - the request was stopped by bot protection (202/403/429), so the
             endpoint's real state is unknown. This happens on datacenter IPs
             such as GitHub-hosted runners.
  skipped  - marked "deprecated" in endpoints.json; not requested at all

Exits with a non-zero status only if an endpoint is broken.
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
TIMEOUT_SECONDS = 30
BLOCKED_STATUSES = {202, 403, 429}
ICONS = {"ok": "✅", "broken": "❌", "blocked": "🛡️", "skipped": "⏭️"}


def check(url):
    """Returns (state, status, detail)."""
    request = urllib.request.Request(
        url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"}
    )
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            body = response.read()
            status = response.status
    except urllib.error.HTTPError as error:
        if error.code in BLOCKED_STATUSES:
            return "blocked", error.code, "Blocked by bot protection"
        return "broken", error.code, f"HTTP {error.code}"
    except (urllib.error.URLError, TimeoutError) as error:
        return "broken", None, f"Connection error: {error}"

    if status in BLOCKED_STATUSES:
        return "blocked", status, "Blocked by bot protection"

    # Some endpoints (e.g. quickselect/teams) send JSON with a text/html
    # content type, so parse the body instead of trusting the header.
    try:
        json.loads(body)
    except ValueError:
        return "broken", status, "Response is not valid JSON"
    return "ok", status, ""


def write_summary(rows, counts):
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    lines = [
        "## Endpoint Health Check",
        "",
        " · ".join(f"{ICONS[state]} {state}: **{n}**" for state, n in counts.items()),
        "",
        "| | Doc | URL | Detail |",
        "|:-|:-|:-|:-|",
    ]
    for state, doc, url, status, detail in rows:
        lines.append(f"| {ICONS[state]} | `{doc}` | {url} | {detail or status} |")
    if counts["blocked"]:
        lines += [
            "",
            "> 🛡️ *Blocked* means Transfermarkt's bot protection rejected the request "
            "from this runner's IP, so the endpoint's real state could not be checked. "
            "Run `python scripts/health_check.py` locally to verify these.",
        ]
    with open(summary_path, "a", encoding="utf-8") as summary:
        summary.write("\n".join(lines) + "\n")


def main():
    endpoints = json.loads(
        (Path(__file__).parent / "endpoints.json").read_text(encoding="utf-8")
    )

    rows = []
    counts = dict.fromkeys(ICONS, 0)
    requested = 0
    for endpoint in endpoints:
        if endpoint.get("deprecated"):
            state, status, detail = "skipped", None, "Marked as deprecated"
        else:
            if requested:
                time.sleep(DELAY_SECONDS)
            requested += 1
            state, status, detail = check(endpoint["url"])
        counts[state] += 1
        rows.append((state, endpoint["doc"], endpoint["url"], status, detail))
        print(f"{state.upper():8} {status or '---'} {endpoint['url']}"
              + (f"  ({detail})" if detail else ""))

    write_summary(rows, counts)

    if counts["blocked"] and os.environ.get("GITHUB_ACTIONS"):
        print(f"::warning::{counts['blocked']} endpoint(s) could not be checked "
              "because the runner's IP was blocked by bot protection.")

    sys.exit(1 if counts["broken"] else 0)


if __name__ == "__main__":
    main()
