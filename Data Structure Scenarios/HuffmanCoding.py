import sys
from collections import Counter


class HuffmanNode():
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None

    def is_leaf(self):
        return self.left == None and self.right == None


def get_character_frequency(data):
    freq_counter = Counter(data)
    char_frequencies = freq_counter.most_common()
    frequency_nodes = []
    for index in range(len(char_frequencies) - 1, -1, -1):
        character_frequency = char_frequencies[index]
        node = HuffmanNode(character_frequency[0], character_frequency[1])
        frequency_nodes.append(node)

    return frequency_nodes


def sort_frequency_nodes(frequency_nodes):
    #print(len(frequency_nodes))
    return sorted(frequency_nodes, key = lambda x: x.frequency, reverse = True)


def create_huffman_tree(data):
    frequency_nodes = get_character_frequency(data)

    while(len(frequency_nodes) > 1):
        #pick the least two frequent characters
        least_freq_node1 = frequency_nodes.pop()
        least_freq_node2 = frequency_nodes.pop()
        #create a parent with their sum value
        parent_node_value = least_freq_node1.frequency + least_freq_node2.frequency
        parent_node = HuffmanNode(None, parent_node_value)
        parent_node.left = least_freq_node1
        parent_node.right = least_freq_node2
        #add that to the list
        frequency_nodes.append(parent_node)
        #sort the list
        frequency_nodes = sort_frequency_nodes(frequency_nodes)

    return frequency_nodes[0]

def generate_character_codes(huffman_tree_root):
    root = huffman_tree_root
    char_code = ''
    character_code_map = {}
    #navigate (dfs) all nodes and generate codes
    generate_code(root, char_code, character_code_map)
    return character_code_map


def generate_code(node, code, character_code_map):
    if node.is_leaf():
        character = node.character
        character_code_map[character] = code
    else:
        if node.left != None:
            generate_code(node.left, code + '0', character_code_map)
        if node.right != None:
            generate_code(node.right, code + '1', character_code_map)

def generate_characters(data, tree_root):
    index = 0
    node = tree_root
    decoded_data = ''
    while(index < len(data)):
        binary_character = data[index]
        #go left or right based on the binary character
        if(binary_character == '0'):
            node = node.left
        elif(binary_character == '1'):
            node = node.right
        #if node is leaf, then this is the character node
        if(node.is_leaf()):
            decoded_data += node.character
            node = tree_root
        index += 1

    return decoded_data

def huffman_encoding(data):
    huffman_tree_root = create_huffman_tree(data)
    character_code_map = generate_character_codes(huffman_tree_root)
    encoded_data = ''
    for character in data:
        encoded_data += character_code_map[character]

    return encoded_data, huffman_tree_root


def huffman_decoding(data, tree):
    decoded_data = generate_characters(data, tree)
    return decoded_data

if __name__ == '__main__':
    codes = {}

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {} \n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    #The size of the data is: 45
    #The content of the data is: The bird is the word

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    #The size of the encoded data is: 22
    #The content of the encoded data is: 0000111001110000110101011100110101001101100111111001110010001011011100

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    #The size of the decoded data is: 45
    #The content of the encoded data is: The bird is the word
    

    # Additional test case - with contents from an e-book
    # Contains first 10 chapters of the popular book - Anna Karenina
    # E-Book - Anna Karenina by Leo Tolstoy - from Project Gutenburg
    # Content extracted and cleared of non-unicode characters

    with open('Anna_Karenina_leo_tolstoy.txt', 'rt') as _file :
        contents = _file.read()
        print("The size of the e-book contents is: {} \n".format(sys.getsizeof(contents)))
        # prints "The size of the e-book contents is: 94190" . (~95 KB)

        encoded_book_data, book_tree = huffman_encoding(contents)
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_book_data, base=2))))
        # prints "The size of the encoded data is: 56972" . (~56 KB)

        decoded_book_data = huffman_decoding(encoded_book_data, book_tree)
        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_book_data)))
        # prints "The size of the decoded data is: 94190" . (~95 KB)
