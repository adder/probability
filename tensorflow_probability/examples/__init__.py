# Copyright 2018 The TensorFlow Probability Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Example implementations of common models."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tensorflow_probability.examples import bayesian_neural_network
from tensorflow_probability.examples import logistic_regression
from tensorflow_probability.examples import vae

from tensorflow.python.util.all_util import remove_undocumented

_allowed_symbols = [
    "bayesian_neural_network",
    "logistic_regression",
    "vae",
]

remove_undocumented(__name__, _allowed_symbols)
