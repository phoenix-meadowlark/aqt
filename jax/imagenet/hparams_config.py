"""Contains the hparams class used for ResNet."""

import dataclasses
import typing
from typing import Any

from google3.third_party.google_research.google_research.aqt.jax.flax import struct as flax_struct
from google3.third_party.google_research.google_research.aqt.utils import hparams_utils

dataclass = flax_struct.dataclass if not typing.TYPE_CHECKING else dataclasses.dataclass


@dataclass
class LrScheduler:
  warmup_epochs: int
  cooldown_epochs: int
  scheduler: str
  num_epochs: int
  endlr: float
  knee_lr: float
  knee_epochs: int


@dataclass
class Adam:
  beta1: float
  beta2: float


@dataclass
class TrainingHParams:
  """Hyperparameters used for training."""

  # Metadata
  metadata: hparams_utils.HParamsMetadata

  # General hparams
  base_learning_rate: float
  momentum: float  # only used when optimier=='sgd'
  weight_decay: float
  lr_scheduler: LrScheduler
  optimizer: str
  adam: Adam  # only used when optimizer=='adam'
  early_stop_steps: int
  teacher_model: str
  is_teacher: bool
  seed: int

  # Auto-clip activation quantization hparams. See
  # train_utils.should_update_bounds for more details. We use -1 instead of None
  # to indicate that these parameters should be inactive since if these
  # attributes are marked as optional, Dacite will set them to None even if
  # they are missing from the JSON-serialized version of this dataclass, while
  # we want Dacite to raise an error in this case to alert users about an
  # incomplete configuration.
  activation_bound_update_freq: int
  activation_bound_start_step: int
  weight_quant_start_step: int

  # Model hparams
  model_hparams: Any