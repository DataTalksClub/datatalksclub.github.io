import sys
import yaml

REQUIRED_FIELDS = ['time', 'title', 'type']


def main():
    filepath = '_data/events.yaml'

    with open(filepath, encoding='utf-8') as f:
        try:
            events = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"YAML parsing error in {filepath}: {e}")
            print("Suggestion: Check for incorrect indentation, missing quotes, or invalid characters.")
            sys.exit(1)

    if not isinstance(events, list):
        print(f"ERROR: {filepath} must contain a list of events.")
        print("Suggestion: Ensure the file starts with a list (each entry begins with '- ').")
        sys.exit(1)

    errors = []
    for i, event in enumerate(events):
        if not isinstance(event, dict):
            errors.append(
                f"Event at index {i} is not a dictionary. "
                "Suggestion: Ensure each event entry is a YAML mapping (key: value pairs)."
            )
            continue
        for field in REQUIRED_FIELDS:
            if field not in event or not event[field]:
                errors.append(
                    f"Event at index {i} (title: '{event.get('title', 'unknown')}') "
                    f"is missing required field '{field}'. "
                    f"Suggestion: Add '{field}: <value>' to this event entry."
                )
        if 'youtube' in event and event['youtube'] is not None:
            if not isinstance(event['youtube'], str):
                errors.append(
                    f"Event at index {i} (title: '{event.get('title', 'unknown')}') "
                    "has a non-string 'youtube' field. "
                    "Suggestion: Set 'youtube' to a string URL (e.g. https://www.youtube.com/watch?v=...) "
                    "or leave it empty / remove it entirely."
                )

    if errors:
        print(f"Found {len(errors)} error(s) in {filepath}:\n")
        for err in errors:
            print(f"  ERROR: {err}")
        sys.exit(1)

    print(f"Validation passed: {len(events)} events OK.")


if __name__ == "__main__":
    main()
