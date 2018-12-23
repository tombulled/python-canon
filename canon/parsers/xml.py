import bs4

def parse_xml(xml, parser='html.parser'):
    """
    Parse a string of xml data ('xml') into
    ... a python dictionary

    Note: Tailor made for the canon library
    """

    xml_soup = bs4.BeautifulSoup(xml, parser) # lxml?

    tag_response = xml_soup.find('response')

    data = {}

    for tag_child in tag_response.find_all(recursive=False):
        sub_children_data = {}

        for tag_sub_child in tag_child.find_all(recursive=False):
            sub_children_data[tag_sub_child.name] = tag_sub_child.text

        if sub_children_data:
            child_data = sub_children_data
        else:
            child_data = tag_child.text

        tag_key = tag_child.name

        if tag_key in data:
            if sub_children_data:
                data[tag_key].update(child_data)
            else:
                # WARNING: Overwriting value
                data[tag_key] = child_data
        else:
            data[tag_key] = child_data

    return data
