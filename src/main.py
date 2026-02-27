import src.hana_connection_and_query as db_query
import src.mailer as mailer

attachment_path = r"C:\Users\pliedtke_ext\OneDrive - Mutual\Escritorio\Pedidos Lucho\auto-mail\solicitudes_2025_plus.csv"
recipient = "Liedtke22@gmail.com"

email = mailer.build_mail(recipient, attachment_path)
mailer.send(email)

