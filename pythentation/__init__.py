'''Simple utility to make a pretty presentations from markdown text
'''
import markdown
import sys


def generate(text):
    return markdown.markdown(text, ['codehilite', 'splitsections'])


def main():
    argc = len(sys.argv)
    if argc < 2:
        raise Exception('No input file specified.')
    elif argc > 3:
        raise Exception('To many arguments.')
    elif argc == 2:
        input_file = sys.argv[1]
        output_file = input_file + '.html'
    else:
        input_file, output_file = sys.argv[1:]
    text = ''.join(open(input_file).readlines())
    html = generate(text)
    write_handle = open(output_file, 'w')
    write_handle.write(html)
    write_handle.close()


if __name__ == '__main__':
    main()
