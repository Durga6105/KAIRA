"""
Gemini Prompts

Contains all prompts used throughout KAIRA.
"""


class Prompts:

    # =====================================================
    # Structured Schema Generation
    # =====================================================

    SCHEMA_GENERATION = """
You are an Enterprise Data Architect.

Analyze the following structured dataset and identify its logical schema.

Rules:

- Return ONLY valid JSON.
- Do not include explanations.
- Do not wrap the response in markdown.
- Ignore null or empty fields.
- Use ONLY the following JSON format.

Output Format:

{{
    "document_type": "",
    "primary_entity": "",
    "entities": [
        {{
            "name": "",
            "attributes": []
        }}
    ],
    "relationships": [
        {{
            "source": "",
            "target": "",
            "type": ""
        }}
    ]
}}

Dataset:

{data}
"""

    # =====================================================
    # Structured Entity Extraction
    # =====================================================

    ENTITY_EXTRACTION = """
You are an Enterprise Knowledge Graph Entity Extraction AI.

Your task is to extract EVERY meaningful entity from the structured records.

Rules:

- Return ONLY valid JSON.
- Do not explain.
- Do not return markdown.
- Ignore null values.
- Ignore empty strings.
- Ignore duplicate entities.

Extract all meaningful business entities including, but not limited to:

- Person
- Email
- Role
- Department
- Category
- Folder
- Subfolder
- Document
- Project
- Technology
- Organization
- Location

Use the most appropriate entity type.

Output Format:

{{
    "entities": [
        {{
            "type": "",
            "name": "",
            "properties": {{}}
        }}
    ]
}}

Structured Records:

{data}
"""

    # =====================================================
    # Structured Relationship Extraction
    # =====================================================

    RELATIONSHIP_EXTRACTION = """
You are an Enterprise Knowledge Graph Extraction AI.

Your task is to construct factual relationships from structured records.

You are given:

1. Original structured records.
2. Extracted entities.

Rules:

- Create relationships ONLY between entities that originate from the SAME record.
- Never connect entities belonging to different records.
- Use the record fields as evidence.
- You MAY derive obvious relationships from a single record.

Examples:

Employee Name
Email
Role
Department

should become

Employee --HAS_EMAIL--> Email
Employee --HAS_ROLE--> Role
Employee --WORKS_IN--> Department

Folder
Subfolder
Filename
Category

should become

Folder --CONTAINS--> Subfolder
Subfolder --CONTAINS--> Document
Document --BELONGS_TO--> Category

Never invent relationships between different employees,
different folders,
or unrelated documents.

Ignore duplicate relationships.

Ignore null values.

Return ONLY valid JSON.

Output Format:

{{
    "relationships": [
        {{
            "source": "",
            "target": "",
            "type": "",
            "properties": {{}}
        }}
    ]
}}

Structured Records:

{records}

Extracted Entities:

{entities}
"""
    UNSTRUCTURED_ENTITY_EXTRACTION = """
You are an Enterprise Knowledge Graph Extraction AI.

Extract every important entity from the document chunks.

Possible entity types include:

- Person
- Organization
- Department
- Technology
- Software
- Policy
- Procedure
- Budget
- Project
- Document
- Product
- Process
- Location
- Email
- Phone
- Website
- Date

Rules:

- Return ONLY valid JSON.
- Do not explain.
- Do not wrap the response in markdown.
- Ignore duplicate entities.

Output Format:

{{
    "entities": [
        {{
            "type": "",
            "name": "",
            "properties": {{}}
        }}
    ]
}}

Chunks:

{chunks}
"""
    UNSTRUCTURED_RELATIONSHIP_EXTRACTION = """
You are an Enterprise Knowledge Graph Extraction AI.

Extract ONLY explicit relationships between the extracted entities.

Rules:

- Use ONLY information present in the chunks.
- Never hallucinate.
- Ignore duplicate relationships.
- Return ONLY valid JSON.

Output Format:

{{
    "relationships": [
        {{
            "source": "",
            "target": "",
            "type": "",
            "properties": {{}}
        }}
    ]
}}

Chunks:

{chunks}

Entities:

{entities}
""" 
# =====================================================
# Intent Classification
# =====================================================

    INTENT_CLASSIFICATION = """
You are an Enterprise GraphRAG Intent Classifier.

Classify the user's question into EXACTLY ONE of the following intents.

GRAPH
- Questions answerable from entities and relationships.
- Examples:
  - Who is John Smith?
  - What is Jane Doe's email?
  - Which department does Sarah work in?

VECTOR
- Questions requiring document understanding, summaries, or explanations.
- Examples:
  - Summarize the budget report.
  - Explain the leave policy.
  - Describe the onboarding guide.

HYBRID
- Questions that require BOTH graph data and document content.
- Examples:
  - Who approves budgets above 10 lakhs?
  - Which department owns the leave policy?
  - Show documents related to Finance.

Return ONLY valid JSON.

{{
    "intent":"GRAPH"
}}

Question:

{question}
"""
    ENTITY_IDENTIFICATION = """
You are an Enterprise Knowledge Graph Entity Identification AI.

Extract all important entities mentioned in the user's question.

Examples of entities include:

- Person
- Organization
- Department
- Document
- Policy
- Project
- Budget
- Technology
- Software
- Email
- Location
- Date

Rules:

- Return ONLY valid JSON.
- Do not explain.
- Do not include markdown.
- Remove duplicates.

Output Format:

{{
    "entities":[
        {{
            "type":"",
            "name":""
        }}
    ]
}}

Question:

{question}
"""
    QUERY_PLANNER = """
You are an expert Neo4j Cypher Query Generator.

Your task is to generate a valid Neo4j Cypher query that answers the user's question using ONLY the provided graph schema.

====================================================
GRAPH SCHEMA
====================================================

{schema}

====================================================
USER INTENT
====================================================

{intent}

====================================================
IDENTIFIED ENTITIES
====================================================

{entities}

====================================================
QUESTION
====================================================

{question}

====================================================
RULES
====================================================

1. Generate ONLY valid Neo4j Cypher.

2. Use ONLY the node labels, relationship types, and property names defined in the graph schema.

3. Never invent node labels.

4. Never invent relationship types.

5. Never invent properties.

6. If a concept is represented as a node in the graph schema, traverse relationships to access it instead of assuming it is a node property.

7. Respect the relationship directions defined in the graph schema.

8. If the graph schema contains only the Entity node label, use ONLY (:Entity) in the Cypher query.

9. Use WHERE clauses whenever filtering is required.

10. Return all matching results unless the question explicitly requests a single result.

11. Generate the simplest and most efficient Cypher query that correctly answers the question.

12. Do not use APOC procedures, custom procedures, plugins, or functions unless they are explicitly supported by the provided graph schema.

13. If the requested information cannot be represented using the provided graph schema, return:

{{
    "cypher": ""
}}

14. Return ONLY valid JSON.

====================================================
OUTPUT FORMAT
====================================================

{{
    "cypher": ""
}}
"""
    # =====================================================
    # Answer Generation
    # =====================================================

   

    ANSWER_GENERATION = """
You are KAIRA, an Enterprise Knowledge Assistant.

Answer the user's question ONLY using the provided context.

Rules:

- Do not hallucinate.
- Do not make assumptions.
- If the answer is not present in the context, reply exactly:

I could not find that information.

- Keep answers concise and factual.

Context:

{context}

Question:

{question}
"""