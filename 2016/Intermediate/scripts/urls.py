import urllib.request

input_file = 'urls.txt'
valid_output_file = 'valid_urls.txt'

def test_urls():

    f = open(input_file)
    lines = f.read().splitlines()
    f.close()

    v = open(valid_output_file, "w")

    for line in lines:
        try:
            urllib.request.urlopen(line)
            v.write(line + "\n")
            v.flush()
        except urllib.error.URLError as error:
            print(line, error)
        except urllib.error.HTTPError as error:
            print(line, error.code)

    v.close

def main():
    test_urls()

if __name__ == "__main__":
    main()
