from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QScrollArea, QGridLayout, QSizePolicy, QFrame, QSpacerItem, QMessageBox, QDialog
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPixmap, QIcon
from datetime import datetime
from pathlib import Path
from functools import partial


class Tablero(QMainWindow):
    def __init__(self, controlador, parent=None):
        super().__init__()
        self.__controlador = controlador
        
        self.setWindowTitle("Tablero de Juego")
        self.setGeometry(20, 30, 1500, 750)
        self.setWindowIcon(QIcon("imagenes/ui/icono.png"))
        path_script = Path(__file__).resolve()
        self.path_proyecto = path_script.parent.parent
        
        self.tiempo_restante = 60
        self.dinero_selecionado = []
        self.propiedad_selecionada = []
        self.carta_seleccionada = None
        self.jugador_seleccionado = None
        self.label_propiedad = None
        self.label_dinero = None
        self.deuda = 0
        self.labels_dinero = []
        self.labels_conjuntos_completos = []
        # Registro del tiempo de inicio de la partida:
        self.tiempo_inicio = datetime.now()
        
        # Configuración del temporizador:
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_tiempo)
        self.timer.start(1000)
        
        # Configuración para el titileo del reloj:
        self.titileo_timer = QTimer(self)
        self.titileo_timer.timeout.connect(self.titilar_reloj)
        self.reloj_titilando = False
        
        #region TODO_MENOS_EL_MINI_ZOOM
        
        # Widget principal:
        self.main_widget = QWidget(self)
        self.main_widget.setObjectName("MainWidget") # <-- Le doy el ID "MainWidget" para que funcione el CSS de abajo.
        self.setCentralWidget(self.main_widget)
        
        # Imagen de fondo usando CSS:
        self.main_widget.setStyleSheet("""
            QWidget#MainWidget {
                background-image: url("imagenes/ui/fondo_tablero_1650x820.jpg");
                background-repeat: no-repeat;
                background-position: center;
            }
            QLabel, QPushButton {
                background: none;
                border: none;
            }
        """)
        # Layout principal (zona superior e inferior):
        #region Instanciación y seteo de su layout.
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)
        
        # ---
        
        # Zona superior:
        self.zona_superior_layout = QHBoxLayout()
        self.main_layout.addLayout(self.zona_superior_layout, 2)
        
        # Zona inferior:
        self.zona_inferior_layout = QHBoxLayout()
        self.main_layout.addLayout(self.zona_inferior_layout, 2)

        # ---
        
        # Zona superior izquierda:
        self.zona_superior_izquierda_layout = QVBoxLayout()
        self.zona_superior_layout.addLayout(self.zona_superior_izquierda_layout, 1) # <-- El 1 es que tiene proporción 1.
        self.mostrar_jugadores(self.__controlador.get_jugadores())                                           # Si tienen ambos el mismo, van a
        #                                                                             ocupar el mismo ancho.
        # Zona superior derecha:
        self.zona_superior_derecha_layout = QVBoxLayout()
        self.zona_superior_layout.addLayout(self.zona_superior_derecha_layout, 1) # <-- (El comentario de arriba)
        #self.mostrar_tus_cartas()
        
        # ---
        
        # Zona inferior izquierda:
        self.zona_inferior_izquierda_layout = QVBoxLayout()
        self.zona_inferior_layout.addLayout(self.zona_inferior_izquierda_layout)
        
        # Zona inferior central:
        self.zona_inferior_central_layout = QVBoxLayout()
        self.zona_inferior_layout.addLayout(self.zona_inferior_central_layout)
        
        # Zona inferior derecha:
        self.zona_inferior_derecha_layout = QVBoxLayout()
        self.zona_inferior_layout.addLayout(self.zona_inferior_derecha_layout)
        #endregion
        # ----------------------------------------------------------------------
        #region ZONA DE BOTONES Y TURNOS
        # (Zona inferior izquierda):
        # (1) Empuje hacia abajo <-- Fijense, pruebenlo si les gusta empujado hacia abajo o sin eso, se ven distinto.
        # (2) Turno
        # (3) reloj
        # (Opcional): Espacio en blanco
        # (4) finalizar turno
        # (5) finalizar partida

        # (1):
        spacer_superior = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.zona_inferior_izquierda_layout.addItem(spacer_superior)
        
        # (2):
        turno_layout = QHBoxLayout()

        self.turno_icon = QLabel(self)
        turno_pixmap = QPixmap("imagenes/ui/turn.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.turno_icon.setPixmap(turno_pixmap)
        self.turno_icon.setFixedSize(50, 50) # <-- Hace que QLabel sea del mismo tamaño para que coincida con el del QPixmap.
        turno_layout.addWidget(self.turno_icon)

        self.turno_label = QLabel(f"Turno de: {self.__controlador.get_jugador_actual().nombre}", self)
        turno_layout.addWidget(self.turno_label)

        self.zona_inferior_izquierda_layout.addLayout(turno_layout)

        # (3):
        tiempo_layout = QHBoxLayout()

        self.reloj_icon = QLabel(self)
        self.reloj_pixmap = QPixmap("imagenes/ui/fixedClock.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.reloj_rojo_pixmap = QPixmap("imagenes/ui/fixedClockRojo.png").scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.reloj_icon.setPixmap(self.reloj_pixmap)
        self.reloj_icon.setFixedSize(50, 50) # <-- Hace que QLabel sea del mismo tamaño para que coincida con el del QPixmap.
        tiempo_layout.addWidget(self.reloj_icon)

        self.timer_label = QLabel(f"Tiempo restante: {self.tiempo_restante}s", self)
        tiempo_layout.addWidget(self.timer_label)

        self.zona_inferior_izquierda_layout.addLayout(tiempo_layout)
        
        # (Espacio vacío opcional entre medio):
        self.espacio_vacio_label = QLabel("") # <-- Un espacio vacío.
        self.zona_inferior_izquierda_layout.addWidget(self.espacio_vacio_label)
        
        # (4):
        self.btn_finalizar_turno = QPushButton("Finalizar Turno", self)
        self.btn_finalizar_turno.clicked.connect(self.__controlador.terminar_turno)
        self.zona_inferior_izquierda_layout.addWidget(self.btn_finalizar_turno)
        self.btn_finalizar_turno.setStyleSheet("""
            QPushButton {
                background-color: rgba(194, 78, 27, 0.2);
                color: white;
                border: 2px solid rgba(43, 22, 11, 1);
                border-radius: 10px;
                padding: 8px;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(194, 137, 48, 0.9);
            }
            QPushButton:pressed {
                background-color: rgba(125, 72, 34, 1);
            }
        """)
        
        # (5):
        self.btn_finalizar_partida = QPushButton("Finalizar Partida", self)
        self.btn_finalizar_partida.clicked.connect(self.__controlador.terminar_partida)
        self.zona_inferior_izquierda_layout.addWidget(self.btn_finalizar_partida)
        self.btn_finalizar_partida.setStyleSheet("""
            QPushButton {
                background-color: rgba(194, 78, 27, 0.2);
                color: white;
                border: 2px solid rgba(43, 22, 11, 1);
                border-radius: 10px;
                padding: 8px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(194, 137, 48, 0.9);
            }
            QPushButton:pressed {
                background-color: rgba(125, 72, 34, 1);
            }
        """)
        self.btn_finalizar_partida.setToolTip("Finaliza la partida para todos.")
        #endregion
        # ----------------------------------------------------------------------
        
        
        # Espacio en blanco, cartas (Zona inferior central)
        self.zona_inferior_central_layout.addWidget(self.espacio_vacio_label)
        
        self.cartas_layout = QHBoxLayout()
        self.zona_inferior_central_layout.addLayout(self.cartas_layout)
        
        self.mostrar_mano_jugador()
        
        # ----------------------------------------------------------------------
        # Descripción carta (Zona inferior derecha)
        descripcion_carta_layout = QVBoxLayout()

        # Descripción de carta
        self.descripcion_carta_label = QLabel(self)
        
        self.path_queHaceVacio = self.path_proyecto / "imagenes/ui/queHaceVacio.png"
        self.path_queHaceVacio = self.path_queHaceVacio.as_posix()

        pixmap_fondo = QPixmap(self.path_queHaceVacio).scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.descripcion_carta_label.setPixmap(pixmap_fondo) #                  |                                   | Estos dos dos Qt solucionan la vida.
        self.descripcion_carta_label.setFixedSize(400, 300)
        # Agregar el QLabel al layout:
        descripcion_carta_layout.addWidget(self.descripcion_carta_label)
        # Agregar el layout al área de la zona inferior derecha:
        self.zona_inferior_derecha_layout.addLayout(descripcion_carta_layout)
    #endregion TODO_MENOS_EL_MINI_ZOOM
    
    # ---------------------------------- MINI ZOOM --------------------------------------
    
    #region DISEÑO MINI ZOOM
        # Agregar el Mini menu
        ventana = QWidget()
        
        ventana.setStyleSheet("""
            QWidget {
                border: 3px solid red; /* Borde rojo */
                border-radius: 5px; /* Esquinas redondeadas */
                padding: 10px; /* Espaciado interno */
                background-color: transparent; /* Color de fondo */
            }
        """)
        # Layout principal
        contenedor = QVBoxLayout()
        contenedor.setContentsMargins(0, 0, 0, 0)
        # Crear el primer widget (cartas)
        self.cartas_ = QWidget()
        #cartas.setFixedSize(100, 150)
        self.cartas_layouts = QGridLayout(self.cartas_)  # Layout interno de "cartas"
        self.cartas_layouts.setContentsMargins(0, 0, 0, 0)
        # .setStyleSheet("background-color: transparent;")
    

        

        
        #self.cartas_layout.addWidget(QLabel("a"), 0, 3)
        # Crear el widget con los botones
        botones = QWidget()
        self.botones_layout = QHBoxLayout(botones)  # Layout interno de "botones"
        self.pestaña_cartas()
        
        
        botones.setStyleSheet("""
            QPushButton {
                background-color: rgba(194, 78, 27, 0.2);
                color: white;
                border: 2px solid rgba(43, 22, 11, 1);
                border-radius: 10px;
                padding: 8px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(194, 137, 48, 0.9);
            }
            QPushButton:pressed {
                background-color: rgba(125, 72, 34, 1);
            }
        """)
        # Añadir los widgets al layout principal
        contenedor.addWidget(self.cartas_)  # Primera fila
        contenedor.addWidget(botones)  # Segunda fila # Segunda fila
        contenedor.setStretch(0, 8)  # El primer widget (cartas) ocupa el 80% del espacio
        contenedor.setStretch(1, 2)  # El segundo widget (botones) ocupa el 20% del espacio

        ventana.setLayout(contenedor)
        ventana.setFixedSize(700, 400)
        self.zona_superior_derecha_layout.addWidget(ventana)
        
        #self.agregar_cartas()
    #endregion DISEÑO MINI ZOOM
    
    #region CARGAR_CARTAS
    def cargar_cartas(self,tipo,jugador):
        self.limpiar_layout(self.cartas_layouts)
        #self.carta_seleccionada = None
        filas = 0
        columnas = 0
        if tipo == "propiedad":
            
            listas = jugador.get_sets_completos_jugador()
            if len(listas) < 11:
                for diccionarios in listas:
                    if isinstance(diccionarios, dict):
                        columnas += 1
                        grupo =  self.agregar_cartas(diccionarios["sublista"],tipo)
                        self.cartas_layouts.addWidget(grupo, filas, columnas)
                        if columnas == 5:
                            filas +=1
                            columnas = 0
                    else:
                        print("No es un diccionario")
        elif tipo == "dinero":
            
            lista = jugador.get_banco()  # Llamas al método para obtener la lista
            sublistas = [lista[i:i + 5] for i in range(0, len(lista), 5)]
            if len(sublistas) < 11:
                for cartas in sublistas:
                    
                    columnas += 1
                    grupo =  self.agregar_cartas(cartas,tipo)
                    self.cartas_layouts.addWidget(grupo, filas, columnas)
                    if columnas == 5:
                        filas +=1
                        columnas = 0
    #endregion CARGAR_CARTAS
                
    #region AGREGAR_CARTAS
    def agregar_cartas(self, sublista,tipo):   
        grupos = QWidget()
        for index, carta in enumerate(sublista):
            label_carta = QLabel(self)
            label_carta.mousePressEvent = lambda _, label=label_carta, carta_actual=carta: self.resaltar_carta(label, tipo, carta_actual)
            label_carta.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            label_carta.setScaledContents(True)
            label_carta.setMinimumSize(60, 100)  # Tamaño mínimo de la carta
            label_carta.setMaximumSize(80, 120)  # Tamaño máximo de la carta
            pixmap = QPixmap(carta.path_a_imagen)
            label_carta.setPixmap(pixmap)  # Establece la imagen en el QLabel
            self.agregar_carta(label_carta, grupos, offset=index * 20)
            
        return grupos
    #endregion AGREGAR_CARTAS
    
    #region AGREGAR_CARTA
    def agregar_carta(self, carta, padre, offset):
        """
        Agrega una carta al widget `mano_contenedora` con un desplazamiento para simular superposición.
        """
        max_width = padre.width()  # Obtiene el ancho máximo del contenedor
        if offset < max_width:  # Si el desplazamiento está dentro de los límites del contenedor
            carta.setParent(padre)  # Establecer el padre
            carta.move(offset, 20)  # Posicionar con superposición (offset horizontal)
            carta.show()
        else:
            print("No hay suficiente espacio para mover la carta.")
    #endregion AGREGAR_CARTA
    #region RESALTAR_CARTA
    def resaltar_carta(self, label, tipo,carta):
        
        # Si es una carta de dinero
        if tipo == "dinero":
            # Si ya hay una carta de dinero seleccionada, quita su borde
            if hasattr(self, 'label_dinero') and self.label_dinero is not None:
                self.label_dinero.setStyleSheet("border: 2px solid transparent;")

            # Asigna la nueva carta de dinero seleccionada
            self.label_dinero = label
            
            self.carta_seleccionada = carta
            self.carta_seleccionada.mostrar_carta()
            
            # Agrega el borde rojo a la carta de dinero seleccionada
            self.label_dinero.setStyleSheet("border: 2px solid red;")

            # Limpiar la carta de propiedad seleccionada
            self.label_propiedad = None

        # Si es una carta de propiedad
        elif tipo == "propiedad":
            # Si ya hay una carta de propiedad seleccionada, quita su borde
            if hasattr(self, 'label_propiedad') and self.label_propiedad is not None:
                self.label_propiedad.setStyleSheet("border: 2px solid transparent;")

            # Asigna la nueva carta de propiedad seleccionada
            self.label_propiedad = label
            
            self.carta_seleccionada = carta
            self.carta_seleccionada.mostrar_carta()
            # Agrega el borde rojo a la carta de propiedad seleccionada
            self.label_propiedad.setStyleSheet("border: 2px solid red;")

            # Limpiar la carta de dinero seleccionada
            self.label_dinero = None

        else:
            print("Carta Vacia")
    #endregion RESALTAR_CARTA
    # ---------------------------------- MINI ZOOM --------------------------------------
    
    #region LIMPIAR_LAYOUT
    def limpiar_layout(self, layout):
        """Elimina todos los widgets de un layout."""
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
            elif item.layout():
                self.limpiar_layout(item.layout())
    #endregion LIMPIAR_LAYOUT
    
    #region SELECCIONAR Y ELEGIR
    def seleccionar_jugador(self, event, jugador, avatar):
        if self.layout_selecionado:  
            self.layout_selecionado.setStyleSheet("border: none;")
        avatar.setStyleSheet("border: 2px solid red;")
        # Guarda el jugador seleccionado
        self.jugador_seleccionado = jugador
        self.layout_selecionado = avatar

    def get_jugador_seleccionado(self):
        jugador = self.jugador_seleccionado
        self.jugador_seleccionado = None
        return jugador

    def seleccionar_dinero(self, dinero,jugador):
        self.dinero_selecionado.append(dinero)
        self.deuda -= dinero.valor
        if self.deuda < 0:
            jugador.pagar_banco(dinero)
            self.deuda = 0
            self.pestaña_cartas()
        else:
            jugador.pagar_banco(dinero)
            self.carta_seleccionada = None
            if hasattr(self, 'label_dinero') and self.label_dinero is not None:
                self.label_dinero.deleteLater()
                self.label_dinero = None
            self.elejir_dinero(jugador,self.deuda)
    
    def elejir_dinero(self, jugador, monto):
        self.deuda = monto
        self.limpiar_layout(self.botones_layout)
        self.cargar_cartas("dinero", jugador)
        # Mostrar el monto a cobrar
        total_pago = QLabel(f"Deuda: {self.deuda}")
        self.botones_layout.addWidget(total_pago)
        elejir_dinero_button = QPushButton("Cobrar")
        elejir_dinero_button.clicked.connect(lambda: self.seleccionar_dinero(self.carta_seleccionada, jugador))
        self.botones_layout.addWidget(elejir_dinero_button)
    
    def elejir_jugador(self, jugadores_totales, jugador_actual):
        # Quita al jugador que esta eligiendo de la lista
        jugadores = [jugador for jugador in jugadores_totales if jugador != jugador_actual]
        for index, jugador in enumerate(jugadores):
            perfil = QHBoxLayout()
            # Nombre del jugador
            nombre = QLabel(f"{jugador.nombre}")
            # Avatar del jugador
            avatar = QLabel()
            avatar_img = QPixmap(jugador.avatar)
            avatar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            avatar.setScaledContents(True) 
            avatar.setFixedSize(150, 150)
            avatar.setPixmap(avatar_img)
            avatar.setStyleSheet("border: none;")
            # Agregar al layout del perfil
            perfil.addWidget(avatar)
            perfil.addWidget(nombre)
            # Añadir el perfil al layout principal
            self.cartas_layouts.addLayout(perfil, 0, index)
            # Asignar el evento al avatar (cuidado con el uso de lambda)
            avatar.mousePressEvent = lambda event, jugador=jugador, avatar=avatar: self.seleccionar_jugador(event, jugador, avatar)
    #endregion SELECCIONAR Y ELEGIR
    
    #region UPDATE_INTERFAZ
    def update_interfaz(self):
        self.pestaña_cartas()
        self.mostrar_jugadores(self.__controlador.get_jugadores())
        self.mostrar_mano_jugador()
        self.repaint()
    #endregion UPDATE_INTERFAZ
    
    #region NUEVOS ELEGIR Y SELECCIONAR
    #region UPDATE_LABEL_DINERO
    def actualizar_dinero_jugadores(self):
        jugadores = self.__controlador.get_jugadores()
        for i, jugador in enumerate(jugadores):
            self.labels_dinero[i].setText(f"Dinero: ${jugador.calcular_valor_banco()}")
    #endregion UPDATE_LABEL_DINERO
    def pedido_elejir_jugador(self, jugadores):
        dialogo = QDialog()
        dialogo.setWindowTitle("Elegir Jugador")
        dialogo.setFixedSize(400, 300) 
        dialogo.jugador_seleccionado = None
        dialogo.avatar_seleccionado = None
        # Layout principal
        layout_V = QVBoxLayout(dialogo)
        # Mensaje
        mensaje = QLabel("Seleccione un jugador:")
        layout_V.addWidget(mensaje)
        # Contenedor para los jugadores
        contendor_jugadores = QWidget()
        layout_H = QHBoxLayout()
        contendor_jugadores.setLayout(layout_H)
        # Iterar sobre jugadores
        for jugador in jugadores:
            layout_jugador = QVBoxLayout()
            ## Imagen del jugador
            avatar = QLabel()
            pixmap = QPixmap(jugador.avatar)
            avatar.setPixmap(pixmap)
            avatar.setFixedSize(100, 100)
            avatar.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            avatar.setScaledContents(True)
            def seleccionar_jugador(event, jugador=jugador, avatar=avatar):
                # Quitar el borde del avatar previamente seleccionado
                if dialogo.avatar_seleccionado is not None:
                    dialogo.avatar_seleccionado.setStyleSheet("""border: 2px solid black; border-radius: 10px;""")
                # Cambiar el borde del avatar actual
                avatar.setStyleSheet("""border: 2px solid red; border-radius: 10px;""")
                # Actualizar referencias
                dialogo.avatar_seleccionado = avatar
                dialogo.jugador_seleccionado = jugador
            avatar.mouseReleaseEvent = seleccionar_jugador
            layout_jugador.addWidget(avatar)
            ## Nombre del jugador
            nombre = QLabel(jugador.nombre)
            nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout_jugador.addWidget(nombre)
            # Añadir al layout horizontal
            layout_H.addLayout(layout_jugador)

        # Añadir contenedor al layout vertical
        layout_V.addWidget(contendor_jugadores)
        def confirmar_seleccion():
            if dialogo.jugador_seleccionado is not None:
                dialogo.accept()
            else:
                print("Ningún jugador seleccionado.")
        boton_confirmar = QPushButton("Confirmar")
        # Botón de confirmación
        
        boton_confirmar.clicked.connect(confirmar_seleccion)
        layout_V.addWidget(boton_confirmar)
        return dialogo
    
    #region PEDIDO DINERO
    def pedido_elegir_dinero(self,jugador,monto):
        # Limpia layouts
        self.limpiar_layout(self.cartas_layouts)
        self.limpiar_layout(self.botones_layout)
        # Crea un QDialog para usarlo como ventana emergente
        dialogo = QDialog()
        dialogo.setFixedSize(700, 400)
        layout = QVBoxLayout(dialogo)
        grilla  = self.cartas_
        layout.addWidget(grilla)
        self.cargar_cartas("dinero",jugador)
        # Agrega un botón de cerrar
        deuda =  QLabel(f"Deuda: {self.deuda}")
        boton_agarrar = QPushButton("Agarrar")
        boton_agarrar.clicked.connect(partial(self.seleccionar_dinero(self.carta_seleccionada,jugador)))
        cerrar_boton = QPushButton("Cerrar")
        cerrar_boton.clicked.connect(dialogo.accept)  # Cierra el diálogo cuando se presiona
        layout.addWidget(cerrar_boton)
        layout.addWidget(boton_agarrar)
        layout.addWidget(deuda)
        dialogo.setLayout(layout)
        return dialogo
    #endregion PEDIDO DINERO
    
    #region PEDIDO PROPIEDADES
    def pedido_elegir_propiedades(self,propiedades,jugador):
            # Limpia layouts
            self.limpiar_layout(self.cartas_layouts)
            self.limpiar_layout(self.botones_layout)
            # Crea un QDialog para usarlo como ventana emergente
            dialogo = QDialog()
            dialogo.setFixedSize(700, 400)
            layout = QVBoxLayout(dialogo)
            grilla  = self.cartas_
            layout.addWidget(grilla)
            self.cargar_cartas("propiedad",jugador)
            # Agrega un botón de cerrar
            agarrar_propiedad = QPushButton("Agarrar Propiedad")
            agarrar_propiedad.clicked.connect(partial(self.seleccionar_propiedad(jugador)))
            layout.addWidget(agarrar_propiedad)
            cerrar_boton = QPushButton("Cerrar")
            cerrar_boton.clicked.connect(dialogo.accept)  # Cierra el diálogo cuando se presiona
            layout.addWidget(cerrar_boton)
            dialogo.setLayout(layout)
            return dialogo
    #endregion PEDIDO PROPIEDADES
    
    #region PEDIDO COLOR
    def pedido_elegir_color(self,colores,carta):
            # Limpia layouts
            self.limpiar_layout(self.cartas_layouts)
            self.limpiar_layout(self.botones_layout)
            # Crea un QDialog para usarlo como ventana emergente
            dialogo = QDialog()
            dialogo.color_seleccionado = None
            dialogo.setWindowTitle("Elegir Color")
            layout = QVBoxLayout(dialogo)
            carta_img = QLabel() 
            pixmap = QPixmap(carta.path_a_imagen)
            carta_img.setFixedSize(150, 200)
            carta_img.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            carta_img.setScaledContents(True)
            carta_img.setPixmap(pixmap)
            layout.addWidget(carta_img)
            for color  in colores:
                boton_color = QPushButton(f"{color}")
                def seleccionar_color():
                    dialogo.color_seleccionado = color
                    dialogo.accept()
                boton_color.clicked.connect(seleccionar_color)
                layout.addWidget(boton_color)
            cerrar_boton = QPushButton("Cerrar")
            cerrar_boton.clicked.connect(dialogo.reject)  # Cierra el diálogo cuando se presiona
            layout.addWidget(cerrar_boton)
            dialogo.setLayout(layout)
            return dialogo
    #endregion PEDIDO COLOR
    
    #region SELECC JUGADOR
    def seleccionar_jugador(self, event, jugador, avatar):
        # Si ya hay un avatar seleccionado, le quitamos el borde rojo
        if self.avatar_seleccionado is not None:
            self.avatar_seleccionado.setStyleSheet("""border: 2px solid black; border-radius: 10px;""")
        
        # Cambiar el borde del avatar seleccionado
        avatar.setStyleSheet("""border: 2px solid red; border-radius: 10px;""")
        
        # Actualizamos la referencia al avatar seleccionado
        self.avatar_seleccionado = avatar
        self.jugador_seleccionado = jugador
    #endregion SELECC JUGADOR
    
    #region SELECC COLOR
    def seleccionar_color(self,color):
        self.color_seleccionado = color
        print(self.color_seleccionado)
    #endregion SELECC COLOR
    
    #region SELECC PROPIEDAD
    def seleccionar_propiedad(self,jugador):
        self.propiedad_seleciconada.append(self.carta_seleccionada)
        clase_propiedad = jugador.get_objeto_propiedad()
        clase_propiedad.quitar_propiedad(self.carta_seleccionada)
    #endregion SELECC PROPIEDAD
    
    #region SELECC DINERO
    def seleccionar_dinero(self, dinero,jugador):
        self.dinero_selecionado.append(dinero)
        self.deuda -= dinero.valor
        if self.deuda < 0:
            jugador.pagar_banco(dinero)
            self.deuda = 0
            self.pestaña_cartas()
        else:
            jugador.pagar_banco(dinero)
            self.carta_seleccionada = None
            if hasattr(self, 'label_dinero') and self.label_dinero is not None:
                self.label_dinero.deleteLater()
                self.label_dinero = None
            self.pedido_elegir_dinero(jugador,self.deuda)
    #endregion SELECC DINERO
    
    #region UPDATE_LABEL_CONJUNTOS
    def actualizar_conjuntos_jugadores(self):
        jugadores = self.__controlador.get_jugadores()
        for i, jugador in enumerate(jugadores):
            self.labels_conjuntos_completos[i].setText(f"SCs: {jugador.get_cantidad_sets_completos_jugador()}")
    #endregion UPDATE_LABEL_CONJUNTOS
    
    #region PESTAÑA_CARTAS
    def pestaña_cartas(self):
        self.limpiar_layout(self.botones_layout)
        self.limpiar_layout(self.cartas_layouts)
        propiedades_button = QPushButton("Propiedades")
        dinero_button = QPushButton("Dinero")
        descarte_button = QPushButton("Descarte")
        propiedades_button.clicked.connect(lambda:self.cargar_cartas("propiedad", self.__controlador.get_jugador_actual()))
        dinero_button.clicked.connect(lambda:self.cargar_cartas("dinero", self.__controlador.get_jugador_actual()))
        # descarte_button.clicked.connect(self.elejir_color)
        self.botones_layout.addWidget(propiedades_button)
        self.botones_layout.addWidget(dinero_button)
        self.botones_layout.addWidget(descarte_button)    
    #endregion PESTAÑA_CARTAS
    
    #region MOSTRAR_JUGADORES
    def mostrar_jugadores(self, jugadores):
        """Muestra la información de los jugadores."""
        self.limpiar_layout(self.zona_superior_izquierda_layout)
        self.labels_dinero.clear()
        self.labels_conjuntos_completos.clear()
        for jugador in jugadores:
            jugador_layout = QHBoxLayout()      # <--   (Perfil) | (Propiedades) | (Banco)
            propiedades_layout = QGridLayout()
            banco_layout = QGridLayout()

            # --- Perfil ---

            # Crear un contenedor para todo el conjunto de avatar, nombre y dinero:
            perfil_contenedor = QWidget(self)
            perfil_contenedor.setStyleSheet("""
                QWidget {
                    background-color: rgba(207, 106, 39, 0.2);
                    border: 2px solid rgba(43, 22, 11, 1);
                    border-radius: 10px;
                    padding: 10px;         /*<-- Padding es un espaciado interno, super útil. */
                }
            """)

            # Layout del contenedor:
            perfil_layout = QHBoxLayout(perfil_contenedor)
            perfil_layout.setContentsMargins(10, 10, 10, 10) # <-- Márgenes internos del contenedor
            perfil_layout.setSpacing(15)                     # <-- Espaciado entre el avatar y el texto

            # Avatar:
            avatar = QPixmap(jugador.avatar) # <-- (No escalar acá)
            if avatar.isNull():
                print(f"Error! No se pudo cargar este avatar: {jugador.avatar}")
            avatar_label = QLabel(self)
            avatar_label.setPixmap(avatar)
            avatar_label.setToolTip(f'Este es el avatar del jugador "{jugador.nombre}".')

            # Configuración para escalar el avatar adentro del espacio disponible:
            avatar_label.setScaledContents(True)   # <-- (Muy opcional) Permite que la imagen se escale dentro del QLabel.
            avatar_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

            # Definir un tamaño máximo y mínimo para evitar que ocupe toda la pantalla:
            avatar_label.setMaximumSize(100, 100)
            avatar_label.setMinimumSize(50, 50)    # <-- (Opcional)

            # Agregar el avatar al layout del contenedor:
            perfil_layout.addWidget(avatar_label) #, alignment=Qt.AlignmentFlag.AlignLeft)

            # Contenedor para el texto (nombre y dinero):
            texto_layout = QVBoxLayout()
            texto_layout.setSpacing(5)   # <-- Espaciado entre el nombre y el dinero.

            # Nombre:
            nombre_label = QLabel(f"{jugador.nombre}")
            nombre_label.setFixedSize(100, 33)
            nombre_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            nombre_label.setStyleSheet("""
                font-size: 14px; 
                font-weight: bold;
                color: white;
                background-color: rgba(46, 21, 8, 0.7);
                padding: 5px;
                border-radius: 5px;
            """)
            texto_layout.addWidget(nombre_label)
            nombre_label.setToolTip(f'"{jugador.nombre}" es uno de los jugadores de esta partida.')

            # Dinero:
            dinero_label = QLabel(f"Actualizando...")
            dinero_label.setFixedSize(100, 33)
            dinero_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            dinero_label.setStyleSheet("""
                font-size: 13px;
                font-weight: bold;
                color: white;
                background-color: rgba(46, 21, 8, 0.7);
                padding: 5px;
                border-radius: 5px;
            """)
            texto_layout.addWidget(dinero_label)
            self.labels_dinero.append(dinero_label)
            dinero_label.setToolTip(f'Este es el dinero del jugador "{jugador.nombre}".')
            
            # Conjuntos completos:
            scs_label = QLabel(f"Actualizando...")
            scs_label.setFixedSize(100, 33)
            scs_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            scs_label.setStyleSheet("""
                font-size: 14px;
                font-weight: bold;
                color: white;
                background-color: rgba(46, 21, 8, 0.7);
                padding: 5px;
                border-radius: 5px;
            """)
            texto_layout.addWidget(scs_label)
            self.labels_conjuntos_completos.append(scs_label)
            scs_label.setToolTip(f'Estos son los Sets Completos del jugador "{jugador.nombre}".')
            
            # Agregar el layout del texto al perfil:
            perfil_layout.addLayout(texto_layout)

            # Agregar el contenedor al layout del jugador:
            jugador_layout.addWidget(perfil_contenedor)
            
            # --- Propiedades ---
            propiedades_widget = QWidget(self)
            propiedades_widget.setLayout(propiedades_layout)
            propiedades_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            propiedades_layout.setSpacing(5)
            self.mostrar_cartas_en_cuadricula(propiedades_layout, jugador.get_propiedades(), "propiedad")
            jugador_layout.addWidget(propiedades_widget, 2)
            
            # --- Banco ---
            banco_widget = QWidget(self)
            banco_widget.setLayout(banco_layout)
            banco_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            propiedades_layout.setSpacing(5) 
            self.mostrar_cartas_en_cuadricula(banco_layout, jugador.get_banco(), "banco")
            jugador_layout.addWidget(banco_widget, 2)
            
            # Agregar el layout jugador al layout de la zona superior izquierda:
            self.zona_superior_izquierda_layout.addLayout(jugador_layout)
    #endregion MOSTRAR_JUGADORES
    
    #region MOSTRAR_CARTAS_EN_CUADRICULA
    def mostrar_cartas_en_cuadricula(self, grid_layout, cartas, tipo=None):
        
        """
        Rellena la cuadrícula indicada con las imágenes de las cartas que tiene
        y se asegura de que todas las celdas estén presentes, incluso si están vacías.
        """
        self.limpiar_layout(grid_layout)
        columnas = 9
        filas = 2
        total_celdas = filas * columnas
        if tipo == "propiedad":
            
            #cant_cartas = self.contar_propiedades(cartas)
            
            #print("Recorrido")
            listas = []
            for color,lista in cartas.items():
                        for cartas in lista["lista"]:
                            listas.extend(cartas["sublista"])
            cant_cartas = min(len(listas), total_celdas)
            for index in range(total_celdas):
                
                
                fila = index // columnas
                columna = index % columnas
                if index < cant_cartas :
                    print(f"Index: {index}")
                    print(f"Cartas: {cant_cartas}")
                    
                    # Si hay una carta en esta posición, muestra la carta:
                    
                    carta = listas[index]
                    carta_label = QLabel(self)
                    #carta_label.setFixedSize(25, 40)
                    carta_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                    carta_label.setScaledContents(True)
                    carta_label.setMinimumSize(35, 60)  # Puedes ajustar el tamaño mínimo según el diseño
                    carta_label.setMaximumSize(35, 65)
                    pixmap = QPixmap(carta.path_a_imagen)#.scaled(23, 40, Qt.AspectRatioMode.KeepAspectRatio)
                    #carta.mostrar_carta()
                    carta_label.setPixmap(pixmap)
                    carta_label.setToolTip(carta.nombre)
                    grid_layout.addWidget(carta_label, fila, columna)
                else:
                    
                    # Si no hay carta, agrega un QLabel vacío como placeholder:
                    #print("Entro al else")
                    placeholder = QLabel(self)
                    placeholder.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                    placeholder.setScaledContents(True)
                    placeholder.setMinimumSize(35, 60)  # Puedes ajustar el tamaño mínimo según el diseño
                    placeholder.setMaximumSize(35, 65)
                    placeholder.setStyleSheet("background-color: transparent; border: 1px solid gray;")
                    placeholder.setToolTip("No hay carta aquí.")
                    grid_layout.addWidget(placeholder, fila, columna)
        else:
            
            for index in range(total_celdas):
                fila = index // columnas
                columna = index % columnas
                if index < len(cartas) :
                    # Si hay una carta en esta posición, muestra la carta:
                    carta = cartas[index]
                    carta_label = QLabel(self)
                    carta_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                    carta_label.setScaledContents(True)
                    carta_label.setMinimumSize(35, 60)  # Puedes ajustar el tamaño mínimo según el diseño
                    carta_label.setMaximumSize(35, 65)
                    pixmap = QPixmap(carta.path_a_imagen) #.scaled(23, 40, Qt.AspectRatioMode.KeepAspectRatio)
                    carta_label.setPixmap(pixmap)
                    carta_label.setToolTip(carta.nombre)
                    grid_layout.addWidget(carta_label, fila, columna)
                else:
                    # Si no hay carta, agrega un QLabel vacío como placeholder:
                    placeholder = QLabel(self)
                    placeholder.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                    placeholder.setScaledContents(True)
                    placeholder.setMinimumSize(35, 60)  # Puedes ajustar el tamaño mínimo según el diseño
                    placeholder.setMaximumSize(35, 65)
                    placeholder.setStyleSheet("background-color: transparent; border: 1px solid gray;")
                    placeholder.setToolTip("No hay carta aquí.")
                    grid_layout.addWidget(placeholder, fila, columna)
    #endregion MOSTRAR_CARTAS_EN_CUADRICULA

    #region MOSTRAR_MANO_JUGADOR
    def mostrar_mano_jugador(self):
        """Muestra las cartas en la mano del jugador actual y actualiza la descripción."""
        
        # Limpiar el área de las cartas antes de agregar otras nuevas:
        while self.cartas_layout.count():
            widget = self.cartas_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        jugador_actual = self.__controlador.get_jugador_actual()
        cartas = jugador_actual.get_mano()
        
        imagen_vacia = self.path_proyecto / "imagenes/cartas/cartaVacia.png"
        imagen_vacia = imagen_vacia.as_posix()

        # Lógica para mostrar hasta 7 cartas:
        for i in range(7):      # <-- (No se va a exceder, pero igual tengo que usarlo).
            # Creación del widget de cada carta:
            carta_label = QLabel(self)
            
            # Esta disposición del código es perfecta, hace que al seleccionar una carta vacía no se actualice la imagen de descripció:
            if i < len(cartas):
                carta = cartas[i]
                carta_imagen = carta.path_a_imagen
                # Actualizar al clickear:
                carta_label.mousePressEvent = self.evento_click_carta(carta)
            else:
                carta_imagen = imagen_vacia
            pixmap = QPixmap(carta_imagen).scaled(100, 150, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            carta_label.setPixmap(pixmap)
            carta_label.setFixedSize(100, 150)
            #carta_label.setStyleSheet("border: 1px solid black;") <-- Opcional

            # Agregar carta al layout:
            self.cartas_layout.addWidget(carta_label)
    #endregion MOSTRAR_MANO_JUGADOR

    #region EVENTO_CLICK_CARTA
    def evento_click_carta(self, carta):
        """Actualizar la imagen de descripción al haber hecho click, por la imagen que se indica."""
        def evento(_):
            descripcion_imagen = carta.path_a_queHace
            if carta == self.carta_seleccionada:
                #print("Doble click detectado.")
                
                self.__controlador.jugar_carta(carta)
                
                
                self.carta_seleccionada = None
                self.update_interfaz()
            else:
                self.carta_seleccionada = carta # <-- Almacena primer click.
                
                if descripcion_imagen: # <-- En caso de que si tenga contenido descripcion_imagen.
                    pixmap_descripcion = QPixmap(descripcion_imagen).scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.descripcion_carta_label.setPixmap(pixmap_descripcion)
                else:                  # <-- En caso de que sea Null porque no hay carta, usa la imagen vacía. (Igual ya no va a pasar)
                    pixmap_descripcion = QPixmap(self.path_queHaceVacio).scaled(400, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    self.descripcion_carta_label.setPixmap(pixmap_descripcion)
                #self.update_interfaz()    
                
        return evento
    #endregion EVENTO_CLICK_CARTA
    
    #region CARTA_NO_JUGABLE
    def carta_no_es_jugable(self):
        QMessageBox.warning(self, "Carta No Jugable", "Esta carta no se puede jugar en este momento.", QMessageBox.StandardButton.Ok)
    #endregion CARTA_NO_JUGABLE

    #region TITILAR_RELOJ
    def titilar_reloj(self):
        """Alterna entre las dos imágenes del reloj para crear el efecto del titileo."""
        if self.reloj_titilando:
            self.reloj_icon.setPixmap(self.reloj_pixmap)
        else:
            self.reloj_icon.setPixmap(self.reloj_rojo_pixmap)
        self.reloj_titilando = not self.reloj_titilando
    #endregion TITILAR_RELOJ
    
    #region ACTUALIZAR_TIEMPO
    def actualizar_tiempo(self):
        """Actualiza el temporizador."""
        if self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.timer_label.setText(f"Tiempo restante: {self.tiempo_restante}s")
            
            self.reloj_icon.setToolTip(f"Tiempo restante de tu turno (te quedan {self.tiempo_restante}s).")
            self.timer_label.setToolTip(f"Tiempo restante de tu turno (te quedan {self.tiempo_restante}s).")
            
            self.turno_icon.setToolTip(f'Este es el turno actual (el de "{self.__controlador.get_jugador_actual().nombre}", o sea tú).')
            self.turno_label.setToolTip(f'Este es el turno actual (el de "{self.__controlador.get_jugador_actual().nombre}", o sea tú).')
            
            self.actualizar_dinero_jugadores()
            self.actualizar_conjuntos_jugadores()
            
        # Iniciar el titileo cuando queden 5, o 10, o 15, segundos. <-- (A gusto como quieran, me parece que 15 está bien)
            if self.tiempo_restante <= 15:
                if not self.titileo_timer.isActive():
                    self.titileo_timer.start(500)     # <-- Esto cambia la imagen cada 500 ms.
        else:
            self.titileo_timer.stop() # <-- Detiene el titileo cuando el tiempo termine.
            self.__controlador.terminar_turno()
    #endregion ACTUALIZAR_TIEMPO

    #region FINALIZAR_TURNO
    def finalizar_turno(self):
        """
        Finaliza el turno y pasa al siguiente jugador.
        Acá va la lógica que se maneja cuando finaliza el tiempo.
        """
        # pro2 = self.__controlador.get_jugador_actual().get_propiedades
        # self.turno_actual = (self.turno_actual + 1) % len(self.__controlador.get_jugadores())
        self.turno_label.setText(f"Turno de: {self.__controlador.get_jugador_actual().nombre}")
        self.tiempo_restante = 60
        self.timer_label.setText(f"Tiempo restante: {self.tiempo_restante}s")

        self.reloj_icon.setPixmap(self.reloj_pixmap)
        self.titileo_timer.stop()
        
        self.carta_seleccionada = None
        
        self.mostrar_mano_jugador()
    #endregion FINALIZAR_TURNO
    
    #region FINALIZAR_PARTIDA
    def finalizar_partida(self):
        """Pregunta al usuario si está seguro de que la quiere finalizar."""
        respuesta = QMessageBox.question(
            self,
            "Confirmar finalización",
            "¿Estás seguro de que querés finalizar la partida?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if respuesta == QMessageBox.StandardButton.Yes:
            self.muestra_resumen_y_sale()
        else:
            pass
    #endregion FINALIZAR_PARTIDA
    
    #region RESUMEN SALIR
    def muestra_resumen_y_sale(self):
        # Cálculo del tiempo:
            tiempo_fin = datetime.now()
            tiempo_total = tiempo_fin - self.tiempo_inicio # <-- Diferencia entre el inicio y el final.
            minutos, segundos = divmod(tiempo_total.total_seconds(), 60)
            tiempo_formateado = f"{int(minutos)} minutos y {int(segundos)} segundos"
            
            # Cálculo del resumen de la partida:
            resumen = "Resumen de la partida jugada:\n\n"
            resumen += f"Tiempo total jugado: {tiempo_formateado}\n\n"
            
            for jugador in self.__controlador.get_jugadores():
                propiedades = len(jugador.get_objeto_propiedad().get_cartas_propiedades())
                dinero_final = jugador.calcular_valor_banco_propiedades()

                acciones_usadas = len(jugador.get_mano()) # <-- Ejemplo (falta implementar).
                
                resumen += (
                    f"Jugador: {jugador.nombre}\n"
                    f"Dinero final: ${dinero_final}\n"
                    f"Propiedades adquiridas: {propiedades}\n"
                    f"Cartas de acción usadas: {acciones_usadas}\n\n"
                )
            
            resumen += "¡Muchas gracias por jugar!"
            
            # Mostrar el cuadro con la información de la partida:
            QMessageBox.information(
                self,
                "Resumen de la Partida",
                resumen,
                QMessageBox.StandardButton.Ok
        )
            
            self.__controlador.volver()
    #endregion RESUMEN SALIR
