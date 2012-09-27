'''Simple utility to make a pretty presentations from markdown text
'''
import markdown
import os
import sys

ROOT_PATH = os.path.realpath(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.join(ROOT_PATH, 'template.html')
STYLE_PATH = os.path.join(ROOT_PATH, 'style.css')
HEAD_PATH = os.path.join(ROOT_PATH, 'head.min.js')
REVEAL_PATH = os.path.join(ROOT_PATH, 'reveal.min.js')
SCRIPT_PATH = os.path.join(ROOT_PATH, 'script.js')


def generate(text):
    '''Generate a html from markdown text
    '''
    return markdown.markdown(text, extensions=('codehilite', 'splitsections'))


def main():
    '''Main application
    '''
    # Check arguments
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
    # Retrive a text and generate result
    text = ''.join(open(input_file).readlines())
    content = generate(text)
    template = ''.join(open(TEMPLATE_PATH).readlines())
    style = ''.join(open(STYLE_PATH).readlines())
    script = ''.join(open(HEAD_PATH).readlines() +
                     open(REVEAL_PATH).readlines() +
                     open(SCRIPT_PATH).readlines())
    html = template.format(content=content, title='Presentation',
                           style=style, script=script)
    # Write result
    write_handle = open(output_file, 'w')
    write_handle.write(html)
    write_handle.close()


if __name__ == '__main__':
    main()
