import re

required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])

rhgt = re.compile(r"^(\d+)(cm|in)$")
rhcl = re.compile(r"^#[0-9a-f]{6}$")
recl = re.compile(r"^amb|blu|brn|gry|grn|hzl|oth$")
rpid = re.compile(r"^\d{9}$")


def lax(passport: dict):
    keys = set(passport.keys())
    keys.add("cid")
    return keys == required


def strict(passport: dict):
    keys = set(passport.keys())
    keys.add("cid")

    if keys != required:
        return False

    try:
        valid = True
        byr = int(passport["byr"])
        valid &= 1920 <= byr <= 2002
        iyr = int(passport["iyr"])
        valid &= 2010 <= iyr <= 2020
        eyr = int(passport["eyr"])
        valid &= 2020 <= eyr <= 2030
        hgt, unit = rhgt.match(passport["hgt"]).groups()
        hgt = int(hgt)
        if unit == "cm":
            valid &= 150 <= hgt <= 193
        else:
            valid &= 59 <= hgt <= 76
        hcl = passport["hcl"]
        valid &= bool(rhcl.match(hcl))
        ecl = passport["ecl"]
        valid &= bool(recl.match(ecl))
        pid = passport["pid"]
        valid &= bool(rpid.match(pid))
    except:
        return False

    return valid


def parse(line: str):
    fields = line.replace("\n", " ").strip().split(" ")
    return dict([tuple(field.split(":")) for field in fields])


with open("input", "r") as f:
    passports = [parse(line) for line in f.read().split("\n\n")]

    lax_passports = [passport for passport in passports if lax(passport)]
    print(f"Part one: {len(lax_passports)} valid (lax) passports")

    strict_passports = [passport for passport in passports if strict(passport)]
    print(f"Part two: {len(strict_passports)} valid (strict) passports")
