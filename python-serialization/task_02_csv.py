#!/usr/bin/env python3
"""Convert CSV data to JSON."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to data.json."""
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except FileNotFoundError:
        return False
