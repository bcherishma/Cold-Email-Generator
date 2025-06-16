import chromadb
client = chromadb.Client()
collection = client.create_collection(name="my_collection")

collection.add(
    documents=[
        "This doc is about New York City.",
        "This doc is about New delhi"
    ],
    ids = ["id1","id2"]
)

all_doc = collection.get()
print(all_doc)