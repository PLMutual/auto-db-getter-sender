import win32com.client as win32

def build_mail(recipient_mail, attachment_path=None):
    outlook = win32.Dispatch('Outlook.Application')
    mail = outlook.CreateItem(0)
    
    # mail.To = "pliedtke_ext@mutual.cl"
    mail.To = recipient_mail
    mail.CC = "lrojasr@mutual.cl; pliedtke_ext@mutual.cl"
    mail.Subject = f"Test 3 Mail Automatico con adjunto"
    mail.Body = (
        "Estimadas, buenos días,\n\n"
        "Espero estén bien. Adjunto datos de las Órdenes Médicas de 2025 en adelante.\n\n"
        "Saludos."
    )

    if attachment_path:
        # mail.Attachments.Add("solicitudes_2025_plus.csv")
        mail.Attachments.Add(attachment_path)
    
    return mail

def send(mail):
    print("Sending Mail")
    mail.Send()
    print("Sent")

if __name__ == "__main__":
    attachment_path = r"C:\Users\pliedtke_ext\OneDrive - Mutual\Escritorio\Pedidos Lucho\auto-mail\solicitudes_2025_plus.csv"
    recipient = "Liedtke22@gmail.com"

    email = build_mail(recipient, attachment_path)
    send(email)

    print(f"Archivo enviado: {attachment_path}")