# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ExportToGE
                                 A QGIS plugin
 Sends polygons, lines, points, and multi-part geometries to Google Earth
                             -------------------
        begin                : 2017-06-06
        copyright            : (C) 2017 by Wei-an V. Hung
        email                : huntboy320@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ExportToGE class from file ExportToGE.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Export_To_GE import ExportToGE
    return ExportToGE(iface)
