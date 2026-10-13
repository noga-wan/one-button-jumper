# One Button Jumper

An endless one-button platformer that runs in the browser. Tap for a short hop, hold for a big jump, and press again in mid-air to double jump.

- 8 levels plus an endless mode, getting faster and harder as you go
- Collect coins and spend them in the store on colors, trails, weapons, and upgrades
- Power-ups, gravity-flip zones, missions, and synthesized music and sound effects

**Play it live:** https://noga-wan.github.io/one-button-jumper/

Controls: Space / ↑ / click / tap. S opens the store, M toggles music, N toggles sound effects.

## Run it locally

The project includes a small web server ([`server.py`](server.py)). It needs Python 3 and nothing else.

```sh
python3 server.py
```

Then open **http://localhost:8000/** in your browser.

Caching is turned off, so after you edit `index.html` a browser refresh shows the change.

| Option | What it does |
|---|---|
| `--port 9000` | Use a different port |
| `--open` | Open the game in your browser automatically |
| `--lan` | Let phones and other devices on your Wi-Fi connect; the address is printed when the server starts |

Stop the server with Ctrl+C.
