#!/usr/bin/env python
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


class AtumException(Exception):
    pass


class DuplicateDataException(AtumException):
    """Raise duplicate data exception"""
    pass


class UnknownObjectException(AtumException):
    """Raise unknown object exception"""
    pass


class JSONDecodeError(AtumException):
    pass


class APIResponseError(AtumException):
    pass


class UnknownProviderException(AtumException):
    pass


class IllegalArgumentError(ValueError):
    pass


class APIRequestError(AtumException):
    pass


class AtumProvisionerException(AtumException):
    pass


class InvalidObjectException(AtumProvisionerException):
    pass


class OperationFailedException(AtumProvisionerException):
    pass


class InvalidAuthException(AtumProvisionerException):
    pass
