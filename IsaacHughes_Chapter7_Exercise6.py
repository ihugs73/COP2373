import re

def validate_phone(phone):
    """
    Validate a phone number.
    Acceptable formats:
      - 123-456-7890
      - (123) 456-7890
      - 123 456 7890
      - 1234567890
    """
    pattern = re.compile(r'^\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}$')
    return bool(pattern.match(phone))

def validate_ssn(ssn):
    """
    Validate a Social Security Number (SSN).
    Expected format: 123-45-6789
    """
    pattern = re.compile(r'^\d{3}-\d{2}-\d{4}$')
    return bool(pattern.match(ssn))

def validate_zip(zip_code):
    """
    Validate a U.S. zip code.
    Acceptable formats:
      - 12345
      - 12345-6789
    """
    pattern = re.compile(r'^\d{5}(-\d{4})?$')
    return bool(pattern.match(zip_code))

def main():
    phone = input("Enter a phone number: ")
    ssn = input("Enter a social security number (SSN) [format: 123-45-6789]: ")
    zip_code = input("Enter a zip code: ")

    if validate_phone(phone):
        print("Valid phone number.")
    else:
        print("Invalid phone number.")

    if validate_ssn(ssn):
        print("Valid social security number.")
    else:
        print("Invalid social security number.")

    if validate_zip(zip_code):
        print("Valid zip code.")
    else:
        print("Invalid zip code.")

if __name__ == "__main__":
    main()
