#!/usr/bin/env python3
"""Local web server for One Button Jumper.

Serves the game from this folder with caching turned off, so edits show up
as soon as you refresh the browser. Uses only the Python standard library.

    python3 server.py              # http://localhost:8000
    python3 server.py --port 9000  # pick another port
    python3 server.py --lan        # also reachable from phones on your Wi-Fi
    python3 server.py --open       # open the game in your browser
"""
import argparse
import functools
import http.server
import socket
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def lan_ip():
    # The address this machine uses to reach the network; no packets are sent.
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(("10.255.255.255", 1))
            return s.getsockname()[0]
        except OSError:
            return None


def main():
    parser = argparse.ArgumentParser(description="Serve One Button Jumper locally.")
    parser.add_argument("--port", type=int, default=8000, help="port to listen on (default: 8000)")
    parser.add_argument("--lan", action="store_true", help="listen on all interfaces so other devices can connect")
    parser.add_argument("--open", action="store_true", help="open the game in your default browser")
    args = parser.parse_args()

    host = "0.0.0.0" if args.lan else "127.0.0.1"
    handler = functools.partial(NoCacheHandler, directory=str(ROOT))
    with http.server.ThreadingHTTPServer((host, args.port), handler) as httpd:
        url = f"http://localhost:{args.port}/"
        print(f"One Button Jumper running at {url}")
        if args.lan and (ip := lan_ip()):
            print(f"On your Wi-Fi network:     http://{ip}:{args.port}/")
        print("Press Ctrl+C to stop.", flush=True)
        if args.open:
            webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
