from os import startfile
from os import system
import os
import shutil
import xml.etree.ElementTree as ET
from controller.GraphvizMatrixParser import GraphvizMatrixParser
from controller.Simulation import Simulation


class Report():

    REPORT_PATH = './reports/'

    def __init__(self, register):
        Report.generateAllReports(register)

    @staticmethod
    def generateAllReports(patients):
        return Report.generateXmlReport(patients)

    @staticmethod
    def generateGravizReport(history, name):

        try:
            for i in range(0, history.lenght):
                GraphvizMatrixParser(history.getElement(i), i)

            print('generando dot completo')

            system('cd dot && type *.dot | gvpack -u -o output.dot')
            system(
                f'cd dot && dot -Tpng ./output.dot -o ../historial{name}.png')
            startfile(f'historial{name}.png')

            # * Delete files
            # system(f'cd dot && del *.*')
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

            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def generateXmlReport(patients):

        try:

            xmlDoc = ET.Element('pacientes')
            FILE_NAME = 'reporte.xml'

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
