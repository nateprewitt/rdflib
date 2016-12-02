"""
some more specific Literal tests are in test_literal.py
"""

import unittest
from rdflib.py3compat import format_doctest_out as uformat
from rdflib.term import URIRef, BNode, Literal
from rdflib.graph import QuotedGraph, Graph
from rdflib.namespace import XSD

class TestURIRefRepr(unittest.TestCase):
    """
    see also test_literal.TestRepr
    """
    
    def testSubclassNameAppearsInRepr(self):
        class MyURIRef(URIRef):
            pass
        x = MyURIRef('http://example.com/')
        self.assertEqual(repr(x), uformat("MyURIRef(%(u)s'http://example.com/')"))

    def testGracefulOrdering(self):
        u = URIRef('cake')
        g = Graph()
        a = u>u
        a = u>BNode()
        a = u>QuotedGraph(g.store, u)
        a = u>g


class TestBNodeRepr(unittest.TestCase):

    def testSubclassNameAppearsInRepr(self):
        class MyBNode(BNode):
            pass
        x = MyBNode()
        self.assert_(repr(x).startswith("MyBNode("))


class TestXSDToPythonTypes(unittest.TestCase):

    def test_base64_isnt_decoded(self):
        """
        ensure base64 values aren't decoded to avoid accidental data mangling.
        """
        b64msg = 'cmRmbGliIGlzIGNvb2whIGFsc28gaGVyZSdzIHNvbWUgYmluYXJ5IAAR83UC'
        lit = Literal(b64msg, datatype=XSD.base64Binary)
        self.assertEqual(lit.value, b64msg)
