import pyautogui as pyauto
import pyautogui as tempoEspera

#Tempo de espera para que o computador possa processar informações
tempoEspera.sleep(1)


#movendo mouse até o botão win e clicando
tempoEspera.sleep(1)
pyauto.click(x=27, y=1061)
tempoEspera.sleep(1)

#Escrevendo league e abrindo ele
pyauto.typewrite('league')
tempoEspera.sleep(1)
pyauto.click(x=146, y=512)
tempoEspera.sleep(7)
pyauto.click(x=382, y=352)

#coloque o usuario
pyauto.typewrite('usuario')
pyauto.click(x=390, y=426)

#coloque a senha

pyauto.typewrite('senha')
tempoEspera.sleep(5)
pyauto.click(x=370, y=797)



