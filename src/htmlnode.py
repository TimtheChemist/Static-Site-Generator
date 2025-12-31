

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_string = ""

        if self.props == None or self.props == {}:
            return html_string

        for key, value in self.props.items():
            html_string += f'{key}="{value}" '

        return " " + html_string.rstrip()

    def __repr__(self):
        html_node_rep = self.__class__.__name__
        return f'{html_node_rep}(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})'


