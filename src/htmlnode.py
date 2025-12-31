

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


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode has no value.")

        if self.tag is None:
            return self.value

        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'

        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode has no tag.")

        if self.children is None:
            raise ValueError("ParentNode has no children.")


        children_string = ""
        for child in self.children:
            children_string += child.to_html()


        return f'<{self.tag}>{children_string}</{self.tag}>'


