# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2020 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import logging

from shapely.wkt import loads

from pygeoapi.provider.xarray_ import XarrayProvider

LOGGER = logging.getLogger(__name__)


class EDRProvider(XarrayProvider):
    """EDR Provider"""

    def __init__(self, provider_def):
        """
        Initialize object

        :param provider_def: provider definition

        :returns: pygeoapi.provider.rasterio_.RasterioProvider
        """

        XarrayProvider.__init__(self, provider_def)

    def get_fields(self):
        """
        Get provider field information (names, types)

        :returns: dict of dicts of parameters
        """

        return self.get_coverage_rangetype()

    def get_query_types(self):
        """
        Provide supported query types

        :returns: list of EDR query types
        """

        return ['position', 'area']

    def query(self, **kwargs):
        """
        Extract data from collection collection

        :param wkt: str of WKT geometry
        :param datetime_: temporal (datestamp or extent)
        :param select_properties: list of parameters
        :param z: vertical level(s)
        :param format_: data format of output

        :returns: coverage data as dict of CoverageJSON or native format
        """

        if kwargs.get('wkt') is not None:
            LOGGER.debug('Transforming WKT into GeoJSON dict')
            geojson_dict = loads(kwargs['wkt']).__geo_interface__

        return {'foo': 'bar'}
