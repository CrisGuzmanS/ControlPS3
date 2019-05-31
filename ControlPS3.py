# ===========
# DESCRIPCION
# ===========

# Configura los botones de un control de
# PlayStation 3 dependiendo del sistema
# operativo (Windows 10 o Linux/Ubuntu).

# ===========
# BIBLIOTECAS
# ===========

import pygame # FUNCIONALIDADES DEL CONTROL
import platform	# FUNCIONALIDADES DEL SISTEMA OPERATIVO

class ControlPS3:

	def __init__(self):

		# ========================
		# CONFIGURACION DE BOTONES
		# ========================

		if platform.system() == "Windows":
			self.buttons = {
				0:'Equis',
				1:'Circulo',
				2:'Cuadrado',
				3:'Triangulo',
				4:'L1',
				5:'R1',
				6:'Select',
				7:'Start',
				8:'Push analogo izquierdo',
				9:'Push analogo derecho'
			}

			self.analogs = {
				0:'LX',
				1:'LY',
				2:'RX',
				3:'RY'
			}

		elif platform.system() == 'Linux':
			self.buttons = {
				0:'Equis',
				1:'Circulo',
				2:'Triangulo',
				3:'Cuadrado',
				4:'L1',
				5:'R1',
				6:'L2', # NO EXISTE EN WINDOWS
				7:'R2', # NO EXISTE EN WINDOWS
				8:'Select',
				9:'Start',
				10:'Encendido', # NO EXISTE EN WINDOWS
				11:'Push analogo izquierdo',
				12:'Push analogo derecho'
			}

			self.analogs = {
				0:'LX',
				1:'LY',
				3:'RX',
				4:'RY'
			}

		# =========================
		# CONFIGURACION DEL CONTROL
		# =========================

		pygame.init()
		pygame.joystick.init()
		self.control = pygame.joystick.Joystick(0) # 0 representa el primer control conectado
		self.control.init()

	def get_buttons_dictionary(self):
		return self.buttons

	def get_analogs_dictionary(self):
		return self.analogs

	def tester(self):
		while True:
			# OBTENEMOS LOS BOTONES OPRIMIDOS
			events = pygame.event.get()
			for event in events:
				if event.type == pygame.JOYBUTTONDOWN:
					# BOTONES
					if self.control.get_button(0):
						print(self.buttons[0])
					if self.control.get_button(1):
						print(self.buttons[1])
					if self.control.get_button(2):
						print(self.buttons[2])
					if self.control.get_button(3):
						print(self.buttons[3])
					if self.control.get_button(4):
						print(self.buttons[4])
					if self.control.get_button(5):
						print(self.buttons[5])
					if self.control.get_button(6):
						print(self.buttons[6])
					if self.control.get_button(7):
						print(self.buttons[7])
					if self.control.get_button(8):
						print(self.buttons[8])
					if self.control.get_button(9):
						print(self.buttons[9])

				# JOYSTICK
				# if int(self.control.get_axis(0)*100) != 0:
				# 	print("izquierda x:",int(self.control.get_axis(0)*100))
				# if int(self.control.get_axis(1)*100) != 0:
				# 	print("izquierda y:",int(-self.control.get_axis(1)*100))
				# if int(self.control.get_axis(3)*100) != 0:
				# 	print("derecha x:",int(self.control.get_axis(3)*100))
				# if int(self.control.get_axis(4)*100) != 0:
				# 	print("derecha y:",int(-self.control.get_axis(4)*100))
