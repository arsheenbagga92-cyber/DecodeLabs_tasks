from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# List of available courses
courses = [
    "Python Programming",
    "Machine Learning",
    "Artificial Intelligence",
    "Web Development",
    "Data Science",
    "Cyber Security",
    "Cloud Computing",
    "Java Programming",
    "Deep Learning",
    "SQL Database"
]

print("      AI COURSE RECOMMENDATION SYSTEM")

user_input = input("\nEnter your interests (comma separated): ")

documents = courses + [user_input]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

similarity = cosine_similarity(
    tfidf_matrix[-1],
    tfidf_matrix[:-1]
)
scores = similarity.flatten()

recommendations = list(zip(courses, scores))

recommendations = sorted(
    recommendations,
    key=lambda x: x[1],
    reverse=True
)

print("\nTop Course Recommendations\n")

for i, (course, score) in enumerate(recommendations[:5], start=1):
    print(f"{i}. {course}")
    print(f"   Similarity Score: {score:.2f}\n")