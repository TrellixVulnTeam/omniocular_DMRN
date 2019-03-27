import os

import models.diff_string.args


def get_args():
    parser = models.diff_string.args.get_args()

    parser.add_argument('--dataset', type=str, default='VulasDiff', choices=['VulasDiff'])
    parser.add_argument('--mode', type=str, default='multichannel', choices=['rand', 'static', 'non-static', 'multichannel'])
    parser.add_argument('--output-channel', type=int, default=100)
    parser.add_argument('--words-dim', type=int, default=300)
    parser.add_argument('--embed-dim', type=int, default=300)
    parser.add_argument('--epoch-decay', type=int, default=15)
    parser.add_argument('--weight-decay', type=float, default=0)

    parser.add_argument('--dropout', type=float, default=0.5)
    parser.add_argument('--dropblock', type=float, default=0.0)
    parser.add_argument('--dropblock-size', type=int, default=7)
    parser.add_argument('--beta-ema', type=float, default=0, help="for temporal averaging")
    parser.add_argument('--embed-droprate', type=float, default=0.0, help="for embedded droupout")
    parser.add_argument('--batchnorm', action='store_true')
    parser.add_argument('--dynamic-pool', action='store_true')
    parser.add_argument('--attention', action='store_true')
    parser.add_argument('--bottleneck-units', type=int, default=100)
    parser.add_argument('--dynamic-pool-length', type=int, default=8)
    parser.add_argument('--bottleneck-layer', action='store_true')

    parser.add_argument('--word-vectors-dir', default=os.path.join(os.pardir, 'omniocular-data', 'embeddings', 'word2vec'))
    parser.add_argument('--word-vectors-file', default='GoogleNews-vectors-negative300.txt')
    parser.add_argument('--save-path', type=str, default=os.path.join('reg_cnn', 'saves'))
    parser.add_argument('--resume-snapshot', type=str)
    parser.add_argument('--trained-model', type=str)

    args = parser.parse_args()
    return args