from controller.PatientRegister import PatientRegister
import xml.dom.minidom
from data.doublyLinkedListWithIndex import DoublyLinkedListWithIndex

from data.matrix import SquareMatrix


class Register(object):

    patients = DoublyLinkedListWithIndex()

    def __init__(self, xmlDocumentPath):
        Register.loadData(xmlDocumentPath)

    @staticmethod
    def loadData(xmlDocumentPath):
        try:
            domTree = xml.dom.minidom.parse(xmlDocumentPath)
            group = domTree.documentElement

            patients = group.getElementsByTagName('paciente')

            for patient in patients:
                # Personal Data
                name = patient.getElementsByTagName(
                    'nombre')[0].childNodes[0].nodeValue
                age = patient.getElementsByTagName(
                    'edad')[0].childNodes[0].nodeValue
                periods = patient.getElementsByTagName(
                    'periodos')[0].childNodes[0].nodeValue
                cellDimension = patient.getElementsByTagName(
                    'm')[0].childNodes[0].nodeValue

                # Genereate Matrix
                matrix = SquareMatrix(int(cellDimension))

                cells = patient.getElementsByTagName('celda')

                for cell in cells:
                    row = int(cell.getAttribute('f'))
                    col = int(cell.getAttribute('c'))
                    matrix.setElement(row, col, True)

                # Create register
                patientRegister = PatientRegister(name, age, periods,
                                                  cellDimension, matrix)
                Register.patients.insertAtEnd(patientRegister)

            return {"ok": True, "msg": "Información cargada correctamente"}

        except Exception as e:
            print(e)
            return {"ok": False, "msg": "Error al cargar el archivo"}

    @staticmethod
    def cleanRegisters():
        Register.patients = DoublyLinkedListWithIndex()
