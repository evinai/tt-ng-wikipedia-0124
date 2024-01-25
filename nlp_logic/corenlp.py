from textblob import TextBlob
import wikipedia

def search_wikipedia(search_term):
    try:
        # Search for the given term on Wikipedia
        search_results = wikipedia.search(search_term)

        if search_results:
            # Get the summary of the first search result
            page_summary = wikipedia.summary(search_results)

            return page_summary
        else:
            return "No results found on Wikipedia."

    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation error
        return f"Disambiguation Error: {e.options}"

    except wikipedia.exceptions.PageError:
        # Handle page not found error
        return "Page not found on Wikipedia."