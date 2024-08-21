Python 3.12.3 (v3.12.3:f6650f9ad7, Apr  9 2024, 08:18:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

>>> import torch
... import torch.nn.functional as F
... from torch_geometric.nn import GCNConv
... 
... class GCN(torch.nn.Module):
...     def __init__(self, in_channels, hidden_channels, out_channels):
...         super(GCN, self).__init__()
...         self.conv1 = GCNConv(in_channels, hidden_channels)
...         self.conv2 = GCNConv(hidden_channels, out_channels)
... 
...     def forward(self, x, edge_index):
...         x = self.conv1(x, edge_index)
...         x = F.relu(x)
...         x = self.conv2(x, edge_index)
...         return F.log_softmax(x, dim=1)
