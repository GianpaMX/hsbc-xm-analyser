import xml.etree.ElementTree

class Analyser(object):
    def __init__(self, config):
        self.fieldnames = []
        self.config = config
        self.result = []
        self.ns = {
            'cfdi': 'http://www.sat.gob.mx/cfd/3',
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital',
            'DG': 'http://www.hsbc.com.mx/schema/DG'
        }

    def analyse(self, fileName):
        root = xml.etree.ElementTree.parse(fileName).getroot()
        rows = root.findall('./cfdi:Addenda/DG:DatosGenerales/DG:Movimientos', self.ns)[0]
        for row in rows.findall('DG:MovimientosDelCliente', self.ns):
            pass

        for row in rows.findall('DG:MovimientoDelClienteFiscal', self.ns):
            rfc = row.attrib['RFCenajenante']
            category = self.config.categoryByRFC[rfc] if rfc in self.config.categoryByRFC else 'undefined'
            amount = float(row.attrib['importe'])

            row = {
                'date': row.attrib['fecha'][:10],
                'description': row.attrib['descripcion'],
                'placeId': rfc,
                'amount': amount,
                'category': category
            }
            self.result.append(row)

            if len(self.fieldnames) == 0:
                self.fieldnames = row.keys()
