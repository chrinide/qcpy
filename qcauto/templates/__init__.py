import os
import logging
from jinja2 import Environment, FileSystemLoader

log = logging.getLogger(__name__)
_env = Environment(loader=FileSystemLoader(os.path.dirname(os.path.abspath(__file__))))

GaussianSinglePointEnergy = _env.get_template('gaussian_spe.template')
TontoDFTSinglePointEnergy = _env.get_template('tonto_dft.template')
TontoRobyBondIndex = _env.get_template('tonto_roby.template')
GaussianWaveFunction = _env.get_template('gaussian_wave.template')
EmptyTemplate = _env.get_template('empty.template')