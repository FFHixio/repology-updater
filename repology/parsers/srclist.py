# Copyright (C) 2016-2018 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

import rpm

from repology.package import Package
from repology.util import GetMaintainers


class SrcListParser():
    def __init__(self):
        pass

    def Parse(self, path):
        result = []

        for header in rpm.readHeaderListFromFile(path):
            fields = {
                key: str(header[key], 'utf-8')
                for key in ['name', 'version', 'release', 'packager', 'group', 'summary']
            }

            pkg = Package()

            pkg.name = fields['name']
            pkg.version = fields['version']  # XXX: handle release
            pkg.maintainers = GetMaintainers(fields['packager'])  # XXX: may have multiple maintainers
            pkg.category = fields['group']
            pkg.comment = fields['summary']

            result.append(pkg)

        return result
