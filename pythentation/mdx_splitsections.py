'''Extension that split document into sections using a h1/h2 tags
'''
import markdown
import re
import unidecode


def slugify(str):
    '''To slug
    '''
    str = unidecode.unidecode(str).lower()
    return re.sub(r'\W+', '-', str)


def split_sections(tree, tag, slide_class, head_class=None):
    '''Add section 
    '''
    head_class = head_class or slide_class
    wrapper = None
    toc = markdown.util.etree.Element('nav')  # create a table of content
    children = list(tree)
    for i, child in enumerate(children):
        # should allow lower level to stop as well
        m = re.search(r"h(\d+)", child.tag)
        tag_level = int(m.group(1)) if m else 0
        if tag_level == 1 or tag_level == 2:
            # Create a new wrapper to start new section
            wrapper = markdown.util.etree.Element(tag)
            wrapper.set('class', head_class if tag_level == 1 else slide_class)
            wrapper.set('id', slugify(child.text))
            tree.remove(child)
            tree.insert(i, wrapper)
            wrapper.append(child)
            # Add into table of content
            toc_item = markdown.util.etree.Element('a')
            toc_item.text = child.text
            toc_item.set('href', '#' + wrapper.get('id'))
            toc_item.set('title', child.text)
            toc.append(toc_item)
        elif wrapper:
            # Add an element into exists wrapper
            tree.remove(child)
            wrapper.append(child)
    # Put a table of content as first element
    tree.insert(0, toc)


class SplitSectionsTreeprocessor(markdown.treeprocessors.Treeprocessor):
    '''Markdown tree processor used to create a sections from headers
    '''

    def run(self, doc):
        split_sections(doc, self.config.get("tag")[0],
                     self.config.get("slide_class")[0],
                     self.config.get("head_class")[0])


class SplitSectionsExtension(markdown.Extension):
    '''Class for adding an extion to markdown
    '''

    def __init__(self, configs):
        self.config = {
            'tag': ['section', 'tag name to use, default: section'],
            'slide_class': ['section', 'slide class name'],
            'head_class': [None, 'head slide class name']
        }
        for key, value in configs:
            self.setConfig(key, value)

    def extendMarkdown(self, md, md_globals):
        '''Extend markdown with AddSectionsTreeprocessor
        '''
        ext = SplitSectionsTreeprocessor(md)
        ext.config = self.config
        md.treeprocessors.add("splitsections", ext, "_end")

    
def makeExtension(configs={}):
    '''Create extension
    '''
    return SplitSectionsExtension(configs=configs)
