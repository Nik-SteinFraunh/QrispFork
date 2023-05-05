"""
/*********************************************************************
* Copyright (c) 2023 the Qrisp Authors
*
* This program and the accompanying materials are made
* available under the terms of the Eclipse Public License 2.0
* which is available at https://www.eclipse.org/legal/epl-2.0/
*
* SPDX-License-Identifier: EPL-2.0
**********************************************************************/
"""

"""
    Cyqlone-Backend Interface

    An API specification for interfacing the high-level language Cyqlone to backend providers.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.qubit import Qubit

globals()["Qubit"] = Qubit
from openapi_client.model.connectivity_edge import ConnectivityEdge


class TestConnectivityEdge(unittest.TestCase):
    """ConnectivityEdge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConnectivityEdge(self):
        """Test ConnectivityEdge"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ConnectivityEdge()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
