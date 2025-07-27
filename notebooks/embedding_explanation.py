import spacy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def demonstrate_embeddings():
    print("=== WORD EMBEDDINGS EXPLANATION ===\n")
    
    # 1. Basic embedding extraction
    print("1. BASIC EMBEDDING EXTRACTION:")
    word = "king"
    vector = nlp(word).vector
    print(f"Word: '{word}'")
    print(f"Vector shape: {vector.shape}")
    print(f"First 10 values: {vector[:10]}")
    print(f"Vector magnitude: {np.linalg.norm(vector):.4f}\n")
    
    # 2. Similarity between words
    print("2. WORD SIMILARITY:")
    words = ["king", "queen", "man", "woman", "apple", "computer"]
    vectors = [nlp(w).vector for w in words]
    
    # Calculate similarities
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words[i+1:], i+1):
            similarity = cosine_similarity([vectors[i]], [vectors[j]])[0][0]
            print(f"'{word1}' vs '{word2}': {similarity:.4f}")
    print()
    
    # 3. Famous word analogy: king - man + woman ≈ queen
    print("3. WORD ANALOGY (king - man + woman ≈ queen):")
    king_vec = nlp("king").vector
    man_vec = nlp("man").vector
    woman_vec = nlp("woman").vector
    
    # Calculate: king - man + woman
    analogy_result = king_vec - man_vec + woman_vec
    
    # Find the closest word to this result
    queen_vec = nlp("queen").vector
    similarity = cosine_similarity([analogy_result], [queen_vec])[0][0]
    print(f"Similarity between (king - man + woman) and 'queen': {similarity:.4f}")
    print("This shows that the embedding space preserves semantic relationships!\n")
    
    # 4. Context matters
    print("4. CONTEXT EXAMPLES:")
    context_words = {
        "bank": ["river", "money", "financial"],
        "python": ["snake", "programming", "code"],
        "apple": ["fruit", "company", "technology"]
    }
    
    for word, related_words in context_words.items():
        print(f"'{word}' similarities:")
        word_vec = nlp(word).vector
        for related in related_words:
            related_vec = nlp(related).vector
            similarity = cosine_similarity([word_vec], [related_vec])[0][0]
            print(f"  - '{related}': {similarity:.4f}")
        print()

def visualize_embeddings():
    """Visualize word embeddings in 2D space"""
    print("5. VISUALIZATION:")
    
    # Categories of words
    categories = {
        "Animals": ["cat", "dog", "bird", "fish", "lion"],
        "Colors": ["red", "blue", "green", "yellow", "black"],
        "Numbers": ["one", "two", "three", "four", "five"],
        "Emotions": ["happy", "sad", "angry", "excited", "calm"]
    }
    
    all_words = []
    all_vectors = []
    colors = []
    
    for i, (category, words) in enumerate(categories.items()):
        for word in words:
            all_words.append(word)
            all_vectors.append(nlp(word).vector)
            colors.append(i)
    
    # Reduce to 2D for visualization
    pca = PCA(n_components=2)
    vectors_2d = pca.fit_transform(all_vectors)
    
    # Plot
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(vectors_2d[:, 0], vectors_2d[:, 1], c=colors, cmap='tab10', s=100)
    
    # Add labels
    for i, word in enumerate(all_words):
        plt.annotate(word, (vectors_2d[i, 0], vectors_2d[i, 1]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=10)
    
    plt.title('Word Embeddings Visualization (PCA)')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend(handles=scatter.legend_elements()[0], 
              labels=list(categories.keys()), title="Categories")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    demonstrate_embeddings()
    visualize_embeddings() 