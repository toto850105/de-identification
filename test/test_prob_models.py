from django.test import TestCase

from common.data_utilities import DataUtils
from prob_models.dep_graph import DependencyGraph
from prob_models.jtree import JunctionTree

import common.constant as c

TESTING_FILE = c.TEST_DATA_PATH

"""
The test file has for fields, and the dependency graph would be a complete graph.
The junction Tree has only one clique

"""
class DependencyGraphTests(TestCase):

	def setUp(self):
		self.data = DataUtils(TESTING_FILE)

	def test_dep_graph_edges_length_is_6(self):
		"""
		Test the Dependency graph computation
		"""
		dep_graph = DependencyGraph(self.data)
		edges = dep_graph.get_dep_edges(display = True)
		#print self.data.get_domain()
		self.assertEqual(len(edges) == 3, True)

class JunctionTreeTests(TestCase):

	def setUp(self):
		self.data = DataUtils(TESTING_FILE)
		self.dep_graph = DependencyGraph(self.data)
		self.edges = self.dep_graph.get_dep_edges(display=True)
		self.nodes = self.data.get_nodes_name()
		self.jtree_path = c.TEST_JTREE_FILE_PATH

	def test_build_jtree_then_check_jtree_file(self):
		self.TestA()
		self.TestB()

	def TestA(self):
		"""
		The dependency graph is a complete graph, 
		so there is only one clique in the junction tree
		"""
		jtree = JunctionTree(self.edges, self.nodes, self.jtree_path)
		jtreepy = jtree.get_jtree()
		#print jtreepy
		self.assertEqual(len(jtreepy) == 3, True)

	def TestB(self):
		import os, time
		from stat import *
		st = os.stat(self.jtree_path)
		now = time.time()
		self.assertEqual((st.st_mtime - now) < 50000, True)