import re

def main():
    phone = input("Enter your phone number as follows (XXX-XXX-XXXX): ")
    ssn = input("Enter your Social Security Number as follows (XXX-XX-XXXX): ")
    zipcode = input("Enter your zip code as follows (XXXXX or XXXXX-XXXX): ")

    print(f"Phone number format is valid: {valid_phone(phone)}")
    print(f"Social Security Number format is valid: {valid_ssn(ssn)}")
    print(f"Zip code format is valid: {valid_zip(zipcode)}")

def valid_phone(phone_number):
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, phone_number))

def valid_ssn(ssn):
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(pattern, ssn))

def valid_zip(zipcode):
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(pattern, zipcode))

if __name__ == "__main__":
    main()