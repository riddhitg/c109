import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

dice_result = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)

mean = sum(dice_result)/len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)

print("mean of the data is {}".format(mean))
print("mode of the data is {}".format(mode))
print("median of the data is {}".format(median))
print("standard deviation of the data is {}".format(std_deviation))

first_std_deviation_start, first_std_deviation_end = mean-std_deviation,mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

list_of_data_within_one_standard_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_two_standard_deviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_three_standard_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]

print("{}% of data lies within one standard deviation".format(len(list_of_data_within_one_standard_deviation)*100.0/len(dice_result)))
print("{}% of data lies within two standard deviation".format(len(list_of_data_within_two_standard_deviation)*100.0/len(dice_result)))
print("{}% of data lies within three standard deviation".format(len(list_of_data_within_three_standard_deviation)*100.0/len(dice_result)))

fig = ff.create_distplot([dice_result],["Result"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [first_std_deviation_start, first_std_deviation_start], y = [0,0.17], mode = "lines", name = "standard deviation 1 start"))
fig.add_trace(go.Scatter(x = [first_std_deviation_end, first_std_deviation_end], y = [0,0.17], mode = "lines", name = "standard deviation 1 end"))
fig.add_trace(go.Scatter(x = [second_std_deviation_start, second_std_deviation_start], y = [0,0.17], mode = "lines", name = "standard deviation 2 start"))
fig.add_trace(go.Scatter(x = [second_std_deviation_end, second_std_deviation_end], y = [0,0.17], mode = "lines", name = "standard deviation 2 end"))
fig.add_trace(go.Scatter(x = [third_std_deviation_start, third_std_deviation_start], y = [0,0.17], mode = "lines", name = "standard deviation 3 start"))
fig.add_trace(go.Scatter(x = [third_std_deviation_end, third_std_deviation_end], y = [0,0.17], mode = "lines", name = "standard deviation 3 end"))

fig.show()