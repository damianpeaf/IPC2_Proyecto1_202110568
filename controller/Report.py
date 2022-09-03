from os import startfile
from os import system
import os
import shutil
import xml.etree.ElementTree as ET
from controller.GraphvizMatrixParser import GraphvizMatrixParser
from controller.PatientRegister import PatientRegister
from controller.Simulation import Simulation
from data.doublyLinkedListWithIndex import DoublyLinkedListWithIndex


class Report():

    REPORT_PATH = './reports/'

    def __init__(self, register):
        Report.generateAllReports(register)

    @staticmethod
    def generateAllReports(patients: DoublyLinkedListWithIndex):

        try:
            # Generate xml report
            Report.generateXmlReport(patients, "ReporteGeneralDePacientes.xml")

            # Generate graphviz report for each patient register
            for i in range(0, patients.lenght):
                patient = patients.getElement(i)
                simulation = Simulation(patient)
                simulation.runAllStates()
                Report.generateGravizReport(simulation.history, patient.name)

            return True
        except:
            return False

    def generateIndividualReport(patientRegister: PatientRegister):

        try:
            # Graphviz Report
            simulation = Simulation(patientRegister)
            simulation.runAllStates()
            Report.generateGravizReport(
                simulation.history, patientRegister.name)

            # XML report
            patientList = DoublyLinkedListWithIndex()
            patientList.insertAtEnd(patientRegister)
            Report.generateXmlReport(
                patientList, f'Reporte{patientRegister.name}.xml')

            return True
        except:
            return False

    @staticmethod
    def generateGravizReport(history, name):

        try:
            GraphvizMatrixParser(history, name)

            pdfName = f'historial{name}.pdf'

            system(
                f'cd dot && dot -Tpdf ./historial{name}.dot -o ../reports/{pdfName}')

            filePath = os.path.join(os.getcwd(), 'reports', pdfName)

            startfile(filePath)

            os.pardir

            # * Delete files
            folder = 'dot'
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                file_name, file_extension = os.path.splitext(file_path)

                if file_extension == '.md':
                    continue

                if os.path.isfile(file_path) or os.path.islink(file_path):

                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            print('Borrando archivos dot')

            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def generateXmlReport(patients: DoublyLinkedListWithIndex, FILE_NAME: str):
        try:

            xmlDoc = ET.Element('pacientes')

            for i in range(0, patients.lenght):
                patient = patients.getElement(i)

                patientSimulation = Simulation(patient)
                # * Run all the simulation again
                patientSimulation.runAllStates()

                patientTag = ET.SubElement(xmlDoc, 'paciente')
                datosPersonalesTag = ET.SubElement(patientTag,
                                                   'datospersonales')

                # * Name
                ET.SubElement(datosPersonalesTag, 'nombre').text = patient.name
                # * Age
                ET.SubElement(datosPersonalesTag, 'edad').text = patient.age

                # * Rest of the info

                ET.SubElement(patientTag, 'periodos').text = patient.periods
                ET.SubElement(patientTag, 'm').text = patient.cellDimension

                # * Result
                ET.SubElement(patientTag,
                              'resultado').text = patientSimulation.diseaseType

                # * Aditional Disease info

                if patientSimulation.diseaseType == 'mortal' or patientSimulation.diseaseType == 'grave':
                    if patientSimulation.initialStatePatternDetected:
                        ET.SubElement(patientTag, 'n').text = str(
                            patientSimulation.initialStatePatternPeriod)
                    else:
                        ET.SubElement(patientTag, 'n').text = str(
                            patientSimulation.laterStatePatternOcurrence)
                        ET.SubElement(patientTag, 'n1').text = str(
                            patientSimulation.laterStatePatternPeriod)

            tree = ET.ElementTree(xmlDoc)

            tree.write(Report.REPORT_PATH + FILE_NAME,
                       encoding='UTF-8',
                       xml_declaration=True)

            return True

        except Exception as e:
            print(e)
            return False
