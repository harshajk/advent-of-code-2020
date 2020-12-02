def count_good_passwords_p1(filename):
    good_pwd_count = 0
    with open(filename,"r") as f:
        for l in f.readlines():
            rules_str, letter_str, password_str = l.split(" ")
            rule_min, rule_max = [int(m) for m in rules_str.split("-")]
            letter = letter_str[0]
            password = password_str.strip() # strip the new line at the end of the string
            letter_count = password.count(letter)
            if letter_count in range(rule_min, rule_max + 1):
                good_pwd_count += 1
    return good_pwd_count

def count_good_passwords_p2(filename):
    good_pwd_count = 0
    with open(filename,"r") as f:
        for l in f.readlines():
            rules_str, letter_str, password_str = l.split(" ")
            positions = [int(m) -1 for m in rules_str.split("-")]
            letter = letter_str[0]
            password = password_str.strip() # strip the new line at the end of the string
            if (password[positions[0]] == letter) ^ (password[positions[1]] == letter):
                good_pwd_count += 1
    return good_pwd_count

if __name__ == '__main__':
    #result = count_good_passwords_p1("input/day02.txt")
    #result = count_good_passwords_p2("input/day02test.txt")
    result = count_good_passwords_p2("input/day02.txt")
    print(result)