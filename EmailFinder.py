
import re

def find_emails_in_file(file_path):
    with open(file_path, 'r') as infile:
        email_log = infile.readlines()

    emails = []

    for line in email_log:
        emails.extend(re.findall("\w+@\w+\.\w+", line))

    return emails

def main():
    file_path = input("Enter the file path: ")
    emails = find_emails_in_file(file_path)
    print(emails)

if __name__ == "__main__":
    main()
