input_file = 'math_problems.txt'

def test_problems():
    f = open(input_file)
    lines = f.read().splitlines()
    f.close()

    for line in lines:
        answer = eval(line)
        # print(line, "=", answer)
        # print line + " = " + answer
        print str(line) + " = " + str(answer)

def main():
    test_problems()

if __name__ == "__main__":
    main()
