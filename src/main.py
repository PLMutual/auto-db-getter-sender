import src.mailer as mailer

attachment_path = r"C:\Users\pliedtke_ext\OneDrive - Mutual\GPCCDG - Equipo Planificación estratégica y Proyectos\11 Salud\Centro Coordinador Quirúrgico (CCQ)\02 Ordenes Clínicas\Ordenes Clínicas de Pabellón Ley.xlsx"
recipient = "Liedtke22@gmail.com"

email = mailer.build_mail(recipient, attachment_path)
mailer.send(email)

