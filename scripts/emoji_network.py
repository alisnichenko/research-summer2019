import os
import matplotlib.pyplot as plt
# import mplcairo
import numpy as np
from matplotlib.font_manager import FontProperties
import networkx as nx
from matplotlib import font_manager as fm, rcParams
from itertools import combinations

import re
import regex
import emoji

# prototype of a class that i will use for networkx library
class EmojiEdge:
    def __init__(self, emoji_from, emoji_to, weight):
        self.emoji_from = emoji_from
        self.emoji_to = emoji_to
        self.weight = weight

# finding emojis using this crappy method that i found on stackoverflow
# doesn't register emojis like ♀️... 
# apparently windows doesn't either (should be like this:💥)
# flags are separate issue: 🇺🇸 (which is one us flag emoji) actually consists of two emojis
def find_emojis(text):
        emoji_list = []
        # flag_list = regex.findall(u'[\U0001F1E6-\U0001F1FF]', text) 
        data = regex.findall(r'\X', text)
        for word in data:
            try:
                if any(char in emoji.UNICODE_EMOJI for char in word):
                    emoji_list.append(word)
            except:
                continue
        return emoji_list # + flag_list

# writing a dictionary to a file   
def write_dict_to_file(file, dictionary):
    with open(file, 'w', encoding='utf8') as f:
        # key value pair
        for k, v in dictionary.items():
            print(type(v))
            f.write('pair: ' + str(k) + ' value: ' + str(v) + '\n')

def write_list_to_file(file, items):
    with open(file, 'w', encoding='utf8') as f:
        for tup in items:
            f.write(str(tup) + '\n')

def create_edge_list(edge_dict):
    edge_list = []
    # loop through dict using key value pairs
    for k, v in edge_dict.items():
        # getting every emoji out of the key (which is a pair itself)
        edge = (k[0], k[1], v)
        edge_list.append(edge)
    write_list_to_file('test.txt', edge_list)
    return edge_list

# extract edges from a different file
def extract_edges(file):
    edge_list = []
    with open(file, "r", encoding="utf8", errors="ignore") as f:
        for edge in f:
            edge = edge.replace("(", "").replace(")", "").replace("'", "").replace(",", "")
            edge = edge.split()
            # forming an edge
            edge_tuple = (edge[0], edge[1], edge[2])
            edge_list.append(edge_tuple)
    # print(edge_list)
    return edge_list

# draw a graph from emoji dictionary where the key is a pair of emojis
def draw_edge_graph(edge_list):
    G = nx.Graph()
    G.add_weighted_edges_from(edge_list)
    nx.draw_networkx(G, with_labels=True, node_color='w', linewidths=0, font_family='Symbola', font_size = 20)
    plt.show()
    # implementing the graph creation
      
if __name__ == "__main__":
    # Load Microsoft Segoe UI Color Emoji font
    # font_dir = 'C:\\windows\\Fonts\\seguiemj.ttf'
    # G = nx.Graph()
    # Add nodes and edges
    # G.add_weighted_edges_from([("😊", "😱", 2), ("😂", "😊", 10)])
    
    # the file from which i imported my edges created earlier
    fname = "emoji-edges-mod.txt"
    edge_list = extract_edges(fname)
    draw_edge_graph(edge_list)
