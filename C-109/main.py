import pandas as pd 
import csv
import plotly.express as px
import statistics
import plotly.figure_factory as ff
df = pd.read_csv("height-weight.csv")
height=df["Height(Inches)"].tolist()
weight = df["Weight(Pounds)"].tolist()
heightmean=statistics.mean(height)
weightmean = statistics.mean(weight)
heightmedian = statistics.median(height)
weightmedian = statistics.median(weight)
heightmode = statistics.mode(height)
weightmode = statistics.mode(weight)
print("mean,median,mode of height is: {}, {} and {} respectively".format(heightmean,heightmedian,heightmode))
print("mean,median,mode of weight is: {}, {} and {} respectively".format(weightmean,weightmedian,weightmode))
heightstd=statistics.stdev(height)
weightstd = statistics.stdev(weight)
fig=ff.create_distplot([height],["height"],show_hist=False)
height1stdstart,height1stdend = heightmean-heightstd,heightmean+heightstd
height2stdstart,height2stdend = heightmean-(2*heightstd),heightmedian+(2*heightstd)
height3stdstart,height3stdend = heightmean-(3*heightstd),heightmedian+(3*heightstd)
weight1stdstart,weight1stdend = weightmean-weightstd,weightmean+weightstd
weight2stdstart,weight2stdend = weightmean-(2*weightstd),weightmean+(2*weightstd)
weight3stdstart,weight3stdend = weightmean-(3*weightstd),weightmean+(3*heightstd)
heightdatawithin1std=[result for result in height if result>height1stdstart and result<height1stdend]
heightdatawithin2std=[result for result in height if result>height2stdstart and result<height2stdend]
heightdatawithin3std=[result for result in height if result>height3stdstart and result<height3stdend]
weightdatawithin1std=[result for result in weight if result>weight1stdstart and result<weight1stdend]
weightdatawithin2std=[result for result in weight if result>weight2stdstart and result<weight2stdend]
weightdatawithin3std=[result for result in weight if result>weight3stdstart and result<weight3stdend]
print("{}% of data for height lies within 1st standard deviation".format(len(heightdatawithin1std)*100/len(height)))
print("{}% of data for height lies within 2nd standard deviation".format(len(heightdatawithin2std)*100/len(height)))
print("{}% of data for height lies within 3rd standard deviation".format(len(heightdatawithin3std)*100/len(height)))
print("{}% of data for weight lies within 1st standard deviation".format(len(weightdatawithin1std)*100/len(weight)))
print("{}% of data for weight lies within 2nd standard deviation".format(len(weightdatawithin2std)*100/len(weight)))
print("{}% of data for weight lies within 3rd standard deviation".format(len(weightdatawithin3std)*100/len(weight)))