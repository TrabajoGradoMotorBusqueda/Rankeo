#############################################CREACION DE CLASES#################################################


#IMPORTAR RUTA

with ontologia:
	#GRUPO DE INVESTIGACION
	class Grupo_investigacion(Thing):

		def get_id_grupo_investigacion(self):
			return self.id_grupo_investigacion

		def set_id_grupo_investigacion(self,id_grupo_investigacion):
			self.id_grupo_investigacion = [id_grupo_investigacion]

		def get_nombre_grupo_investigacion(self):
			return self.nombre_grupo_investigacion
		
		def set_nombre_grupo_investigacion(self,nombre_grupo_investigacion):
			self.nombre_grupo_investigacion = [nombre_grupo_investigacion]

		def get_clasificacion_grupo_investigacion(self):
			return self.clasificacion_grupo_investigacion
		
		def set_clasificacion_grupo_investigacion(self,clasificacion_grupo_investigacion):
			self.clasificacion_grupo_investigacion = [clasificacion_grupo_investigacion]
		
		def get_area_grupo_investigacion(self):
			return self.area_grupo_investigacion
		
		def set_area_grupo_investigacion(self,area_grupo_investigacion):
			self.area_grupo_investigacion = [area_grupo_investigacion]
		
		def get_correo_grupo_investigacion(self):
			return self.correo_grupo_investigacion
		
		def set_correo_grupo_investigacion(self,correo_grupo_investigacion):
			self.correo_grupo_investigacion = [correo_grupo_investigacion]


		def relation_gi_tiene_li(self,li):
			self.gi_tiene_li.append(li)



		def relation_gi_tiene_investigador(self,investigador):
			self.gi_tiene_investigador.append(investigador)



		def relation_gi_tiene_docente(self,docente):
			self.gi_tiene_docente.append(docente)


		def relation_gi_tiene_estudiante(self,estudiante):
			self.gi_tiene_estudiante.append(estudiante)

	#SUBCLASE LINEA DE INVESTIGACION
	class Linea_investigacion(Grupo_investigacion):
		
		def get_id_linea_investigacion(self):
			return self.id_linea_investigacion
		
		def set_id_linea_investigacion(self, id_linea_investigacion):
			self.id_linea_investigacion = [id_linea_investigacion]
		
		def get_nombre_linea_investigacion(self):
			return self.nombre_linea_investigacion
		
		def set_nombre_linea_investigacion(self, nombre_linea_investigacion):           
			self.nombre_linea_investigacion = [nombre_linea_investigacion]
		

		def relation_li_tiene_pi(self,pi):
			self.li_tiene_pi.append(pi)

		
	#CLASE INVESTIGADOR
	class Investigador(Thing):
		
		def get_id_investigador(self):
			return self.id_investigador

		def set_id_investigador(self,id_investigador):
			self.id_investigador = [id_investigador]



		def get_nombres_investigador(self):
			return self.nombres_investigador

		def set_nombres_investigador(self,nombres_investigador):
			self.nombres_investigador = [nombres_investigador]



		def get_apellidos_investigador(self):
			return self.apellidos_investigador

		def set_apellidos_investigador(self,apellidos_investigador):
			self.apellidos_investigador = [apellidos_investigador]
		


		def get_codigo_investigador(self):
			return self.codigo_investigador

		def set_codigo_investigador(self,codigo_investigador):
			self.codigo_investigador = [codigo_investigador]
		


		def get_cedula_investigador(self):
			return self.cedula_investigador

		def set_cedula_investigador(self,cedula_investigador):
			self.cedula_investigador = [cedula_investigador]
		


		def get_correo_investigador(self):
			return self.correo_investigador

		def set_correo_investigador(self,correo_investigador):
			self.correo_investigador = [correo_investigador]
	


		def relation_investigador_es_docente(self,docente):
			self.investigador_es_docente.append(docente)



		def relation_investigador_es_estudiante(self,estudiante):
			self.investigador_es_estudiante.append(estudiante)


		def relation_investigador_es_ie(self,ie):
			self.investigador_es_ie.append(ie)


	#SUBCLASE DOCENTE INVESTIGADOR
	class Docente(Investigador):

		def get_id_docente(self):
			return self.id_docente
		
		def set_id_docente(self, id_docente):            
			self.id_docente = [id_docente]


		def relation_docente_es_autor_pi(self,pi):
			self.docente_es_autor_pi.append(pi)


		def relation_docente_asesora_pi(self,pi):
			self.docente_asesora_pi.append(pi)
		

	#SUBCLASE ESTUDIANTE INVESTIGADOR
	class Estudiante(Investigador):

		def get_id_estudiante(self):
			return self.id_estudiante
		
		def set_id_estudiante(self, id_estudiante):            
			self.id_estudiante = [id_estudiante]

		def relation_estudiante_es_autor_pi(self,pi):
			self.estudiante_es_autor_pi.append(pi)
		
	#SUBCLASE INVESTIGADOR EXTERNO
	class Investigador_externo(Investigador):
		
		def get_id_investigador_externo(self):
			return self.id_investigador_externo
		
		def set_id_investigador_externo(self, id_investigador_externo):
			self.id_investigador_externo = [id_investigador_externo]

		def relation_ie_es_autor_pi(self,pi):
			self.ie_es_autor_pi.append(pi)			
		
		
	#CLASE PALABRA
	class Palabra(Thing):
		
		def get_id_palabra(self):
			return self.id_palabra

		def set_id_palabra(self,id_palabra):
			self.id_palabra = [id_palabra]


		def get_descripcion_palabra(self):
			return self.descripcion_palabra

		def set_descripcion_palabra(self,descripcion_palabra):
			self.descripcion_palabra = [descripcion_palabra]


		def get_lema_palabra(self):
			return self.lema_palabra

		def set_lema_palabra(self,lema_palabra):
			self.lema_palabra = [lema_palabra]



		def get_tipo_palabra(self):
			return self.tipo_palabra

		def set_tipo_palabra(self,tipo_palabra):
			self.tipo_palabra = [tipo_palabra]


		def get_concepto_palabra(self):
			return self.concepto_palabra

		def set_concepto_palabra(self,concepto_palabra):
			self.concepto_palabra = [concepto_palabra]


		def relation_palabra_sinonimo_palabra(self,palabra):
			self.palabra_sinonimo_palabra.append(palabra)


		def relation_palabra_conecta_palabra(self,palabra):
			self.palabra_conecta_palabra.append(palabra)




	#CLASE PROYECTO DE INVESTIGACION
	class Proyecto_investigacion(Thing):



		def get_id_proyecto_investigacion(self):
			return self.id_proyecto_investigacion

		def set_id_proyecto_investigacion(self, id_proyecto_investigacion):
			self.id_proyecto_investigacion = [id_proyecto_investigacion]		

		def get_titulo_proyecto_investigacion(self):
			return self.titulo_proyecto_investigacion

		def set_titulo_proyecto_investigacion(self, titulo_proyecto_investigacion):
			self.titulo_proyecto_investigacion = [titulo_proyecto_investigacion]			

		def get_resumen_proyecto_investigacion(self):
			return self.resumen_proyecto_investigacion

		def set_resumen_proyecto_investigacion(self, resumen_proyecto_investigacion):
			self.resumen_proyecto_investigacion = [resumen_proyecto_investigacion]			

		def get_estado_proyecto_investigacion(self):
			return self.estado_proyecto_investigacion

		def set_estado_proyecto_investigacion(self, estado_proyecto_investigacion):
			self.estado_proyecto_investigacion = [estado_proyecto_investigacion]			

		def get_tipo_proyecto_investigacion(self):
			return self.tipo_proyecto_investigacion

		def set_tipo_proyecto_investigacion(self, tipo_proyecto_investigacion):
			self.tipo_proyecto_investigacion = [tipo_proyecto_investigacion]			

		def get_palabras_clave(self):
			return self.palabras_clave

		def set_palabras_clave(self, palabras_clave):
			self.palabras_clave = [palabras_clave]


		def relation_pi_tiene_palabra(self,palabra):
			self.pi_tiene_palabra.append(palabra)



##FALTAN PALABRAS CLAVE OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##FALTAN PALABRAS CLAVE OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##FALTAN PALABRAS CLAVE OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##FALTAN PALABRAS CLAVE OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
##FALTAN PALABRAS CLAVE OJO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


	#CLASE UNIVERSIDAD
	class Universidad(Thing):
		
		def get_id_universidad(self):
			return self.id_universidad

		def set_id_universidad(self, id_universidad):        
			self.id_universidad = [id_universidad]

		def get_nombre_universidad(self):
			return self.nombre_universidad
		
		def set_nombre_universidad(self, nombre_universidad):            
			self.nombre_universidad = [nombre_universidad]

		def relation_universidad_tiene_facultad(self,facultad):
			self.universidad_tiene_facultad.append(facultad)

		def relation_universidad_tiene_viis(self,viis):
			self.universidad_tiene_viis.append(viis)
							

	#SUBCLASE FACULTAD
	class Facultad(Universidad):

		def get_id_facultad(self):
			return self.id_facultad

		def set_id_facultad(self, id_facultad):
			self.id_facultad = [id_facultad]

		def get_nombre_facultad(self):
			return self.nombre_facultad
		
		def set_nombre_facultad(self, nombre_facultad):
			self.nombre_facultad = [nombre_facultad]

		def relation_facultad_tiene_departamento(self,departamento):
			self.facultad_tiene_departamento.append(departamento)
		

	#SUBCLASE DEPARTAMENTO
	class Departamento(Facultad):

		def get_id_departamento(self):
			return self.id_departamento
		
		def set_id_departamento(self, id_departamento):
			self.id_departamento = [id_departamento]
		
		def get_nombre_departamento(self):
			return self.nombre_departamento		

		def set_nombre_departamento(self, nombre_departamento):
			self.nombre_departamento = [nombre_departamento]
		
		def relation_departamento_tiene_programa(self,programa):
			self.departamento_tiene_programa.append(programa)
   
		def relation_departamento_tiene_gi(self,gi):
			self.departamento_tiene_gi.append(gi)
	  
	#SUBCLASE PROGRAMA
	class Programa(Departamento):

		def get_id_programa(self):
			return self.id_programa		

		def set_id_programa(self, id_programa):
			self.id_programa = [id_programa]
		
		def get_nombre_programa(self):
			return self.nombre_programa   

		def set_nombre_programa(self, nombre_programa):
			self.nombre_programa = [nombre_programa]


		def relation_programa_tiene_estudiante(self,estudiante):
			self.programa_tiene_estudiante.append(estudiante)


		def relation_programa_tiene_docente(self,docente):
			self.programa_tiene_docente.append(docente)


	#CLASE VIIS
	class VIIS(Thing):
		
		def get_id_VIIS(self):
			return self.id_VIIS

		def set_id_VIIS(self, id_VIIS):
			self.id_VIIS = [id_VIIS]
		
		def get_nombre_VIIS(self):
			return self.nombre_VIIS

		def set_nombre_VIIS(self, nombre_VIIS):
			self.nombre_VIIS = [nombre_VIIS]
		
		def relation_viis_tiene_convocatoria(self,convocatoria):
			self.viis_tiene_convocatoria.append(convocatoria)

		def relation_viis_tiene_investigador(self,investigador):
			self.viis_tiene_investigador.append(investigador)

		def relation_viis_adscribe_gi(self,gi):
			self.viis_adscribe_gi.append(gi)

		def relation_viis_tiene_pi(self,pi):
			self.viis_tiene_pi.append(pi)


	#SUBCLASE CONVOCATORIA
	class Convocatoria(VIIS):

		def get_id_convocatoria(self):
			return self.id_convocatoria

		def set_id_convocatoria(self, id_convocatoria):
			self.id_convocatoria = [id_convocatoria]

		def get_nombre_convocatoria(self):
			return self.nombre_convocatoria

		def set_nombre_convocatoria(self, nombre_convocatoria):
			self.nombre_convocatoria = [nombre_convocatoria]

		def get_tipo_convocatoria(self):
			return self.tipo_convocatoria

		def set_tipo_convocatoria(self, tipo_convocatoria):
			self.tipo_convocatoria = [tipo_convocatoria]
		
		def get_anio_convocatoria(self):
			return self.anio_convocatoria

		def set_anio_convocatoria(self, anio_convocatoria):
			self.anio_convocatoria = [anio_convocatoria]
		
		def relation_convocatoria_tiene_pi(self,pi):
			self.convocatoria_tiene_pi.append(pi)

		def relation_convocatoria_dirigida_investigador(self,investigador):
			self.convocatoria_dirigida_investigador.append(investigador)





#############################################CREACION DE DATA PROPERTIES#################################################

#######################PARA SNIPPET#########################################


# with ontologia:


#     #Clase $1
#     class atributo (DataProperty):
#         domain = [$1]
#         range = [str]

######################################START###################################


with ontologia:

	#Clase Universidad
	class id_universidad (DataProperty):
		domain = [Universidad]
		range = [int]

	#Clase Universidad
	class nombre_universidad (DataProperty):
		domain = [Universidad]
		range = [str]



	#Clase Facultad
	class id_facultad (DataProperty):
		domain = [Facultad]
		range = [int]


	#Clase Facultad
	class nombre_facultad (DataProperty):
		domain = [Facultad]
		range = [str]



	#Clase Departamento
	class id_departamento (DataProperty):
		domain = [Departamento]
		range = [int]   


	#Clase Departamento
	class nombre_departamento (DataProperty):
		domain = [Departamento]
		range = [str]



	#Clase Programa
	class id_programa (DataProperty):
		domain = [Programa]
		range = [int]


	#Clase Programa
	class nombre_programa (DataProperty):
		domain = [Programa]
		range = [str]




	#Clase Docente
	class id_docente (DataProperty):
		domain = [Docente]
		range = [int]



	#Clase Estudiante
	class id_estudiante (DataProperty):
		domain = [Estudiante]
		range = [int]
		

	#Clase Grupo_investigacion
	class id_grupo_investigacion (DataProperty):
		domain = [Grupo_investigacion]
		range = [int]
		

	#Clase Grupo_investigacion
	class nombre_grupo_investigacion (DataProperty):
		domain = [Grupo_investigacion]
		range = [str]


	#Clase Grupo_investigacion
	class clasificacion_grupo_investigacion (DataProperty):
		domain = [Grupo_investigacion]
		range = [str]


	#Clase Grupo_investigacion
	class area_grupo_investigacion (DataProperty):
		domain = [Grupo_investigacion]
		range = [str]



	#Clase Grupo_investigacion
	class correo_grupo_investigacion (DataProperty):
		domain = [Grupo_investigacion]
		range = [str]




	#Clase Linea_investigacion
	class id_linea_investigacion (DataProperty):
		domain = [Linea_investigacion]
		range = [int]


	#Clase Linea_investigacion
	class nombre_linea_investigacion(DataProperty):
		domain = [Linea_investigacion]
		range = [str]



	#Clase VIIS
	class id_VIIS(DataProperty):
		domain = [VIIS]
		range = [str]


	#Clase VIIS
	class nombre_VIIS(DataProperty):
		domain = [VIIS]
		range = [str]


	#Clase Convocatoria
	class id_convocatoria(DataProperty):
		domain = [Convocatoria]
		range = [int]


	#Clase Convocatoria
	class nombre_convocatoria(DataProperty):
		domain = [Convocatoria]
		range = [str]


	#Clase Convocatoria
	class anio_convocatoria(DataProperty):
		domain = [Convocatoria]
		range = [int]


	#Clase Convocatoria
	class tipo_convocatoria(DataProperty):
		domain = [Convocatoria]
		range = [str]



	#Clase Proyecto_investigacion
	class id_proyecto_investigacion (DataProperty):
		domain = [Proyecto_investigacion]
		range = [int]



	#Clase Proyecto_investigacion
	class titulo_proyecto_investigacion (DataProperty):
		domain = [Proyecto_investigacion]
		range = [str]



	#Clase Proyecto_investigacion
	class resumen_proyecto_investigacion (DataProperty):
		domain = [Proyecto_investigacion]
		range = [str]



	#Clase Proyecto_investigacion
	class palabra_clave1 (DataProperty):
		domain = [Proyecto_investigacion]
		range = [str]



	#Clase Proyecto_investigacion
	class palabra_clave2 (DataProperty):
		domain = [Proyecto_investigacion]
		range = [str]



	#Clase Proyecto_investigacion
	class palabra_clave3 (DataProperty):
		domain = [Proyecto_investigacion]
		range = [str]



	#Clase Proyecto_investigacion
	class palabra_clave4 (DataProperty):
		domain = [Proyecto_investigacion]
		range = [str]



	#Clase Proyecto_investigacion
	class palabra_clave5 (DataProperty):
		domain = [Proyecto_investigacion]
		range = [str]                



	#Clase Proyecto_investigacion
	class estado_proyecto_investigacion (DataProperty):
		domain = [Proyecto_investigacion]
		range = [str]



	#Clase Proyecto_investigacion
	class tipo_proyecto_investigacion (DataProperty):
		domain = [Proyecto_investigacion]
		range = [str]



	#Clase Investigador
	class id_investigador (DataProperty):
		domain = [Investigador]
		range = [int]


	#Clase Investigador
	class nombres_investigador (DataProperty):
		domain = [Investigador]
		range = [str]


	#Clase Investigador
	class apellidos_investigador (DataProperty):
		domain = [Investigador]
		range = [str]


	#Clase Investigador
	class codigo_investigador (DataProperty):
		domain = [Investigador]
		range = [str]


	#Clase Investigador
	class cedula_investigador (DataProperty):
		domain = [Investigador]
		range = [str]


	#Clase Investigador
	class correo_investigador (DataProperty):
		domain = [Investigador]
		range = [str]



	#Clase Palabra
	class id_palabra(DataProperty):
		domain = [Palabra]
		range = [int]


	#Clase Palabra
	class descripcion_palabra (DataProperty):
		domain = [Palabra]
		range = [str]


	#Clase Palabra
	class lema_palabra (DataProperty):
		domain = [Palabra]
		range = [str]


	#Clase Palabra
	class tipo_palabra (DataProperty):
		domain = [Palabra]
		range = [str]


	#Clase Palabra
	class concepto_palabra (DataProperty):
		domain = [Palabra]
		range = [str]


	#Clase Investigador_externo
	class id_investigador_externo(DataProperty):
		domain = [Investigador_externo]
		range = [str]

#############################################CREACION DE OBJECT PROPERTIES#################################################



#######################PARA SNIPPET#########################################

# with ontologia:
# 	class $1 (ObjectProperty):
# 		domain = [$2]
# 		range = [$3]
# 		inverse_property = $4

# 	class $4 (ObjectProperty):
# 		domain = [$3]
# 		range = [$2]
# 		inverse_property = $1

# #Metodo $2
# 	def relation_$1(self,$5)
# 		self.$1.append($5)

# #Metodo $3
# 	def relation_$4(self,$6)
# 		self.$4.append($6)

######################################START###################################

"""

with ontologia:
	class universidad_tiene_facultad (ObjectProperty):
		domain = [Universidad]
		range = [Facultad]
		inverse_property = facultad_pertenece_universidad

	class facultad_pertenece_universidad (ObjectProperty):
		domain = [Facultad]
		range = [Universidad]
		inverse_property = universidad_tiene_facultad

	#Metodo Universidad
	def relation_universidad_tiene_facultad(self,facultad):
		self.universidad_tiene_facultad.append(facultad)

	#Metodo Facultad
	def relation_facultad_pertenece_universidad(self,universidad):
		self.facultad_pertenece_universidad.append(universidad)






#OP
	class universidad_tiene_viis (ObjectProperty):
		domain = [Universidad]
		range = [VIIS]
		inverse_property = viis_pertenece_universidad

	class viis_pertenece_universidad (ObjectProperty):
		domain = [VIIS]
		range = [Universidad]
		inverse_property = universidad_tiene_viis

	#Metodo Universidad
	def relation_universidad_tiene_viis(self,viis):
		self.universidad_tiene_viis.append(viis)

	#Metodo VIIS
	def relation_viis_pertenece_universidad(self,universidad):
		self.viis_pertenece_universidad.append(universidad)










#OP
	class facultad_tiene_departamento (ObjectProperty):
		domain = [Facultad]
		range = [Departamento]
		inverse_property = departamento_pertenece_facultad

	class departamento_pertenece_facultad (ObjectProperty):
		domain = [Departamento]
		range = [Facultad]
		inverse_property = facultad_tiene_departamento

	#Metodo Facultad
	def relation_facultad_tiene_departamento(self,departamento):
		self.facultad_tiene_departamento.append(departamento)

	#Metodo Departamento
	def relation_departamento_pertenece_facultad(self,facultad):
		self.departamento_pertenece_facultad.append(facultad)












#OP
	class departamento_tiene_programa (ObjectProperty):
		domain = [Departamento]
		range = [Programa]
		inverse_property = programa_pertenece_departamento

	class programa_pertenece_departamento (ObjectProperty):
		domain = [Programa]
		range = [Departamento]
		inverse_property = departamento_tiene_programa

	#Metodo Departamento
	def relation_departamento_tiene_programa(self,programa):
		self.departamento_tiene_programa.append(programa)

	#Metodo Programa
	def relation_programa_pertenece_departamento(self,departamento):
		self.programa_pertenece_departamento.append(departamento)







#OP
	class departamento_tiene_gi (ObjectProperty):
		domain = [Departamento]
		range = [Grupo_investigacion]
		inverse_property = gi_pertenece_departamento

	class gi_pertenece_departamento (ObjectProperty):
		domain = [Grupo_investigacion]
		range = [Departamento]
		inverse_property = departamento_tiene_gi

	#Metodo Departamento
	def relation_departamento_tiene_gi(self,gi):
		self.departamento_tiene_gi.append(gi)

	#Metodo Grupo_investigacion
	def relation_gi_pertenece_departamento(self,departamento):
		self.gi_pertenece_departamento.append(departamento)








#OP
	class programa_tiene_estudiante (ObjectProperty):
		domain = [Programa]
		range = [Estudiante]
		inverse_property = estudiante_pertenece_programa

	class estudiante_pertenece_programa (ObjectProperty):
		domain = [Estudiante]
		range = [Programa]
		inverse_property = programa_tiene_estudiante

	#Metodo Programa
	def relation_programa_tiene_estudiante(self,estudiante):
		self.programa_tiene_estudiante.append(estudiante)

	#Metodo Estudiante
	def relation_estudiante_pertenece_programa(self,programa):
		self.estudiante_pertenece_programa.append(programa)









#OP
	class programa_tiene_docente (ObjectProperty):
		domain = [Programa]
		range = [Docente]
		inverse_property = docente_pertenece_programa

	class docente_pertenece_programa (ObjectProperty):
		domain = [Docente]
		range = [Programa]
		inverse_property = programa_tiene_docente

	#Metodo Programa
	def relation_programa_tiene_docente(self,docente):
		self.programa_tiene_docente.append(docente)

	#Metodo Docente
	def relation_docente_pertenece_programa(self,programa):
		self.docente_pertenece_programa.append(programa)








#OP
	class gi_tiene_li (ObjectProperty):
		domain = [Grupo_investigacion]
		range = [Linea_investigacion]
		inverse_property = li_pertenece_gi

	class li_pertenece_gi (ObjectProperty):
		domain = [Linea_investigacion]
		range = [Grupo_investigacion]
		inverse_property = gi_tiene_li

	#Metodo Grupo_investigacion
	def relation_gi_tiene_li(self,li):
		self.gi_tiene_li.append(li)

	#Metodo Linea_investigacion
	def relation_li_pertenece_gi(self,gi):
		self.li_pertenece_gi.append(gi)








#OP
	class gi_tiene_investigador (ObjectProperty):
		domain = [Grupo_investigacion]
		range = [Investigador]
		inverse_property = investigador_pertenece_gi

	class investigador_pertenece_gi (ObjectProperty):
		domain = [Investigador]
		range = [Grupo_investigacion]
		inverse_property = gi_tiene_investigador

	#Metodo Grupo_investigacion
	def relation_gi_tiene_investigador(self,investigador):
		self.gi_tiene_investigador.append(investigador)

	#Metodo Investigador
	def relation_investigador_pertenece_gi(self,gi):
		self.investigador_pertenece_gi.append(gi)








#OP
	class gi_tiene_docente (ObjectProperty):
		domain = [Grupo_investigacion]
		range = [Docente]
		inverse_property = docente_pertenece_gi

	class docente_pertenece_gi (ObjectProperty):
		domain = [Docente]
		range = [Grupo_investigacion]
		inverse_property = gi_tiene_docente

	#Metodo Grupo_investigacion
	def relation_gi_tiene_docente(self,docente):
		self.gi_tiene_docente.append(docente)

	#Metodo Docente
	def relation_docente_pertenece_gi(self,gi):
		self.docente_pertenece_gi.append(gi)








#OP
	class gi_tiene_estudiante (ObjectProperty):
		domain = [Grupo_investigacion]
		range = [Estudiante]
		inverse_property = estudiante_pertenece_gi

	class estudiante_pertenece_gi (ObjectProperty):
		domain = [Estudiante]
		range = [Grupo_investigacion]
		inverse_property = gi_tiene_estudiante

	#Metodo Grupo_investigacion
	def relation_gi_tiene_estudiante(self,estudiante):
		self.gi_tiene_estudiante.append(estudiante)

	#Metodo Estudiante
	def relation_estudiante_pertenece_gi(self,gi):
		self.estudiante_pertenece_gi.append(gi)









#OP
	class li_tiene_pi (ObjectProperty):
		domain = [Linea_investigacion]
		range = [Proyecto_investigacion]
		inverse_property = pi_pertenece_li

	class pi_pertenece_li (ObjectProperty):
		domain = [Proyecto_investigacion]
		range = [Linea_investigacion]
		inverse_property = li_tiene_pi

	#Metodo Linea_investigacion
	def relation_li_tiene_pi(self,pi):
		self.li_tiene_pi.append(pi)

	#Metodo Proyecto_investigacion
	def relation_pi_pertenece_li(self,li):
		self.pi_pertenece_li.append(li)









#OP
	class viis_tiene_convocatoria (ObjectProperty):
		domain = [VIIS]
		range = [Convocatoria]
		inverse_property = convocatoria_pertenece_viis

	class convocatoria_pertenece_viis (ObjectProperty):
		domain = [Convocatoria]
		range = [VIIS]
		inverse_property = viis_tiene_convocatoria

	#Metodo VIIS
	def relation_viis_tiene_convocatoria(self,convocatoria):
		self.viis_tiene_convocatoria.append(convocatoria)

	#Metodo Convocatoria
	def relation_convocatoria_pertenece_viis(self,viis):
		self.convocatoria_pertenece_viis.append(viis)









#OP
	class viis_tiene_investigador (ObjectProperty):
		domain = [VIIS]
		range = [Investigador]
		inverse_property = investigador_pertenece_viis

	class investigador_pertenece_viis (ObjectProperty):
		domain = [Investigador]
		range = [VIIS]
		inverse_property = viis_tiene_investigador

	#Metodo VIIS
	def relation_viis_tiene_investigador(self,investigador):
		self.viis_tiene_investigador.append(investigador)

	#Metodo Investigador
	def relation_investigador_pertenece_viis(self,viis):
		self.investigador_pertenece_viis.append(viis)









#OP
	class viis_adscribe_gi (ObjectProperty):
		domain = [VIIS]
		range = [Grupo_investigacion]
		inverse_property = gi_esta_adscrito_viis

	class gi_esta_adscrito_viis (ObjectProperty):
		domain = [Grupo_investigacion]
		range = [VIIS]
		inverse_property = viis_adscribe_gi

	#Metodo VIIS
	def relation_viis_adscribe_gi(self,gi):
		self.viis_adscribe_gi.append(gi)

	#Metodo Grupo_investigacion
	def relation_gi_esta_adscrito_viis(self,viis):
		self.gi_esta_adscrito_viis.append(viis)









#OP
	class viis_tiene_pi (ObjectProperty):
		domain = [VIIS]
		range = [Proyecto_investigacion]
		inverse_property = pi_pertenece_viis

	class pi_pertenece_viis (ObjectProperty):
		domain = [Proyecto_investigacion]
		range = [VIIS]
		inverse_property = viis_tiene_pi

	#Metodo VIIS
	def relation_viis_tiene_pi(self,pi):
		self.viis_tiene_pi.append(pi)

	#Metodo Proyecto_investigacion
	def relation_pi_pertenece_viis(self,viis):
		self.pi_pertenece_viis.append(viis)


	
	
	
	
	
	
#OP
	class convocatoria_tiene_pi (ObjectProperty):
		domain = [Convocatoria]
		range = [Proyecto_investigacion]
		inverse_property = pi_pertenece_convocatoria

	class pi_pertenece_convocatoria (ObjectProperty):
		domain = [Proyecto_investigacion]
		range = [Convocatoria]
		inverse_property = convocatoria_tiene_pi

	#Metodo Convocatoria
	def relation_convocatoria_tiene_pi(self,pi):
		self.convocatoria_tiene_pi.append(pi)

	#Metodo Proyecto_investigacion
	def relation_pi_pertenece_convocatoria(self,convocatoria):
		self.pi_pertenece_convocatoria.append(convocatoria)








#OP
	class convocatoria_dirigida_investigador (ObjectProperty):
		domain = [Convocatoria]
		range = [Investigador]
		inverse_property = investigador_se_encuentra_convocatoria

	class investigador_se_encuentra_convocatoria (ObjectProperty):
		domain = [Investigador]
		range = [Convocatoria]
		inverse_property = convocatoria_dirigida_investigador

	#Metodo Convocatoria
	def relation_convocatoria_dirigida_investigador(self,investigador):
		self.convocatoria_dirigida_investigador.append(investigador)

	#Metodo Investigador
	def relation_investigador_se_encuentra_convocatoria(self,convocatoria):
		self.investigador_se_encuentra_convocatoria.append(convocatoria)








#OP
	class estudiante_es_autor_pi (ObjectProperty):
		domain = [Estudiante]
		range = [Proyecto_investigacion]
		inverse_property = pi_tiene_autor_estudiante

	class pi_tiene_autor_estudiante (ObjectProperty):
		domain = [Proyecto_investigacion]
		range = [Estudiante]
		inverse_property = estudiante_es_autor_pi

	#Metodo Estudiante
	def relation_estudiante_es_autor_pi(self,pi):
		self.estudiante_es_autor_pi.append(pi)

	#Metodo Proyecto_investigacion
	def relation_pi_tiene_autor_estudiante(self,estudiante):
		self.pi_tiene_autor_estudiante.append(estudiante)


		
		
		
		
		
		
#OP
	class docente_es_autor_pi (ObjectProperty):
		domain = [Docente]
		range = [Proyecto_investigacion]
		inverse_property = pi_tiene_autor_docente

	class pi_tiene_autor_docente (ObjectProperty):
		domain = [Proyecto_investigacion]
		range = [Docente]
		inverse_property = docente_es_autor_pi

	#Metodo Docente
	def relation_docente_es_autor_pi(self,pi):
		self.docente_es_autor_pi.append(pi)

	#Metodo Proyecto_investigacion
	def relation_pi_tiene_autor_docente(self,docente):
		self.pi_tiene_autor_docente.append(docente)


		
		
		
		
		

#OP
	class docente_asesora_pi (ObjectProperty):
		domain = [Docente]
		range = [Proyecto_investigacion]
		inverse_property = pi_es_asesorado_docente

	class pi_es_asesorado_docente (ObjectProperty):
		domain = [Proyecto_investigacion]
		range = [Docente]
		inverse_property = docente_asesora_pi

	#Metodo Docente
	def relation_docente_asesora_pi(self,pi):
		self.docente_asesora_pi.append(pi)

	#Metodo Proyecto_investigacion
	def relation_pi_es_asesorado_docente(self,docente):
		self.pi_es_asesorado_docente.append(docente)



#OP

	class ie_es_autor_pi(ObjectProperty):
		domain = [Investigador_externo]
		range = [Proyecto_investigacion]
		inverse_propety = pi_tiene_autor_ie

	class pi_tiene_autor_ie(ObjectProperty):
		domain = [Proyecto_investigacion]
		range = [Investigador_externo]
		inverse_propety = ie_es_autor_pi


	#Metodo Investigador_externo
	def relation_ie_es_autor_pi(self,pi):
		self.ie_es_autor_pi.append(pi)

	#Metodo Proyecto_investigación
	def relation_pi_tiene_autor_ie(self,ie):
		self.pi_tiene_autor_ie.append(ie)



#OP
	class investigador_es_docente (ObjectProperty):
		domain = [Investigador]
		range = [Docente]
		inverse_property = docente_es_investigador

	class docente_es_investigador (ObjectProperty):
		domain = [Docente]
		range = [Investigador]
		inverse_property = investigador_es_docente

	#Metodo Investigador
	def relation_investigador_es_docente(self,docente):
		self.investigador_es_docente.append(docente)

	#Metodo Docente
	def relation_docente_es_investigador(self,investigador):
		self.docente_es_investigador.append(investigador)




	
	
	
	
	
	
#OP
	class investigador_es_estudiante (ObjectProperty):
		domain = [Investigador]
		range = [Estudiante]
		inverse_property = estudiante_es_investigador

	class estudiante_es_investigador (ObjectProperty):
		domain = [Estudiante]
		range = [Investigador]
		inverse_property = investigador_es_estudiante

	#Metodo Investigador
	def relation_investigador_es_estudiante(self,estudiante):
		self.investigador_es_estudiante.append(estudiante)

	#Metodo Estudiante
	def relation_estudiante_es_investigador(self,investigador):
		self.estudiante_es_investigador.append(investigador)
			








#OP
	class investigador_es_ie (ObjectProperty):
		domain = [Investigador]
		range = [Investigador_externo]
		inverse_property = ie_es_investigador

	class ie_es_investigador (ObjectProperty):
		domain = [Investigador_externo]
		range = [Investigador]
		inverse_property = investigador_es_ie

	#Metodo Investigador
	def relation_investigador_es_ie(self,ie):
		self.investigador_es_ie.append(ie)

	#Metodo Investigador_externo
	def relation_ie_es_investigador(self,investigador):
		self.ie_es_investigador.append(investigador)




#OP
	class palabra_sinonimo_palabra (ObjectProperty):
		domain = [Palabra]
		range = [Palabra]
		inverse_property = palabra_sinonimo_palabra


	#Metodo Palabra
	def relation_palabra_sinonimo_palabra(self,palabra):
		self.palabra_sinonimo_palabra.append(palabra)





#OP
	class palabra_conecta_palabra (ObjectProperty):
		domain = [Palabra]
		range = [Palabra]
		inverse_property = palabra_conecta_palabra


	#Metodo Palabra
	def relation_palabra_conecta_palabra(self,palabra):
		self.palabra_conecta_palabra.append(palabra)






###SE ESTA PROBANDO POR AHORA CON ESTE OP

#OP
class pi_tiene_palabra(ObjectProperty):
	domain = [Proyecto_investigacion]
	range = [Palabra]

class palabra_describe_pi(ObjectProperty):
	domain = [Palabra]
	range = [Proyecto_investigacion]
	inverse_property = pi_tiene_palabra


	#Metodo Proyecto_investigacion
	def relation_pi_tiene_palabra(self,palabra):
		self.pi_tiene_palabra.append(palabra)

	#Metodo Palabra
	def relation_palabra_describe_pi(self,pi):
		self.palabra_describe_pi.append(pi)
"""