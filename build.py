import chromadb 

SEPARATOR = "-" * 70

# Initialize database (permanently)
client = chromadb.PersistentClient("./chroma_db")

# Chunk the documents
def load_chunks(filename):
    with open(filename) as f:
        text = f.read()

    sections = text.split(SEPARATOR)
    
    # Removing white space
    chunks = []
    for section in sections:
        chunks.append(section.strip())
    return chunks


chunks = load_chunks("roster_2026.txt")

files_and_collections = [
    ("roster_2026.txt",roster_2026),
    ("scouting_2027.txt",scouting_2027),
    ("opponents_2026.txt",opponents_2026)
]

