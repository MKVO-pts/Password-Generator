import random
import kivy 
import time
import numpy as np
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton

#variables
num = ["1","2","3","4","5","6","7","8","9"]
min_leters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
max_leters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
all_simbolos = ["!","%","$",'?','.','"','+','*','^','º',"#","<","@",';','-','_','%']
arr_num = np.array(num)
arr_max = np.array(max_leters)
arr_min = np.array(min_leters)
arr_sim = np.array(all_simbolos)

def randomize(num_of_times):
    global password
    password = ""
    for x in range(num_of_times):
        password = password + random.choice(lista)
        if x == range(num_of_times):
            return password
            break

def password_creator(self, num_entry):
    global lista
    lista = np.array((0),ndmin= 1)

    letras_maiusculas = self.ids.letras_maiusculas.state   #verifica o estado dos botoes
    letras_minusculas = self.ids.letras_minusculas.state   #verifica o estado dos botoes
    simbolos = self.ids.simbolos.state                     #verifica o estado dos botoes
    numeros = self.ids.numeros.state                       #verifica o estado dos botoes

    if letras_maiusculas == "normal":
        lista = np.concatenate([lista, arr_max])
    if letras_minusculas == "normal":
    	lista =  np.concatenate([lista, arr_min])
    if numeros == "normal":
        lista = np.concatenate([lista,arr_num])
    if simbolos == "normal":
        lista = np.concatenate([lista, arr_sim])
    lista = np.array(lista)
    randomize(num_entry)

class GenGridLayout(GridLayout): #main class
    passwords_final = "[color=#000000]None[/color]"

    def verify(self): #will be called when te button is press
        global passwords_final

        final_list= [] 
        len_pass = self.ids.num_letras.text
        number_pass = self.ids.num_passwords.text
        try:
            number_pass = int(number_pass)
            len_pass = int(len_pass)

            if type(number_pass) == int and type(len_pass) == int:
                pass
            else:
                raise EOFError # it will raise a error, so the popup open
        except: #will open a popup, it will close after a click
            print("Popup open")
            ex = Popup(title='Input error',content=Label(text='TypeError:       The numbers you choose \"{num}, {nums}\" are invalid'.format(num=self.ids.num_letras.text, nums=self.ids.num_passwords.text)), size_hint=(None,None), size=(410,175),auto_dismiss= True)
            ex.open()
        else: #it means nothing went bad
            #funcao para criar passwords
            fim = ""
            for x in range(number_pass):
                password_creator(num_entry = len_pass, self=self)
                final_list.append(password)
                fim = fim + str(final_list[x]) + "\n"
                print(len(final_list))
                print(fim)
                self.ids.output.text = fim

 
class PasswordGenApp(App):
    def build(self):
        return GenGridLayout()
gl = PasswordGenApp()
gl.run()