import arxiv

def search_arxiv(query : str , is_topic : bool):

    client = arxiv.Client()


    if is_topic:
        search = arxiv.Search(
            query=query,
            max_results=1,
            sort_by=arxiv.SortCriterion.Relevance
        )
    else:
        search = arxiv.Search(id_list=[query])


    results = list(client.results(search))

    if not results:
        return None

    return results[0]