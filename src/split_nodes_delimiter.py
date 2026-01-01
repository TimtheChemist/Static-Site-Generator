from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            list_of_nodes.append(old_node)

        else:
            list_of_strings = old_node.text.split(delimiter)

            if len(list_of_strings) % 2 == 0:
                raise Exception("Unmatched delimiter detected!")

            string_counter = 1
            for text_string in list_of_strings:

                if text_string == "":
                    string_counter += 1
                    continue

                if string_counter % 2 != 0:
                    new_node = TextNode(text_string, TextType.TEXT)
                    list_of_nodes.append(new_node)
                    string_counter += 1

                else:
                    new_node = TextNode(text_string, text_type)
                    list_of_nodes.append(new_node)
                    string_counter += 1


    return list_of_nodes


