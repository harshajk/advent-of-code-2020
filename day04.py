import re

req_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

def get_passports(filename):    
    passports = []
    current = {}
    with open(filename,"r") as f:
        for l in f.readlines():
            l = l.strip()
            if l == '':
                passports.append(current)
                current = {}
            for field in l.split():
                k, v = field.split(':')
                current[k] = v

    passports.append(current)
    #print (passports)
    return passports

def day4_p1(passports):
    #print (passports)
    valid_passports = 0
    #print (req_keys)
    for p in passports:
        #print (p)
        missing = req_keys - set(p.keys())
        if missing == {'cid'}  or len(missing) == 0:
            #print (missing)
            valid_passports += 1
    return valid_passports

def day4_p2(passports):
    #print (passports)
    valid_passports = 0
    for p in passports:
        #print(p)
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if (not re.fullmatch(r'\d{4}', p.get('byr','')) or not (1920 <= int (p.get('byr',''))<=2002)):
            continue
        #else:
            #print(p.get('byr',''))
        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if (not re.fullmatch(r'\d{4}', p.get('iyr','')) or not (2010 <= int (p.get('iyr',''))<=2020)):
            continue
        #else:
            #print(p.get('iyr',''))
        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if (not re.fullmatch(r'\d{4}', p.get('eyr','')) or not (2020 <= int (p.get('eyr',''))<=2030)):
            continue
        #else:
            #print(p.get('eyr',''))

        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        # If in, the number must be at least 59 and at most 76.
        hm = re.fullmatch(r'(\d+)(cm|in)', p.get('hgt',''))
        if not hm:
            continue
        height = int(hm.group(1))
        if hm.group(2) == 'cm':
            if not (150 <= height <= 193):
                continue
        else:
            if not (59 <= height <= 76):
                continue

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if not re.fullmatch(r'#[0-9a-f]{6}', p.get('hcl','')):
            continue

        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        ecls = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        if p.get('ecl', '') not in ecls:
            continue

        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if not re.fullmatch(r'[0-9]{9}', p.get('pid','')):
            continue

        # cid (Country ID) - ignored, missing or not.
        valid_passports += 1
    return valid_passports

if __name__ == '__main__':
    passports_test = get_passports("input/day04test.txt")
    passports_real = get_passports("input/day04.txt")
    #Part 1 Test
    print("\nPart-1")
    result = day4_p1(passports_test)
    print(result)
    # #Part 1 Real
    result = day4_p1(passports_real)
    print(result)
    print("\nPart-2")
    # #Part 2 Test
    result = day4_p2(passports_test)
    print(result)
    # #Part 2 Real
    result = day4_p2(passports_real)
    print(result)