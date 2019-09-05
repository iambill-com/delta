# Copyright (C) 2017 Beijing Didi Infinity Technology and Development Co.,Ltd.
# All rights reserved.
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
# ==============================================================================
"""hparam test."""

import tensorflow as tf

from hparam import HParams


class HParamsTest(tf.test.TestCase):
  ''' HParams unittest '''

  def test_hparams(self):
    hparams = HParams(name='fbank', n_mels=40)
    self.assertEqual(hparams.name, 'fbank')
    self.assertEqual(hparams.n_mels, 40)
    self.assertDictEqual(hparams.values(), {'name': 'fbank', 'n_mels': 40})

    hparams.add_hparam('sr', 8000)
    self.assertEqual(hparams.sr, 8000)

    hparams.set_hparam('sr', 16000)
    self.assertEqual(hparams.sr, 16000)
    self.assertEqual(hparams.get('sr'), 16000)

    hparams.del_hparam('sr')
    self.assertJsonEqual(hparams.to_json(), '{"name": "fbank", "n_mels": 40}')

if __name__ == '__main__':
  tf.test.main()