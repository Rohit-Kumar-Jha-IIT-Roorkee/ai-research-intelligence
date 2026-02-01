import chromadb
from chromadb.utils import embedding_functions

class VectorDBManager:
    def __init__(self, db_path="data_intelligence/vector_db"):
        """
        Initializes the Vector DB in the designated folder [cite: 2471-2473].
        This folder acts as the 'Hard Drive' for indexed consumer intelligence.
        """
        self.client = chromadb.PersistentClient(path=db_path)
        
        # Using a standard embedding function for B2C verbatims and pain language [cite: 61-62]
        self.emb_fn = embedding_functions.DefaultEmbeddingFunction()
        
        # 'research_data' is the canonical collection for all 7 goals [cite: 1282-1288]
        self.collection = self.client.get_or_create_collection(
            name="research_data", 
            embedding_function=self.emb_fn
        )

    def add_evidence(self, text_list, metadata_list, ids):
        """
        Stores transcripts and verbatims with mandatory metadata tagging [cite: 60-62].
        Supports segmentation by attaching 'respondent' and 'segment' tags [cite: 98-106].
        """
        self.collection.add(
            documents=text_list,
            metadatas=metadata_list,
            ids=ids
        )

    def query_evidence(self, user_query, n_results=3):
        """
        Retrieves grounded evidence based on semantic similarity [cite: 65-73].
        Used to find 'Quotes that explain problems clearly' for the Synthesis Engine[cite: 379, 1192].
        Returns raw results (quotes and metadata) to ensure Person 2 remains an evidence provider.
        """
        results = self.collection.query(
            query_texts=[user_query],
            n_results=n_results
        )
        return results

    def query_by_segment(self, user_query, segment_name, n_results=3):
        """
        Filters evidence by specific user segments (e.g., 'Gen Z' or 'Power Users') [cite: 107-116, 301-305].
        Ensures research is journey-aware and platform-aware [cite: 402-403].
        """
        results = self.collection.query(
            query_texts=[user_query],
            where={"segment": segment_name},
            n_results=n_results
        )
        return results

    def delete_research_collection(self):
        """
        Utility for demo safety and resetting research data between goals[cite: 2428, 2441].
        """
        self.client.delete_collection(name="research_data")
        self.collection = self.client.get_or_create_collection(
            name="research_data", 
            embedding_function=self.emb_fn
        )