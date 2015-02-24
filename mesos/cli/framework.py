# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from __future__ import absolute_import, print_function

class Framework(object):
    def __init__(self, items):
        self.__items = items

    def __getitem__(self, name):
        return self.__items[name]

    def __str__(self):
        return "{0}:{1}".format(self.name, self.id)

    @property
    def id(self):
        return self['id']

    @property
    def name(self):
        return self['name']

    @property
    def hostname(self):
        return self['hostname']

    @property
    def active(self):
        return self['active']

    @property
    def task_count(self):
        return len(self['tasks'])

    @property
    def user(self):
        return self['user']

    @property
    def cpu_allocated(self):
        return self._resource_allocated("cpus")

    @property
    def cpu_used(self):
        return self._resource_used("cpus")

    @property
    def mem_allocated(self):
        return self._resource_allocated("mem")

    @property
    def mem_used(self):
        return self._resource_used("mem")

    @property
    def disk_allocated(self):
        return self._resource_allocated("disk")

    @property
    def disk_used(self):
        return self._resource_used("disk")

    def _resource_used(self, resource):
        return self["used_resources"][resource]

    def _resource_allocated(self, resource):
        return self["resources"][resource]
