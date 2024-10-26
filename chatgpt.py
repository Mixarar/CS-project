from UnlimitedGPT import ChatGPT

session_token = "YOUR_SESSION_TOKEN"
conversation_id = "YOUR_CONVERSATION_ID"

chatbot = ChatGPT(
    session_token,
    conversation_id=conversation_id,
    proxy=None,
    chrome_args=None,
    disable_moderation=False,
    verbose=False,
)
