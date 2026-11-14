#!/usr/bin/python3
"""Generate personalized invitation files from a template."""
import os


def generate_invitations(template, attendees):
    """Write one output_X.txt file per attendee, filling the template."""
    if not isinstance(template, str):
        print("Error: template must be a string, got {}.".format(
            type(template).__name__))
        return
    if not isinstance(attendees, list) or \
            not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries, got {}."
              .format(type(attendees).__name__))
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]
    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", str(value))

        filename = "output_{}.txt".format(index)
        if os.path.exists(filename):
            print("Warning: {} already exists and will be overwritten."
                  .format(filename))
        try:
            with open(filename, "w") as f:
                f.write(content)
        except OSError as e:
            print("Error writing {}: {}".format(filename, e))
