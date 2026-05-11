import os
import re
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler
from llm.agent import callLLM
from llm.system import topicSystemInstruction, newsSystemInstruction
from api.news import fetchNewsContent, fetchArticleContent

app = App(
    token=os.getenv("SLACK_BOT_TOKEN"),
    signing_secret=os.getenv("SLACK_SIGNING_KEY"),
)

handler = SlackRequestHandler(app)


@app.event("app_mention")
def handle_metions(event, say):
    say("Kết nối thành công! Tôi đã nghe thấy bạn")


@app.message(re.compile(".*"))
def handle_all_messages(message, say):
    # user_id = message.get("user")
    text = message.get("text")

    topic = callLLM(
        text,
        topicSystemInstruction,
    )

    responseObj = fetchNewsContent(searchText=topic)
    if responseObj is None:
        say(f"Sorry, I couldn't find any news for: {topic}")
        return

    articles = responseObj.results
    contents = []
    for i in range(len(articles)):
        content = fetchArticleContent(articles[i].link)
        contents.append(content)

    print("contents:",contents)
    all_articles_text = "\n\n---\n\n".join(contents)
    summary = callLLM(all_articles_text, newsSystemInstruction, "gemini")

    say(f"Topic: {topic}\n{summary}")
