import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="students"
)


def add_student_to_vector_db(student):
    student_text = (
        f"Name: {student.name}, "
        f"Course: {student.course}, "
        f"Year: {student.year}"
    )

    collection.upsert(
        ids=[str(student.id)],
        documents=[student_text],
        metadatas=[
            {
                "student_id": student.id,
                "name": student.name,
                "course": student.course,
                "year": student.year,
            }
        ],
    )


def search_vector_db(query: str):
    return collection.query(
        query_texts=[query],
        n_results=3,
    include=["documents","metadatas"]
    )