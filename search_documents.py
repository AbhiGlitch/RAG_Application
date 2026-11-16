
from vector_store import collection
from embeddings import create_embedding


def search_documents(question):

    question_embedding = create_embedding(question)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )

    return results
