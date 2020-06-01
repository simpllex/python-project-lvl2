from gendiff.parser import parse_args
from gendiff.engine import puf


def main():
    options = parse_args()
    diff_string = puf(options.first_file,
                                options.second_file)


if __name__ == '__main__':
    main()
    
