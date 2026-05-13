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
    process_before_response=True,
)

handler = SlackRequestHandler(app)


@app.event("app_mention")
def handle_metions(event, say):
    say("Kết nối thành công! Tôi đã nghe thấy bạn")


@app.message(re.compile(".*"))
def handle_all_messages(message, say, request):
    if request.headers.get("x-slack-retry-num"):
        return

    # user_id = message.get("user")
    text = message.get("text")

    print("DEBUG: PROCESSING TOPIC")
    topic = callLLM(
        text,
        topicSystemInstruction,
    )
    print(f"DEBUG: DONE PROCESSING TOPIC: {topic}")

    responseObj = fetchNewsContent(searchText=topic)
    if responseObj is None:
        say(f"Sorry, I couldn't find any news for: {topic}")
        return

    print("DEBUG: PROCESSING ARTICLES")
    articles = responseObj.results
    contents = []
    for i in range(len(articles)):
        content = fetchArticleContent(articles[i].link)
        contents.append(content)

    print("DEBUG: DONE PROCESSING ARTICLES")

    all_articles_text = "\n\n---\n\n".join(contents)
    message = f"User message:{text}\nTopic:{topic}\nContent:{all_articles_text}"

    print("DEBUG: PROCESSING GEMINI")
    summary = callLLM(message, newsSystemInstruction, "gemini")

    blocks = [
        {"type": "header", "text": {"type": "plain_text", "text": f"📊 Tóm tắt: {topic}"}},
        {"type": "divider"},
        {"type": "section", "text": {"type": "mrkdwn", "text": summary}},
        {"type": "divider"},
        {"type": "context", "elements": [{"type": "mrkdwn", "text": "🤖 _Cập nhật tự động bởi NewsBot_"}]}
    ]

    say(blocks=blocks, text=f"Summary for {topic}")
