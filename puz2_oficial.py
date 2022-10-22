import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import threading
from pn532pi import Pn532, pn532
from pn532pi import Pn532Hsu
from p112 import Rfid

class Puz2(Gtk.Window):
    def __init__(self):
        
        super().__init__(title="Rfid_gtk.py")
        self.set_border_width(15)
        self.connect("destroy", Gtk.main_quit)
        #creamops el objeto caja CUYA DISTRIBUCION SEA EN VERTICAL
        self.box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
        self.add(self.box)
        self.box.set_homogeneous(False)
        #creamos una caja para poner el texto
        self.tlabel=Gtk.Label(label="Please, log in your university card")
        self.tlabel.set_size_request(800,400)
        self.tlabel.set_name("entrada")
        self.box.pack_start(self.tlabel,True,True,0)
        
        # creamos el botton de clear y que este este conectado a imprimir cosas por pantalla
        self.button = Gtk.Button(label="Clear")
        self.button.connect("clicked",self.cc_b1)
        self.box.pack_start(self.button, True,True,0)
        
        ## colores
        self.azul = b"""
        #entrada {
            background:#05EBF2;
            font: bold 30px Courier New;
            color: #FFFFFF;
        }
        """
        self.rojo = b"""
        #entrada {
            background:#F633FF;
            font: bold 30px Courier New;
            color: #FFFFFF;
        }
        """
        ## iniciamos la definicion de colores con el css
        screen = Gdk.Screen.get_default()
        self.provider = Gtk.CssProvider()
        self.provider.load_from_data(self.azul)
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, self.provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        
        ##acabo colores
        ## empezamos un thread
        self.t1 = threading.Thread(target=self.leer_tarjeta)
        self.t1.setDaemon(True)
        self.t1.start()
       
        
    def cc_b1(self, widget):
        self.tlabel.set_text("Please, log in your university card")
        self.t1 = threading.Thread(target=self.leer_tarjeta)
        self.t1.setDaemon(True)
        self.provider.load_from_data(self.azul)
        self.t1.start()
        
        
    def leer_tarjeta(self):
        self.tarjeta=Rfid()
        identificador= self.tarjeta.read_uid()
        self.provider.load_from_data(self.rojo)
        self.tlabel.set_text("UID: "+identificador)
        
        
window=Puz2()
window.show_all()
Gtk.main()
