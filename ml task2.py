from pathlib import Path
import webbrowser
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

base_dir = Path(__file__).resolve().parent
html_path = base_dir / "ml task2.html"
if not html_path.exists():
    raise SystemExit(f"Missing dashboard file: {html_path}")

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass


def main():
    port = 8000
    server = ThreadingHTTPServer(("127.0.0.1", port), lambda *args, **kwargs: QuietHandler(*args, directory=str(base_dir), **kwargs))
    print(f"Opening dashboard at http://127.0.0.1:{port}/ml task2.html")
    webbrowser.open(html_path.resolve().as_uri())
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
