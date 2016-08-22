import os
import logging
import attr
import re
from attr.validators import instance_of
from qcauto import Geometry
from qcauto.templates import TontoRobyBondIndex
from qcauto.jobs.runners import NullRunner
log = logging.getLogger(__name__)


@attr.s
class TontoRobyBondIndexJob(object):
    geometry = attr.ib(validator=instance_of(Geometry))
    _runner = attr.ib(default=NullRunner())
    basis_set = attr.ib(default="3-21G")
    method = attr.ib(default="HF")
    fchk = attr.ib(default="test.fchk")
    name = attr.ib(default='tonto_job', validator=instance_of(str))
    template = attr.ib(default=TontoRobyBondIndex)
    _input_file = attr.ib('stdin')
    _output_file = attr.ib('stdout')
    success = attr.ib(default=False)

    def write_input_file(self, filename):
        log.debug("Writing input file to {}".format(filename))
        with open(filename, 'w') as f:
            f.write(self.template.render(job=self, geom=self.geometry))

    def before_run(self):
        file_basename = self.name + self.method + self.basis_set
        self._input_file = file_basename + self.input_ext
        self._output_file = file_basename + self.output_ext
        self.write_input_file(self._input_file)

    def args(self):
        return [self._input_file]

    def after_run(self):
        if self.success:
            self._result = self.extract_energy(self._output_file) 

    def result(self):
        return self._result

    def extract_tonto_energy(filename):
        with open(filename) as f:
            for line in f:
                if 'Total energy' in line:
                    return float(re.findall('[-+]\d+[\.]?\d*', line)[0])
