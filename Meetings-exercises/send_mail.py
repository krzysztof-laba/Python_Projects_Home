import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'klaba1@ra.rockwell.com'
mail.Subject = 'Python!'
mail.Body = 'Python rlz :)'
#mail.HTMLBody = '<h2>HTML Message body</h2>'
#attachment  = "Path to the attachment"
mail.Attachments.Add(r"C:\Users\pstopa\PycharmProjects\test\send_mail.py")

mail.Send()