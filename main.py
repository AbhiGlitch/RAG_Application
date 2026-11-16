
from search_documents import search_documents
from generate_answer import generate_answer


question = input("Ask your question: ")

results = search_documents(question)

for i, document in enumerate(results["documents"][0]):

    print(f"\nPage: {results['metadatas'][0][i]['page']}")
    print(document)


if results["distances"][0][0] > 0.8:

    print("\nFinal RAG Answer:")
    print("I don't know based on the provided document.")

else:

    context = "\n\n".join(results["documents"][0])

    answer = generate_answer(question, context)

    print("\nFinal RAG Answer:")
    print(answer)
