from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic

from usuarios.models import Usuario

from ciclo_phva.models import (
    ItemEstandar,
    Phva,
)
from django.contrib.auth.mixins import LoginRequiredMixin

# Importaciones de libreria para generar reportes
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side


class ExcelDetailView(generic.ListView, LoginRequiredMixin):
    item = Usuario
    context_object_name = 'usuario'
    template_name = 'usuarios/tortal_administrador.html'

    def get(self, request, *args, **kwargs):
        item_estandar:(ItemEstandar) = ItemEstandar.objects.all()
        phva:(Phva) = Phva.objects.get(id=1)
        # Abrir flujo de edición de datos
        wb = Workbook()
        ws = wb.active
        contador:(int) = 2
        # Encabezados
        #ws["A" + '1'].alignment = Alignment(horizontal='left')
        ws['A' + '1'] = 'Ciclo'
        ws.alignment = Alignment(horizontal='left')   
        ws['B' + '1'] = 'Estandar'
        ws['D' + '1'] = 'Item de estandar'
        ws['E' + '1'] = 'Valor maximo'
        ws['F' + '1'] = 'Peso porcentual'
        ws['G' + '1'] = 'Puntaje obtenido'
        # Ciclos
        ws['A' + '2'] = 'Planear'
        ws.merge_cells('A2:A23')
        ws['A' + '24'] = 'Hacer'
        ws.merge_cells('A24:A53')
        ws['A' + '54'] = 'Verificar'
        ws.merge_cells('A54:A57')
        ws['A' + '58'] = 'Actuar'
        ws.merge_cells('A58:A61')
        #Estandares
        ws['B' + '2'] = 'Recursos'
        ws.merge_cells('B2:B12')
        ws['B' + '13'] = 'Gestion integral del sistema de gestion de la seguridad y salud en el trabajo'
        ws.merge_cells('B13:B23')
        ws['B' + '24'] = 'Gestion de la salud'
        ws.merge_cells('B24:B41')
        ws['B' + '24'] = 'Gestion de peligros y riesgos'
        ws.merge_cells('B42:B51')
        ws['B' + '52'] = 'Gestion de amenazas'
        ws.merge_cells('B52:B53')
        ws['B' + '54'] = 'Verificacion del SG-SST'
        ws.merge_cells('B54:B57')
        ws['B' + '58'] = 'Mejoramiento'
        ws.merge_cells('B58:B61')
        # Sub estandares
        ws['C' + '2'] = 'Recursos financieros, técnicos humanos y de otra índole requeridos para coordinar y desarrollar el Sistema de Gestion de la Seguridad y Salud en el Trabajo (SG-SST)'
        ws.merge_cells('C2:C9')
        ws['C' + '10'] = 'Capacitación en el Sistema de Gestión de Seguridad y Salud en el Trabajo'
        ws.merge_cells('C10:C12')
        ws['C' + '13'] = 'Política de Seguridad y Salud en el Trabajo'
        ws['C' + '14'] = 'Objetivos del Sistema de Gestión de la Seguridad y la Salud en el Trabajo SG-SST'
        ws['C' + '15'] = 'Evaluación inicial del SG-SST '
        ws['C' + '16'] = 'Plan Anual de Trabajo'
        ws['C' + '17'] = 'Conservación de la documentación'
        ws['C' + '18'] = 'Rendición de cuentas'
        ws['C' + '19'] = 'Normatividad nacional vigente y aplicable en materia de seguridad y salud en el trabajo'
        ws['C' + '20'] = 'Comunicación'
        ws['C' + '21'] = 'Adquisiciones'
        ws['C' + '22'] = 'Contratación'
        ws['C' + '23'] = 'Gestión del cambio'
        ws['C' + '24'] = 'Condiciones de salud en el trabajo'
        ws.merge_cells('C24:C32')
        ws['C' + '33'] = 'Registro, reporte e investigación de las enfermedades laborales, los incidentes y accidentes del trabajo'
        ws.merge_cells('C33:C35')
        ws['C' + '36'] = 'Mecanismos de vigilancia de las condiciones de salud de los trabajadores '
        ws.merge_cells('C36:C41')
        ws['C' + '42'] = 'Identificación de peligros, evaluación y valoración de riesgos'
        ws.merge_cells('C42:C45')
        ws['C' + '46'] = 'Medidas de prevención y control para intervenir los peligros/riesgos'
        ws.merge_cells('C46:C51')
        ws['C' + '52'] = 'Plan de prevención, preparación y respuesta ante emergencias'
        ws.merge_cells('C52:C53')
        ws['C' + '54'] = 'Gestión y resultados del SG-SST'
        ws.merge_cells('C54:C57')
        ws['C' + '58'] = 'Acciones preventivas y correctivas con base en los resultados del SG-SST'
        ws.merge_cells('C58:C61')
        # Peso porcentual
        ws['F' + '2'] = '4'
        ws.merge_cells('F2:F9')
        ws['F' + '10'] = '6'
        ws.merge_cells('F10:F12')
        ws['F' + '13'] = '15'
        ws.merge_cells('F13:F23')
        ws['F' + '24'] = '9'
        ws.merge_cells('F24:F32')
        ws['F' + '33'] = '5'
        ws.merge_cells('F33:F35')
        ws['F' + '36'] = '6'
        ws.merge_cells('F36:F41')
        ws['F' + '42'] = '15'
        ws.merge_cells('F42:F45')
        ws['F' + '46'] = '15'
        ws.merge_cells('F46:F51')
        ws['F' + '52'] = '10'
        ws.merge_cells('F52:F53')
        ws['F' + '54'] = '5'
        ws.merge_cells('F54:F57')
        ws['F' + '58'] = '10'
        ws.merge_cells('F58:F61')
        # Item de estandar
        for q in item_estandar:
            column = str(contador) 
            ws['D' + column] = q.descripcion
            ws['E'+ column] = q.puntaje_maximo
            ws['G'+ column] = q.puntaje_obtenido
            contador += 1

        # Calculo de phva
        column = str(contador) 
        ws['F'+ column] = 'Total'
        ws['G'+ column] = phva.calificacion_obtenida
        
        # ws.merge_cells('A1:A9')
        ws.merge_cells('B1:C1')
        nombre_archivo:(str) = "ListadoPhva.xlsx"
        # Response HTTP
        response = HttpResponse(content_type="application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        # Ciclo de escritura terminado
        wb.save(response)
        # Retornar el response
        return response
