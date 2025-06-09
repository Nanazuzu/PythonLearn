def mask_email(email: str) -> str:
  splited = email.split('@')
  mid = []
  for index in range(len(splited[0])):
    if index % 2 == 1:
      mid.append('*')
    else:
      mid.append(splited[0][index])
  return ''.join(mid) + '@' + splited[1]

#IT MAKE EASIER WITH THIS
# def mask_email(email: str) -> str:
#     user, domain = email.split('@')
#     masked_user = ''.join([c if i % 2 == 0 else '*' for i, c in enumerate(user)])
#     return masked_user + '@' + domain

print(mask_email("myemailaddress@company.com"))
print(mask_email("abcde@hello.com"))
print(mask_email("x@domain.net"))