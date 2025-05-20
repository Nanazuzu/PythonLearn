def is_spam_email(email_body: str, spam_keywords: list[str]) -> bool:
  email = email_body.lower()
  keyword = [k.lower() for k in spam_keywords]
  for index in keyword:
    if index in email:
      return True
  return False

print(is_spam_email("Limited time offer! Buy now!", ["buy now", "limited offer"]))
print(is_spam_email("Hello, how are you?", ["buy now", "limited offer"]))
print(is_spam_email("Congratulations, you have won a prize!", ["prize", "lottery", "winner"]))