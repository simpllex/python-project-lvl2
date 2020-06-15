from gendiff.parser import parse_args
from gendiff.engine import return_string, read_file


def main():
    options = parse_args()
    old = read_file(options.first_file)
    new = read_file(options.second_file)
    diff = return_string(old, new)
    print(diff)


if __name__ == '__main__':
    main()
