from Functions.DataPreprocessingFuncs import *

Data = "AAPLmax"
sample_size = 200
threshold = 1
Noise = 0  # Coefficient of noise. Possible values are integers from 0 to 5 inclusive
Trend = 0  # Trend with 0 corresponding to no trend, 1 corresponding to linear, and 2 corresponding to quadratic

# path = "Results/" + Data + "/" + str(sample_size) + "/" + str(threshold) + "/"
path = "C:\Code\CVQC\src\Results\AAPLmax\\200\\1\\"

dataset = load_data(
    # "Datasets/" + Data + ".csv", usecols=["Close"], sample_size=sample_size
    r'C:/Code/CVQC/src/Datasets/AAPLmax.csv',  # Use forward slashes or double backslashes
    usecols=["Close"],
    sample_size=sample_size
)

percent_of_change = gradient(dataset)

# Provide load_PSD = path if there exists already a file with the power spectral density. Otherwise specify the parameters 'signal' and 'threshold' and provide parameter save_components = path.
DC, amp, N = find_components(load_PSD=path)


full_signal, r = build_signal(
    DC, amp, Noise, Trend, N, bool_plot=False, labels=["Title", "X-axis", "Y-axis"]
)
