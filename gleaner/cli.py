# Handles arg parsing
# Entry point for gleaning
import argparse

from .scraper import Gleaner


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("-o", "--output", default="urls.txt")
    args = parser.parse_args()

    print(f"Gleaning: {args.url}")
    gleaner = Gleaner(start_url=args.url, output_file=args.output)
    gleaner.scrape()
    print(f"Output save to {args.output}")


if __name__ == "__main__":
    main()
