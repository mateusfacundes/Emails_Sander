from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pandas as pd

server = smtplib.SMTP_SSL('*sERVIDOR_DE_EMAIL*', 465)
server.login("*EMAIL*", "*SENHA*")

tabela = pd.read_csv("lista_emails.csv", sep=",")

i = 0

while i < len(tabela):
	msg = MIMEMultipart()
	msg['Subject'] = "Example"
	msg['From'] = "*EMAIL_REMETENTE*"
	msg['To'] = tabela['emails'][i]

	html = """\
	<html>
	  <head><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous"></head>
	  <body>
		<div class="container">
		  	<div class="container" style="background-color: #e9e9e9; width: 650px; height: auto;">
			  		<div class="div" style="padding-top: 20px;">
			  			<center><h1>Bem vindo ao EAD da The Forense!</h1></center>
			  		</div>
			  		<br>
					<div class="container">
						<div class="div" style=" margin-top: 30px;">
							<h3>Faça seu login para redefinir sua senha padrão</h3>
						</div>
						<div>
							<br>
							<h4>Usuário : <span style="color: #053d75">%s</span></h4>
							<h4>Senha : <span style="color: #053d75">theforense2022</span></h4>
							<br>
							
							<br>
							<br>
							<div style="padding-left: 30px; padding-bottom: 30px; color: #4282C2;">

								<h6 style="color: black;"> 
										Contatos:
								</h5>
								<h6 > 
								
								</h5>
								<h6 > 
										
								</h5>
							</div>
						</div>
					</div>
				</div>
			</div>

		<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
		<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
		<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
		
	  </body>
	</html>
	""" % msg['To']

	body = MIMEText(html, 'html')
	msg.attach(body)

	server.sendmail(msg['From'], msg['To'], msg.as_string())
	print("emails enviado para: ", str(msg['To']))
	i += 1

server.quit()
