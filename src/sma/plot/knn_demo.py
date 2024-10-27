import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def knn_demo(
    img_idx,
    neighbor_colors,
    damaged_color,
    fixed_color,
    distances,
    width=15,
    height=4,
    output_format="pdf",
    verbose=False,
):
    """
    Visualizes a K-Nearest Neighbors (KNN) graph representation of a damaged pixel with its neighboring pixels
    and a fixed pixel, saving the plot to a specified format.

    This function creates a directed graph where nodes represent the damaged pixel, its neighboring pixels,
    and the fixed pixel. Edges between nodes are labeled with distances, and each node is color-coded based
    on its pixel color. The plot is saved as an image in the specified `output_format` and can optionally
    be displayed.

    :param img_idx: Unique identifier for the image being processed.
    :type img_idx: int
    :param neighbor_colors: Array of RGB values for the neighboring pixels.
    :type neighbor_colors: list of array-like or np.ndarray
    :param damaged_color: RGB values for the damaged pixel.
    :type damaged_color: array-like or np.ndarray
    :param fixed_color: RGB values for the fixed pixel.
    :type fixed_color: array-like or np.ndarray
    :param distances: Array of distances between the damaged pixel and each neighboring pixel.
    :type distances: list or np.ndarray
    :param width: Width of the figure for the plot (default: 15).
    :type width: float
    :param height: Height of the figure for the plot (default: 4).
    :type height: float
    :param output_format: File format to save the plot, such as 'pdf' or 'png' (default: 'pdf').
    :type output_format: str
    :param verbose: Boolean to control whether to display the plot (default: False).
    :type verbose: bool
    :return: None
    :rtype: None
    """
    plt.rc("font", family="STIXGeneral")
    G = nx.DiGraph()

    input_node = "Input"
    hidden_layer = [f"Hidden_{i+1}" for i in range(len(neighbor_colors))]
    output_node = "Output"

    positions = {input_node: (0, 0)}
    for i, node in enumerate(hidden_layer):
        positions[node] = (i - (len(hidden_layer) - 1) / 2, 1)
    positions[output_node] = (0, 2)

    G.add_node(input_node)
    for node in hidden_layer:
        G.add_node(node)
    G.add_node(output_node)

    for hidden_node in hidden_layer:
        G.add_edge(input_node, hidden_node)
        G.add_edge(hidden_node, output_node)

    input_color = damaged_color / 255.0
    hidden_colors = [color / 255.0 for color in neighbor_colors]
    output_color = fixed_color / 255.0
    node_colors = [input_color] + hidden_colors + [output_color]
    plt.figure(figsize=(width, height))
    nx.draw_networkx_nodes(
        G, positions, node_color=node_colors, node_size=1000, node_shape="s"
    )
    edge_labels = {
        (input_node, hidden_node): f"{dist:.2f}"
        for hidden_node, dist in zip(hidden_layer, distances)
    }
    nx.draw_networkx_edges(
        G, positions, arrowstyle="-|>", arrowsize=20, alpha=0.6, node_size=2000
    )

    rgb_labels = (
        [f"Damaged pixel\n({damaged_color[0]}, {damaged_color[1]}, {damaged_color[2]})"]
        + [
            f"Neighbor pixel\n({color[0]}, {color[1]}, {color[2]})"
            for color in neighbor_colors
        ]
        + [f"Fixed pixel\n({fixed_color[0]}, {fixed_color[1]}, {fixed_color[2]})"]
    )

    rgb_positions = {node: (x, y) for (node, (x, y)) in positions.items()}
    nx.draw_networkx_labels(
        G,
        rgb_positions,
        labels={node: rgb for node, rgb in zip(G.nodes(), rgb_labels)},
        font_size=8,
    )
    nx.draw_networkx_edge_labels(
        G, positions, edge_labels=edge_labels, font_color="black"
    )

    plt.gca().invert_yaxis()
    plt.axis("off")

    plt.savefig(
        f"img/{img_idx}_{idx + 1}_{key}_knn_demo.{output_format}",
        format=output_format,
        bbox_inches="tight",
    )

    if verbose:
        plt.show()

    plt.close()
