"""Unified data structure for input and ouput of all the stages in loading process."""

from dataclasses import dataclass
from typing import Dict, List, Tuple, Union

import torch

from .sampled_subgraph import SampledSubgraph

__all__ = ["DataBlock"]


@dataclass
class DataBlock:
    r"""A composite data class for data structure in the graphbolt. It is
    designed to facilitate the exchange of data among different components
    involved in processing data. The purpose of this class is to unify the
    representation of input and output data across different stages, ensuring
    consistency and ease of use throughout the loading process."""

    sampled_subgraphs: List[SampledSubgraph] = None
    """
    A list of 'SampledSubgraph's, each one corresponding to one layer,
    representing a subset of a larger graph structure.
    """

    node_feature: Union[torch.Tensor, Dict[str, torch.Tensor]] = None
    """A representation of node feature.
    - If `node_feature` is a tensor: It indicates the graph is homogeneous.
    - If `node_feature` is a dictionary: The keys should be node type and the
      value should be corresponding node feature or embedding.
    """

    edge_feature: List[
        Union[torch.Tensor, Dict[Tuple[str, str, str], torch.Tensor]]
    ] = None
    """A representation of edge feature corresponding to 'sampled_subgraphs'.
    - If `edge_feature` is a tensor: It indicates the graph is homogeneous.
    - If `edge_feature` is a dictionary: The keys should be edge type and the
      value should be corresponding edge feature or embedding.
    """

    input_nodes: Union[
        torch.Tensor, Dict[Tuple[str, str, str], torch.Tensor]
    ] = None
    """A representation of input nodes in the outermost layer. Conatins all nodes
       in the 'sampled_subgraphs'.
    - If `input_nodes` is a tensor: It indicates the graph is homogeneous.
    - If `input_nodes` is a dictionary: The keys should be node type and the
      value should be corresponding heterogeneous node id.
    """
