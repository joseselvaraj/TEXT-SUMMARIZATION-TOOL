from transformers import pipeline
import textwrap

def summarize_article(article_text, max_length=150, min_length=40):
    summarizer = pipeline("summarization")
    summary = summarizer(article_text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

def main():
    article = """
    Artificial Intelligence (AI) has made tremendous strides in the past decade. From facial recognition
    to self-driving cars, AI is becoming increasingly prevalent in our daily lives. One of the most
    promising areas of AI is Natural Language Processing (NLP), which enables machines to understand,
    interpret, and generate human language. Applications of NLP range from chatbots and language
    translators to voice assistants and content summarization. The field is evolving rapidly, and new
    models like GPT, BERT, and T5 have significantly advanced the state of the art. Despite these
    advancements, challenges such as bias, ethical concerns, and data privacy remain critical issues
    that need to be addressed to ensure AI's responsible and fair use in society.
    """

    print("\nOriginal Article:\n")
    print(textwrap.fill(article, width=100))

    summary = summarize_article(article)

    print("\n\nSummarized Text:\n")
    print(textwrap.fill(summary, width=100))

if __name__ == "__main__":
    main()
