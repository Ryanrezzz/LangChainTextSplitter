from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

text =""" A common finding from survey data is that Gen Z — comprising young people between the ages of 13 and 28 — is disconnected from politics and disillusioned with democracy.1 Yet youth mobilization has been a primary feature of recent efforts to bring change and accountability to ineffective governments around the world. Just this year, a wave of “Gen-Z protests” has swept the globe from Indonesia to Kenya and Madagascar to Peru. The results have been mixed: Youth-led uprisings have toppled governments, compelled reforms, and provoked violent clashes and crackdowns. Some youth-led struggles, as in Serbia, are ongoing.

Today’s Gen-Z protest movements follow a longer-term trend: Protest movements are often powered by young people. One study finds that, between 1990 and 2020, 80 percent of nonviolent campaigns to topple incumbent national leaders or achieve self-determination featured substantial youth participation, with people under thirty estimated to comprise at least a quarter of frontline participants.2 The second People Power Movement in the Philippines that ousted Joseph Estrada from power in 2001, the Cedar Revolution that expelled Syrian forces from Lebanon in 2005, and the Sudanese uprising that led to Omar al-Bashir’s fall from power in 2019 are but a few examples of movements powered in large part by young peoples’ active frontline participation. While youth disillusionment with established modes of governing may be real, the potential power of youth mobilization to challenge entrenched power is equally evident.   """


splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)
url = "https://www.journalofdemocracy.org/articles/why-gen-z-is-rising/"

loader = WebBaseLoader(url)
docs= loader.load()

chunks= splitter.split_documents(docs)
# chunks = splitter.split_text(text)

print(chunks)
