import pandas as pd
df = pd.read_csv('portfolio.csv')
import chromadb

client = chromadb.PersistentClient('vectorstore')
collection = get_or_create_collection(name='portfolio')

if not collection.count():
    for _,row in df.iterrows():
        collection.add(documents=row["Techstack"],
                       metadata={"links":row["Links"]},
                       ids=[str(uuid.uuid4())])