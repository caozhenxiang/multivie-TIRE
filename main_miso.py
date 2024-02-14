from functions import utils, data_loader
from functions import evaluation
import os
import warnings
import numpy as np
warnings.filterwarnings("ignore")

# --------------------------- #
# SET PARAMETERS
seed = np.random.randint(0, 1e8, size=1).tolist()[0]
generate_data = False
architecture = 'TIRE_miso'
dataset = "JM-SV0"                   # mean0-9, var0-9, gauss0-9, ar0-9, hasc, bee_dance0-5, ..., if generate_data = False
enable_eval_plot = True
enable_model_summary = False
nfft = 30
norm_mode = "timeseries"   # for calculation of DFT, should the timeseries have mean zero or each window?

# --------------------------- #
# BEGINNING OF CODE
# load data and model
window_size, threshold = utils.set_windowsize_and_threshold(dataset)
time_series, windows_TD, windows_FD, parameters = data_loader.data_parse(nfft, norm_mode, generate_data, dataset, window_size)

if len(time_series.shape) == 1:
    time_series = np.expand_dims(time_series, axis=-1)
    windows_TD = np.expand_dims(windows_TD, axis=-1)
    windows_FD = np.expand_dims(windows_FD, axis=-1)

windows_both = np.concatenate((windows_TD, windows_FD), axis=1)

network = utils.load_architecture(architecture)
path = os.path.join(os.path.abspath(os.getcwd()), "results")

#---------------------------#
##TRAIN THE AUTOENCODERS
shared_features_both = network.train_model(windows_both, enable_summary=enable_model_summary, window_size=window_size,
                                           seed=seed)
dissimilarities = evaluation.smoothened_dissimilarity_measures(shared_features_both, None, "TD", window_size)
print("Both Domain TIRE:")
evaluation.show_result(generate_data, window_size, dissimilarities, parameters, threshold, enable_eval_plot)
