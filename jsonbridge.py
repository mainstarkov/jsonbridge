#!/usr/bin/env python3
"""Convert JSON arrays and CSV files without dependencies."""
import argparse
import csv
import json
from pathlib import Path

def json_to_csv(source: Path, target: Path) -> None:
    data = json.loads(source.read_text(encoding="utf-8"))
    if not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        raise ValueError("JSON must contain an array of objects")
    fields = list(dict.fromkeys(key for row in data for key in row))
    with target.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader(); writer.writerows(data)

def csv_to_json(source: Path, target: Path) -> None:
    with source.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    target.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser(description="Convert JSON to CSV and CSV to JSON")
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    args = parser.parse_args()
    if not args.source.is_file(): parser.error("source file does not exist")
    if args.source.suffix.lower() == ".json" and args.target.suffix.lower() == ".csv":
        json_to_csv(args.source, args.target)
    elif args.source.suffix.lower() == ".csv" and args.target.suffix.lower() == ".json":
        csv_to_json(args.source, args.target)
    else:
        parser.error("use .json -> .csv or .csv -> .json")
    print(f"Created {args.target}")

if __name__ == "__main__":
    main()
