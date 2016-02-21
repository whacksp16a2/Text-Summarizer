import sparknoteScraper
import wiki_summary
import summarizer

def getSummary(bookTitle, sentences_count):
    try:
        summary_of_summary = sparknoteScraper.getSummary(bookTitle, sentences_count)
    except:
        try:
            filePath = "Summary.txt"
            summary = wiki_summary.wiki_summary(bookTitle)
            with open(filePath, "w") as text_file:
                text_file.write(summary)
            summary_of_summary = summarizer.getSummaryFromFile(filePath, sentences_count)
        except:
            summary_of_summary = ""

    return summary_of_summary

if __name__ == "__main__":
    book_title = str(raw_input("What's your favorite book?"))
    sentences_count = 2
    print(getSummary(book_title, sentences_count))
