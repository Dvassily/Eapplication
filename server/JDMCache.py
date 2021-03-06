#!/usr/bin/env python
from neo4j import GraphDatabase

from Node import Node
import csv

class JDMCache:
    def __init__(self):
        with open('dbconnection.txt', 'r') as reader:
            connectionArray = list(csv.reader(reader.read().split('\n'), delimiter=';'))[1]
            self.driver = GraphDatabase.driver(connectionArray[0] + ':' + connectionArray[1], auth=(connectionArray[2], connectionArray[3]))

    def close(self):
        if self.driver is not None:
            self.driver.close()

    def insert(self, query, response, main_query=False):
        session = None

        try:
            session = self.driver.session()
            tx = session.begin_transaction()

            self.insertDefinition(query, response.definition, tx)
            self.insertRefinements(query, response.getRefinements(), tx)

            if main_query:
                self.insertDomainTerms(query, response.getDomainTerms(), tx)
                self.insertAssociations(query, response.getAssociations(), tx)
                self.inserParts(query, response.getParts(), tx)
                self.insertSynonyms(query, response.getSynonyms(), tx)
                self.insertAntonyms(query, response.getAntonyms(), tx)

            tx.commit()
        except Exception as e:
            print(e)
            print("Cache insertion : failed")
        finally:
            if session is not None:
                session.close()
        return response


    
    def insertDefinition(self, query, definition, tx):
        definition = repr(definition)[1:-1]
        find_node_origin = "MERGE (t:Term { name : '" + query.term + "'})"
        find_node_definition = "MERGE (d:Definition { content :  \"" + definition + "\"})"

        tx.run(find_node_origin + " " + find_node_definition + " MERGE (t) -[:DEFINITION]-> (d)")

    def insertRefinements(self, query, refinements, tx):
        self.insertTerms(query, refinements, "REFINEMENT", tx)

    def insertDomainTerms(self, query, domain_terms, tx):
        self.insertTerms(query, domain_terms, "DOMAIN", tx)

    def insertAssociations(self, query, associations, tx):
        self.insertTerms(query, associations, "ASSOCIATION", tx)

    def inserParts(self, query, parts, tx):
        self.insertTerms(query, parts, "PART_OF", tx)

    def insertSynonyms(self, query, synonyms, tx):
        self.insertTerms(query, synonyms, "SYNONYM_OF", tx)

    def insertAntonyms(self, query, antonyms, tx):
        self.insertTerms(query, antonyms, "ANTONYM_OF", tx)

    def insertTerms(self, query, terms, relationLabel, tx):
        if not terms:
            return

        find_node_origin = "MERGE (o:Term { name : '" + query.term + "'})"
        nodeToCreate = []

        for term in terms:
            find_node_dest = "MERGE (d:Term { name : '" + term.name + "'})"
            create_relation = " MERGE (o) -[:" + relationLabel + "]-> (d)"
            set_node_id = " SET d.nodeId = " + str(term.nodeId)
            set_node_type = " SET d.nodeType = " + str(term.nodeType)
            set_weight = " SET d.weight = " + str(term.weight)
            set_formatted_name = " SET d.formattedName = " + str(term.formattedName)
            set_is_refinement = " SET d.isRefinement = " + str(term.isRefinement)
            query = find_node_origin + find_node_dest + create_relation
            query += set_node_id + set_node_type + set_weight + set_formatted_name + set_is_refinement

            if term.isRefinement:
                query += set_is_refinement

            tx.run(query)

    def findDefinitions(self, term):
        query = "MATCH(n:Term {name : '" + term + "' })-[:DEFINITION]->(d:Definition) RETURN d.content"
        query += " UNION ALL"
        query += " MATCH (n:Term {name : '" + term + "' })-[:REFINEMENT*]->(m : Term)-[:DEFINITION]->(d:Definition) RETURN d.content"

        return [ record.get('d.content') for record in self.query(query) ]

    def findDomainTerms(self, term):
        return self.findRelatedTerms(term, "DOMAIN")

    def findAssociations(self, term):
        return self.findRelatedTerms(term, "ASSOCIATION")

    def findParts(self, term):
        return self.findRelatedTerms(term, "PART_OF")

    def findSynonyms(self, term):
        return self.findRelatedTerms(term, "SYNONYM_OF")

    def findAntonyms(self, term):
        return self.findRelatedTerms(term, "ANTONYM_OF")


    def findRelatedTerms(self, term, relationLabel):
        query = "MATCH(n:Term {name : '" + term + "'})-[:" + relationLabel + "]->(m:Term) RETURN m.nodeId, m.name, m.nodeType, m.weight, m.formattedName, m.isRefinement"

        result = []

        for record in self.query(query):
            result.append(Node(record.get('m.nodeId'), record.get('m.name'), record.get('m.nodeType'), record.get('m.weight'), record.get('m.formattedName'), record.get('m.isRefinement')))

        return result

    def query(self, query, insertion=False):
        session = None
        response = None

        try:
            session = self.driver.session()
            response = list(session.run(query))
        except Exception as e:
            print(e)
            print("Cache " + ("insertion" if insertion else "retrieve") + " : failed")
        finally:
            if session is not None:
                session.close()
        return response
