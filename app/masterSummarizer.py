import sparknoteScraper
import wiki_summary
import summarizer
import sys
import os


def getSummary(bookTitle, sentences_count):
    summary_of_summary = ""
    sparknotes_failed = False
    try:
        summary_of_summary = sparknoteScraper.getSummary(bookTitle, sentences_count)
    except BaseException as e:
        print e
        sparknotes_failed = True
    if summary_of_summary == "":
        sparknotes_failed = True
    if sparknotes_failed:
        try:
            filePath = "Summary.txt"
            summary = wiki_summary.wiki_summary(bookTitle)
            with open(filePath, "w") as text_file:
                text_file.write(summary)
            summary_of_summary = summarizer.getSummaryFromFile(filePath, sentences_count)
            os.remove(filePath)

        except BaseException as e:
            print e
            summary_of_summary = ""

    return summary_of_summary

if __name__ == "__main__":
    book_title = str(raw_input("What's your favorite book?"))
    sentences_count = 2
    print(getSummary(book_title, sentences_count)).encode(sys.stdout.encoding, errors='replace')
