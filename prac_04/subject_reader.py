"""
Leiyufei Wang
04/12/2022
Practical 04- Files, exceptions
"""

FILENAME = "subject_data.txt"

def main():
    subjects = get_subjects()
    display_subjects(subjects)


def get_subjects():
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        subject.append(parts)
    input_file.close()
    return subject


def display_subjects(subjects):
    """Display data nicely."""
    for subject in subjects:
        # Print using the format method and *unpacking
        print("{} is taught by {:12} and has {:3} students".format(*subject))
        # Another way with f-string instead of format
        # print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()
