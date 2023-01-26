import bag.core
import argparse

from bag.core import BagProject

parser = argparse.ArgumentParser(description='Import schematic view to BAG from given library and cell name.')
parser.add_argument('lib_name', help='Library name.')
parser.add_argument('cell_name', help='Cell name.')

args = parser.parse_args()

prj = BagProject()

prj.import_sch_cellview(args.lib_name, args.cell_name)