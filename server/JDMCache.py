#!/usr/bin/env python
from neo4j import GraphDatabase

from Node import Node

class JDMCache:
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:11003", auth=("basil", "password"))

    def close(self):
        if self.driver is not None:
            self.driver.close()

    def query(self, query):
        session = None
        response = None

        try:
            session = self.driver.session()
            response = list(session.run(query))
        except Exception as e:
            print(e)
            print("Cache retrieve : failed")
        finally:
            if session is not None:
                session.close()
        return response

    def insertDefinition(self, query, definition):
        definition = repr(definition)[1:-1]
        find_node_origin = "MERGE (t:Term { name : '" + query.term + "'})"
        find_node_definition = "MERGE (d:Definition { content :  \"" + definition + "\"})"

        self.query(find_node_origin + " " + find_node_definition + " MERGE (t) -[:DEFINITION]-> (d)")

    def insertRefinements(self, query, refinements):
        self.insertTerms(query, refinements, "REFINEMENT")

    def insertDomainTerms(self, query, domain_terms):
        self.insertTerms(query, domain_terms, "DOMAIN")

    def insertAssociations(self, query, associations):
        self.insertTerms(query, associations, "ASSOCIATION")

    def findDefinitions(self, term):
        query = "MATCH(n:Term {name : '" + term + "' })-[:DEFINITION]->(d:Definition) RETURN d.content"
        query += " UNION ALL"
        query += " MATCH (n:Term {name : '" + term + "' })-[:REFINEMENT*]->(m : Term)-[:DEFINITION]->(d:Definition) RETURN d.content"

        return [ record.get('d.content') for record in self.query(query) ]

    def findDomainTerms(self, term):
        return self.findRelatedTerms(term, "DOMAIN")

    def findAssociations(self, term):
        return self.findRelatedTerms(term, "ASSOCIATION")

    def insertTerms(self, query, terms, relationLabel):
        if not terms:
            return

        find_node_origin = "MERGE (o:Term { name : '" + query.term + "'})"
        nodeToCreate = []

        for term in terms:
            find_node_dest = "MERGE (d:Term { name : '" + term.name + "'})"
            create_relation = " MERGE (o) -[:" + relationLabel + "]-> (d)"
            set_node_id = " SET o.nodeId = " + str(term.nodeId)
            set_node_type = " SET o.nodeType = " + str(term.nodeType)
            set_weight = " SET o.weight = " + str(term.weight)
            set_formatted_name = " SET o.formattedName = " + str(term.formattedName)
            set_is_refinement = " SET o.isRefinement = " + str(term.isRefinement)

            query = find_node_origin + find_node_dest + create_relation
            query += set_node_id + set_node_type + set_weight + set_is_refinement

            if term.isRefinement:
                query += set_is_refinement

            self.query(query)


    def findRelatedTerms(self, term, relationLabel):
        query = "MATCH(n:Term {name : '" + term + "'})-[:" + relationLabel + "]->(m:Term) RETURN m.name"

        result = []

        for record in self.query(query):
            result.append(Node(0, record.get('m.name'), 1, 0, None, False))

        return result
