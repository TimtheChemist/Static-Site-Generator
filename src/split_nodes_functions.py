from textnode import TextType, TextNode
import re


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



def split_nodes_link(old_nodes):
    list_of_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            list_of_nodes.append(old_node)

        else:
            list_of_urls = extract_markdown_links(old_node.text)

            if list_of_urls == []:
                list_of_nodes.append(old_node)
                continue

            old_node_text_copy = old_node.text
            for i in range(len(list_of_urls)):

                matched_linked_text = list_of_urls[i][0]
                matched_url = list_of_urls[i][1]


                list_of_strings = old_node_text_copy.split(f"[{matched_linked_text}]({matched_url})", 1)

                if len(list_of_strings) < 2:
                    break

                if list_of_strings[0] != "":
                    new_node_text_1 = TextNode(list_of_strings[0], TextType.TEXT)
                    list_of_nodes.append(new_node_text_1)

                new_node_linked_text_2 = TextNode(matched_linked_text, TextType.LINK, matched_url)
                list_of_nodes.append(new_node_linked_text_2)

                if i == (len(list_of_urls) - 1):
                    if list_of_strings[1] == "":
                        continue
                    new_node_text_3 = TextNode(list_of_strings[1], TextType.TEXT)
                    list_of_nodes.append(new_node_text_3)


                old_node_text_copy = list_of_strings[1]
    
    return list_of_nodes


def split_nodes_image(old_nodes):
    list_of_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            list_of_nodes.append(old_node)

        else:
            list_of_urls = extract_markdown_image(old_node.text)
            if list_of_urls == []:
                list_of_nodes.append(old_node)
                continue

            old_node_text_copy = old_node.text
            for i in range(len(list_of_urls)):
                matched_image_alt = list_of_urls[i][0]
                matched_image_link = list_of_urls[i][1]


                list_of_strings = old_node_text_copy.split(f"![{matched_image_alt}]({matched_image_link})", 1)

                if len(list_of_strings) < 2:
                    break

                if list_of_strings[0] != "":
                    new_node_text_1 = TextNode(list_of_strings[0], TextType.TEXT)
                    list_of_nodes.append(new_node_text_1)

                new_node_linked_text_2 = TextNode(matched_image_alt, TextType.IMAGE, matched_image_link)
                list_of_nodes.append(new_node_linked_text_2)

                if i == (len(list_of_urls) - 1):
                    if list_of_strings[1] == "":
                        continue
                    new_node_text_3 = TextNode(list_of_strings[1], TextType.TEXT)
                    list_of_nodes.append(new_node_text_3)

                old_node_text_copy = list_of_strings[1]
    
    return list_of_nodes



def extract_markdown_image(text):
    matches_alt_text = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches_alt_text


def extract_markdown_links(text):
    matches_url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches_url



def text_to_textnodes(text):
    DELIMITERS = ("`", "**", "_")

    processed_text_nodes = [TextNode(text, TextType.TEXT)]

    processed_text_nodes = split_nodes_delimiter(processed_text_nodes, "`", TextType.CODE)
    processed_text_nodes = split_nodes_delimiter(processed_text_nodes, "_", TextType.ITALIC)
    processed_text_nodes = split_nodes_delimiter(processed_text_nodes, "**", TextType.BOLD)

    processed_text_nodes = split_nodes_image(processed_text_nodes)
    processed_text_nodes = split_nodes_link(processed_text_nodes)

    return processed_text_nodes