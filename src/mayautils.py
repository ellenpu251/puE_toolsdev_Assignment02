import logging
import os
import maya.cmds as cmds

import pymel.core as pmc
from pymel.core.system import Path

from pymel.core.system import versions

log = logging.getLogger(__name__)

def main():
    increment = 0
    while(increment<3):
        if increment >= 10:
            break
        cubexform, cubeshape = pmc.polyCube()
        cubexform.translateT.set(1.5*increment)
        increment+=1

class SceneFile(object):
    def __init__(self, dir="", descriptor='main', version=1, ext="ma"):
        FilePath = cmds.file(q=True, sn=True)
        if(FilePath==""):
            self._dir = Path(dir)
            self.descriptor = descriptor
            self.version = version
            self.ext = ext
        else:
            parts = os.path.split(FilePath)
            self._dir = parts[0]
            Name = parts[1].split('_v')
            self.descriptor = Name[0]
            Split2 = Name[1].split('.')
            self.version = int(Split2[0])
            self.ext = Split2[1]

    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self,val):
        self._dir=Path(val)

    def basename(self):
        name_pattern = "{descriptor}.{version:03d}.{ext}"
        name = name_pattern.format(descriptor=self.descriptor, version=self.version, ext=self.ext)
        return name

    def path(self):
        return Path(self.dir) / self.basename()

    def save(self):
        try:
            Path = self.dir + "\\" + self.descriptor + '_v0' + str(self.version) + '.' +self.ext
            pmc.system.saveAs(Path)
        except RuntimeError:
            log.warning("Missing directories.creating directories")
            self.dir.markedirs_p()
            Path = self.dir + "\\" + self.descriptor + '_v0' + str(self.version) + '.' + self.ext
            pmc.system.saveAs(Path)

    def increment_and_save(self):
        CurrentVersion = self.version
        for i in self.dir.files('*.ma'):
            parts = os.path.split(i)
            Directory = parts[0]
            Name = parts[1].split('_v')
            Descriptor = Name[0]
            Split2 = Name[1].split('.')
            Version = int(Split2[0])
            Extension = Split2[1]
            if(self.descriptor == Descriptor):
                if CurrentVersion < Version:
                    CurrentVersion = Version
                CurrentVersion = CurrentVersion + 1
                Path = self.dir + "\\" + self.descriptor + '_v0' + str(CurrentVersion) + '.' + self.ext
                pmc.system.saveAs(Path)

