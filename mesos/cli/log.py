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

import functools
import logging
import sys
import time

debug = logging.debug


def fatal(msg, code=1):
    sys.stdout.write(msg + "\n")
    logging.error(msg)
    sys.exit(code)


def fn(f, *args, **kwargs):
    logging.debug("{0}: {1} {2}".format(repr(f), args, kwargs))
    return f(*args, **kwargs)


def duration(fn):
    @functools.wraps(fn)
    def timer(*args, **kwargs):
        start = time.time()
        try:
            return fn(*args, **kwargs)
        finally:
            debug("duration: {0}.{1}: {2:2.2f}s".format(
                fn.__module__,
                fn.__name__,
                time.time() - start))

    return timer
