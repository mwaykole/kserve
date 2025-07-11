# Copyright 2024 The KServe Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Global context management for KServe model server configuration."""

import contextvars
from typing import Optional

from .predictor_config import PredictorConfig

# Global context variable for predictor configuration
_predictor_config_var: contextvars.ContextVar[Optional[PredictorConfig]] = (
    contextvars.ContextVar("predictor_config", default=None)
)


def set_predictor_config(config: PredictorConfig) -> None:
    """Set the predictor configuration for the current context.

    This should be called once during ModelServer initialization.

    Args:
        config: The PredictorConfig instance to set
    """
    _predictor_config_var.set(config)


def get_predictor_config() -> Optional[PredictorConfig]:
    """Get the predictor configuration from the current context.

    Returns:
        The PredictorConfig instance if set, None otherwise
    """
    return _predictor_config_var.get()
