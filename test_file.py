import numpy

target_list = numpy.array(['1','b','c','d','e','f','g','h','i','j'])
to_exclude = [1,4,5]
print target_list[~numpy.in1d(range(len(target_list)),to_exclude)]