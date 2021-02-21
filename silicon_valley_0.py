"""
Silicon Valley - s01e06 

Open Tabs: 
  - HelloWorldClient.java
  - BinTree.java  [current tab]
  - BWindow.java
  
Path to file: Compression/PiedPiper/BinTree.java
"""


def _remove_from_parent(self, tr, path):
    parent = self._find(tr, path[:-1])
    del tr[parent[self.SUBDIRS][path[-1]].key()]

  def
