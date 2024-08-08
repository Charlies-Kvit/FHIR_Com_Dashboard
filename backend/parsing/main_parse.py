import zulip
from openai import OpenAI
from config.config import API_KEY_AI


def parse(emails):
    if len(emails) == 1:
        core = True
    else:
        core = False
    client = zulip.Client(config_file="config/zuliprc")
    AI = OpenAI(api_key=API_KEY_AI, base_url="https://api.perplexity.ai")
    result = {}
    for email in emails:
        result[email] = []
        request = {
            "anchor": "newest",
            "num_before": 100,
            "num_after": 0,
            "narrow": [
                {"operator": "sender", "operand": email},
                {"operator": "channels", "operand": "public"}
            ],
        }
        answer = client.get_messages(request)
        if "messages" not in answer:
            continue
        stream_id_do = []
        data = {}
        for message in answer["messages"]:
            stream_id = message["stream_id"]
            if stream_id in stream_id_do:
                continue
            count = get_post_count(answer["messages"], stream_id)
            stream_id_do.append(stream_id)
            data[stream_id] = count
        sorted_answer = sorted(data.items(), key=lambda item: item[1], reverse=True)
        for el in sorted_answer[:5]:
            stream_id = el[0]
            subject = ""
            display_recipient = ""
            timestamp = 0
            for message in answer["messages"]:
                if message["stream_id"] == stream_id:
                    core_name = message["sender_full_name"]
                    subject = message["subject"]
                    display_recipient = message["display_recipient"]
                    timestamp = message["timestamp"]
                    break
            url = get_url(display_recipient.lower(), subject, stream_id)
            if core:
                text = f"""Read the thread {url}
                        I need to get a summary of what people discuss in that thread. 
                        I need to get a summary of what {core_name} posted into this thread
                        I need to get a result like:
                        Topic summary - 300-500 characters
                        {core_name} posts summary - 300-500 characters
                        3-5 pieces of advice by other interlocutors. For every advice I want to see author. 
                        For every advice and {core_name} summary mark the names like Author: author name"""
            else:
                text = f"""Read the thread {url}
                        I need to get a summary of what people discuss in that thread. 
                        I need to get a result like:
                        Topic summary - 300-500 characters
                        3-5 pieces of advice by other interlocutors. For every advice I want to see author. 
                        For every advice summary mark the names like Author: author name"""
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are an artificial intelligence assistant and you need to "
                        "engage in a helpful, detailed, polite conversation with a user."
                    ),
                },
                {
                    "role": "user",
                    "content": text,
                },
            ]
            response = AI.chat.completions.create(model="llama-3-sonar-small-32k-online", messages=messages)
            result[email].append({
                "text": response.choices[0].message.content,
                "timestamp": timestamp,
                "count": el[1],
                "url": url,
                "title": subject
            })
            if len(result[email]) == 5:
                break
    return result


def get_post_count(messages, stream_id):
    count = 0
    for message in messages:
        if message["stream_id"] == stream_id:
            count += 1
    return count


def get_url(display_recipient, title, stream_id):
    syms = ["_", "-", ".", "~"]
    for el in display_recipient:
        if not el.isalpha() and el not in syms and not el.isdigit():
            display_recipient = display_recipient.replace(el, "." + hex(ord(el))[2:].upper())
    display_recipient = display_recipient.replace(".20", "-")
    for el in title:
        if not el.isalpha() and el not in syms and not el.isdigit():
            title = title.replace(el, "." + hex(ord(el))[2:].upper())
    url = f"https://chat.fhir.org/#narrow/stream/{stream_id}-{display_recipient}/topic/{title}"
    return url


def main(emails):
    result = parse(emails)
    return result
    # "sh@gefyra.de"
