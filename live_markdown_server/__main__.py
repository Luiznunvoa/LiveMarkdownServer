import argparse
from .server import run_server

def main():
    parser = argparse.ArgumentParser(description="Live Markdown Server")
    parser.add_argument("markdown_path", type=str, help="Path to the Markdown file")
    args = parser.parse_args()
    
    try:
        run_server(args.markdown_path)
    except FileNotFoundError as e:
        print(e)
        exit(1)

if __name__ == "__main__":
    main()
