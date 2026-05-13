from llm.agent import callLLM
from llm.system import topicSystemInstruction
from api.news import fetchNewsContent, fetchArticleContent

def testGetMessage(text):
    print("DEBUG: PROCESSING TOPIC")
    topic = callLLM(
        text,
        topicSystemInstruction,
    )
    print(f"DEBUG: DONE PROCESSING TOPIC: {topic}")

    responseObj = fetchNewsContent(searchText=topic)
    if responseObj is None:
        return

    print("DEBUG: PROCESSING ARTICLES")
    articles = responseObj.results
    contents = []
    for i in range(len(articles)):
        content = fetchArticleContent(articles[i].link)
        contents.append(content)

    print("contents:", len(contents))
    all_articles_text = "\n\n---\n\n".join(contents)
    # 2. Save as a normal text file
    temp_file_path = f"./articles_content_{topic}.txt" # Use .txt now
    
    with open(temp_file_path, "w", encoding="utf-8") as f:
        f.write(all_articles_text)