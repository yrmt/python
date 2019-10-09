import copy

# 原型
mail_mode = {
    'tittle': '垃圾邮件',
    'body': '这是垃圾邮件',
    'sendFor': 'laji@mail.com',
    'sendEr': '@'
}

mail_mode_copy = copy.deepcopy(mail_mode)
mail_mode_copy['sendEr'] = 'laji01@mail.com'
print("原模板", mail_mode)
print("发送报文", mail_mode_copy)
