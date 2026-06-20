import re

def extract_aadhaar_data(text: str):
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    name = None
    dob = None
    gender = None
    aadhaar_number = None
    mobile = None
    address = None

    match = re.search(r"(\d{4}\s?\d{4}\s?\d{4})", text)
    if match:
        aadhaar_number = match.group(1)

    dob_match = re.search(r"(\d{2}[/-]\d{2}[/-]\d{2})", text)

    text_lower = text.lower()
    if "female" in text_lower:
        gender = "female"
    else:
        gender = "male"

    if dob_match:
        dob = dob_match.group(1)

    for i, line in enumerate(lines):
        if "dob" in line.lower():
            if i > 0:
                candidate = lines[i - 1]
                if not any(char.isdigit() for char in candidate):
                    name = candidate
            break

    for i, line in enumerate(lines):
        if "/O" in line:
            if i > 0:
                address = ""
                for l in range(1, len(lines) - i - 1):
                    current = lines[i + l]
                    if "mobile" in current.lower():
                        break
                    address += current + " "
            break

    mob_match = re.search(r"(\d{10})", text)
    if mob_match:
        mobile = mob_match.group(1)

    return {
        "name": name,
        "dob": dob,
        "gender": gender,
        "aadhaar_number": aadhaar_number,
        "mobile": mobile,
        "address": address
    }