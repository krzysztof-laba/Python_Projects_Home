from lerning.Meetings import Protection

print("Moje hasło:",Protection.password)
print("")
print("Pierwszy sposób importowania z innej lokacji:")
print("Zakodowane:",Protection.password_encode)
print("Odkodowane:",Protection.password_decode)
print("")
print("Drugi sposób:")
password_encode = Protection.password_encode
password_decode = Protection.password_decode
print("Zakodowane:",password_encode)
print("Odkodowane:",password_decode)