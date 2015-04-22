# Copyright Google Inc. 2010 All Rights Reserved
# licensed under Apache 2.0

# modified to extract elevation data points, don't need to use their chart api

import math
import simplejson
import urllib

ELEVATION_BASE_URL = 'http://maps.google.com/maps/api/elevation/json'
CHART_BASE_URL = 'http://chart.googleapis.com/chart'

def getChart(chartData, chartDataScaling="-500,5000", chartType="lc",chartLabel="Elevation in Meters",chartSize="500x160", chartColor="orange", **chart_args):
    chart_args.update({
        'cht': chartType,
        'chs': chartSize,
        'chl': chartLabel,
        'chco': chartColor,
        'chds': chartDataScaling,
        'chxt': 'x,y',
        'chxr': '1,-500,5000'
    })

    dataString = 't:' + ','.join(str(x) for x in chartData)
    chart_args['chd'] = dataString.strip(',')

    chartUrl = CHART_BASE_URL + '?' + urllib.urlencode(chart_args)

    print("")
    print("Elevation Chart URL:")
    print("")
    print chartUrl

raw_lat_long = [(37.3932, -121.9513), (37.3932, -121.9512), (37.393500000000003, -121.95059999999999), (37.393599999999999, -121.9504), (37.393700000000003, -121.9503), (37.393700000000003, -121.9503), (37.394100000000002, -121.95059999999999), (37.394500000000001, -121.9508), (37.394799999999996, -121.9511), (37.395299999999999, -121.95140000000001), (37.395600000000002, -121.9517), (37.395800000000001, -121.95200000000001), (37.396099999999997, -121.9525), (37.3962, -121.95310000000001), (37.396299999999997, -121.9537), (37.396299999999997, -121.95440000000001), (37.396099999999997, -121.9551), (37.395899999999997, -121.95569999999999), (37.395600000000002, -121.9562), (37.395400000000002, -121.9568), (37.395299999999999, -121.9569), (37.395299999999999, -121.9571), (37.395400000000002, -121.9572), (37.395499999999998, -121.95740000000001), (37.395400000000002, -121.9576), (37.395400000000002, -121.9577), (37.394300000000001, -122.07689999999999), (37.394300000000001, -122.0771), (37.394300000000001, -122.0771), (37.394399999999997, -122.0774), (37.394399999999997, -122.0774), (37.3947, -122.07810000000001), (37.3947, -122.07810000000001), (37.394799999999996, -122.0782), (37.394799999999996, -122.0782), (37.395000000000003, -122.0782), (37.395000000000003, -122.0782), (37.395299999999999, -122.0779), (37.395299999999999, -122.0779), (37.395299999999999, -122.0779), (37.395299999999999, -122.0779), (37.395400000000002, -122.07769999999999), (37.395400000000002, -122.07769999999999), (37.395400000000002, -122.0776), (37.395400000000002, -122.0776), (37.395099999999999, -122.07700000000001), (37.395099999999999, -122.07700000000001), (37.3949, -122.07640000000001), (37.3949, -122.07640000000001), (37.3947, -122.0758), (37.3947, -122.0758), (37.394199999999998, -122.0746), (37.394199999999998, -122.0746), (37.393799999999999, -122.0736), (37.393799999999999, -122.0736), (37.3934, -122.0727), (37.3934, -122.0727), (37.393000000000001, -122.07170000000001), (37.393000000000001, -122.07170000000001), (37.392800000000001, -122.0711), (37.392800000000001, -122.0711), (37.392400000000002, -122.0702), (37.392400000000002, -122.0702), (37.392099999999999, -122.0697), (37.392099999999999, -122.0697), (37.392099999999999, -122.06959999999999), (37.392099999999999, -122.06959999999999), (37.3919, -122.06910000000001), (37.3919, -122.06910000000001), (37.391599999999997, -122.0684), (37.391599999999997, -122.0684), (37.391399999999997, -122.0677), (37.391399999999997, -122.0677), (37.391199999999998, -122.0673), (37.391199999999998, -122.0673), (37.390900000000002, -122.0665), (37.390900000000002, -122.0665), (37.390500000000003, -122.0656), (37.390500000000003, -122.0656), (37.390000000000001, -122.0643), (37.390000000000001, -122.0643), (37.389600000000002, -122.06319999999999), (37.389600000000002, -122.06319999999999), (37.389400000000002, -122.0629), (37.389400000000002, -122.0629), (37.389099999999999, -122.06200000000001), (37.389099999999999, -122.06200000000001), (37.3889, -122.0615), (37.3889, -122.0615), (37.3887, -122.0607), (37.3887, -122.0607), (37.388399999999997, -122.0599), (37.388399999999997, -122.0599), (37.388100000000001, -122.05880000000001), (37.388100000000001, -122.05880000000001), (37.387700000000002, -122.0577), (37.387700000000002, -122.0577), (37.387599999999999, -122.0573), (37.387599999999999, -122.0573), (37.3872, -122.0562), (37.3872, -122.0562), (37.386899999999997, -122.0552), (37.386899999999997, -122.0552), (37.386800000000001, -122.0549), (37.386800000000001, -122.0549), (37.386499999999998, -122.054), (37.386499999999998, -122.054), (37.386200000000002, -122.0531), (37.386200000000002, -122.0531), (37.385899999999999, -122.0521), (37.385899999999999, -122.0521), (37.385800000000003, -122.0515), (37.385800000000003, -122.0515), (37.3857, -122.0508), (37.3857, -122.0508), (37.385599999999997, -122.0501), (37.385599999999997, -122.0501), (37.3857, -122.04949999999999), (37.3857, -122.04949999999999), (37.385800000000003, -122.0488), (37.385800000000003, -122.0488), (37.385999999999996, -122.0483), (37.385999999999996, -122.0483), (37.386200000000002, -122.04730000000001), (37.386200000000002, -122.04730000000001), (37.386400000000002, -122.0466), (37.386400000000002, -122.0466), (37.386499999999998, -122.0462), (37.386499999999998, -122.0462), (37.386699999999998, -122.0455), (37.386699999999998, -122.0455), (37.386800000000001, -122.0448), (37.386800000000001, -122.0448), (37.386800000000001, -122.04430000000001), (37.386800000000001, -122.04430000000001), (37.386699999999998, -122.0436), (37.386699999999998, -122.0436), (37.386499999999998, -122.0428), (37.386499999999998, -122.0428), (37.386299999999999, -122.0416), (37.386299999999999, -122.0416), (37.386099999999999, -122.0407), (37.386099999999999, -122.0407), (37.385899999999999, -122.0399), (37.385899999999999, -122.0399), (37.3857, -122.0389), (37.3857, -122.0389), (37.385599999999997, -122.0382), (37.385599999999997, -122.0382), (37.385399999999997, -122.0371), (37.385399999999997, -122.0371), (37.385199999999998, -122.0363), (37.385199999999998, -122.0363), (37.384999999999998, -122.03530000000001), (37.384999999999998, -122.03530000000001), (37.384700000000002, -122.03440000000001), (37.384700000000002, -122.03440000000001), (37.384500000000003, -122.0335), (37.384500000000003, -122.0335), (37.384500000000003, -122.0333), (37.384500000000003, -122.0333), (37.3842, -122.0324), (37.3842, -122.0324), (37.384099999999997, -122.0318), (37.384099999999997, -122.0318), (37.383899999999997, -122.03060000000001), (37.383899999999997, -122.03060000000001), (37.383600000000001, -122.0296), (37.383600000000001, -122.0296), (37.383400000000002, -122.0286), (37.383400000000002, -122.0286), (37.383200000000002, -122.0275), (37.383200000000002, -122.0275), (37.383000000000003, -122.02670000000001), (37.383000000000003, -122.02670000000001), (37.382899999999999, -122.02600000000001), (37.382899999999999, -122.02600000000001), (37.3827, -122.02500000000001), (37.3827, -122.02500000000001), (37.3825, -122.0243), (37.3825, -122.0243), (37.382300000000001, -122.0231), (37.382300000000001, -122.0231), (37.382100000000001, -122.0226), (37.382100000000001, -122.0226), (37.381999999999998, -122.0218), (37.381999999999998, -122.0218), (37.381799999999998, -122.0213), (37.381799999999998, -122.0213), (37.381399999999999, -122.0204), (37.381399999999999, -122.0204), (37.381300000000003, -122.0201), (37.381300000000003, -122.0201), (37.380699999999997, -122.01909999999999), (37.380699999999997, -122.01909999999999), (37.380400000000002, -122.0187), (37.380400000000002, -122.0187), (37.380000000000003, -122.01819999999999), (37.380000000000003, -122.01819999999999), (37.3797, -122.0176), (37.3797, -122.0176), (37.3795, -122.01700000000001), (37.3795, -122.01700000000001), (37.379199999999997, -122.0163), (37.379199999999997, -122.0163), (37.379199999999997, -122.0162), (37.379199999999997, -122.0162), (37.378999999999998, -122.0157), (37.378999999999998, -122.0157), (37.378799999999998, -122.01479999999999), (37.378799999999998, -122.01479999999999), (37.378500000000003, -122.0141), (37.378500000000003, -122.0141), (37.378300000000003, -122.01349999999999), (37.378300000000003, -122.01349999999999), (37.3782, -122.01309999999999), (37.3782, -122.01309999999999), (37.378, -122.0124), (37.378, -122.0124), (37.377899999999997, -122.012), (37.377899999999997, -122.012), (37.377699999999997, -122.01139999999999), (37.377699999999997, -122.01139999999999), (37.377400000000002, -122.01049999999999), (37.377400000000002, -122.01049999999999), (37.376999999999995, -122.0093), (37.376999999999995, -122.0093), (37.376800000000003, -122.0087), (37.376800000000003, -122.0087), (37.376600000000003, -122.00790000000001), (37.376600000000003, -122.00790000000001), (37.3765, -122.00709999999999), (37.3765, -122.00709999999999), (37.3765, -122.006), (37.3765, -122.006), (37.3765, -122.00530000000001), (37.3765, -122.00530000000001), (37.376600000000003, -122.0047), (37.376600000000003, -122.0047), (37.376800000000003, -122.00399999999999), (37.376800000000003, -122.00399999999999), (37.377099999999999, -122.00299999999999), (37.377099999999999, -122.00299999999999), (37.377400000000002, -122.0021), (37.377400000000002, -122.0021), (37.377499999999998, -122.0012), (37.377499999999998, -122.0012), (37.377499999999998, -122.0003), (37.377499999999998, -122.0003), (37.377499999999998, -121.9992), (37.377499999999998, -121.9992), (37.377499999999998, -121.99799999999999), (37.377499999999998, -121.99799999999999), (37.377600000000001, -121.99700000000001), (37.377600000000001, -121.99700000000001), (37.377600000000001, -121.99639999999999), (37.377600000000001, -121.99639999999999), (37.377600000000001, -121.9957), (37.377600000000001, -121.9957), (37.377600000000001, -121.995), (37.377600000000001, -121.995), (37.377499999999998, -121.99420000000001), (37.377499999999998, -121.99420000000001), (37.377600000000001, -121.99339999999999), (37.377600000000001, -121.99339999999999), (37.377600000000001, -121.9924), (37.377600000000001, -121.9924), (37.377600000000001, -121.99160000000001), (37.377600000000001, -121.99160000000001), (37.377600000000001, -121.991), (37.377600000000001, -121.991), (37.377600000000001, -121.98990000000001), (37.377600000000001, -121.98990000000001), (37.377600000000001, -121.98899999999999), (37.377600000000001, -121.98899999999999), (37.377600000000001, -121.9883), (37.377600000000001, -121.9883), (37.377600000000001, -121.9881), (37.377600000000001, -121.9881), (37.377600000000001, -121.9877), (37.377600000000001, -121.9877), (37.377600000000001, -121.9871), (37.377600000000001, -121.9871), (37.377600000000001, -121.9863), (37.377600000000001, -121.9863), (37.377600000000001, -121.9853), (37.377600000000001, -121.9853), (37.377600000000001, -121.9843), (37.377600000000001, -121.9843), (37.377600000000001, -121.98299999999999), (37.377600000000001, -121.98299999999999), (37.377600000000001, -121.98200000000001), (37.377600000000001, -121.98200000000001), (37.377600000000001, -121.9812), (37.377600000000001, -121.9812), (37.377499999999998, -121.9806), (37.377499999999998, -121.9806), (37.377299999999998, -121.98009999999999), (37.377299999999998, -121.98009999999999), (37.376999999999995, -121.97969999999999), (37.376999999999995, -121.97969999999999), (37.376600000000003, -121.9791), (37.376600000000003, -121.9791), (37.376300000000001, -121.9786), (37.376300000000001, -121.9786), (37.375799999999998, -121.97790000000001), (37.375799999999998, -121.97790000000001), (37.375300000000003, -121.9772), (37.375300000000003, -121.9772), (37.374899999999997, -121.9765), (37.374899999999997, -121.9765), (37.374600000000001, -121.976), (37.374600000000001, -121.976), (37.374400000000001, -121.97539999999999), (37.374400000000001, -121.97539999999999), (37.374400000000001, -121.9748), (37.374400000000001, -121.9748), (37.374400000000001, -121.9738), (37.374400000000001, -121.9738), (37.374400000000001, -121.9727), (37.374400000000001, -121.9727), (37.374400000000001, -121.9723), (37.374400000000001, -121.9723), (37.374299999999998, -121.9721), (37.374299999999998, -121.9721), (37.374099999999999, -121.97190000000001), (37.374099999999999, -121.97190000000001), (37.374099999999999, -121.9716), (37.374099999999999, -121.9716), (37.374200000000002, -121.9712), (37.374200000000002, -121.9712), (37.374299999999998, -121.9704), (37.374299999999998, -121.9704), (37.374299999999998, -121.96939999999999), (37.374299999999998, -121.96939999999999), (37.374200000000002, -121.96899999999999), (37.374200000000002, -121.96899999999999), (37.374099999999999, -121.9688), (37.374099999999999, -121.9688), (37.374000000000002, -121.9688), (37.374000000000002, -121.9688), (37.3735, -121.9688), (37.3735, -121.9688), (37.373399999999997, -121.9688), (37.373399999999997, -121.9688), (37.373399999999997, -121.9688), (37.373399999999997, -121.9688), (37.373600000000003, -121.9688), (37.373600000000003, -121.9688), (37.373800000000003, -121.9688), (37.373800000000003, -121.9688), (37.374000000000002, -121.9688), (37.374000000000002, -121.9688), (37.374400000000001, -121.9687), (37.374400000000001, -121.9687), (37.374699999999997, -121.9687), (37.374699999999997, -121.9687), (37.3748, -121.9687), (37.3748, -121.9687), (37.374899999999997, -121.9688), (37.374899999999997, -121.9688), (37.375300000000003, -121.9688), (37.375300000000003, -121.9688), (37.375599999999999, -121.9688), (37.375599999999999, -121.9688), (37.376300000000001, -121.9688), (37.376300000000001, -121.9688), (37.376999999999995, -121.9688), (37.376999999999995, -121.9688), (37.377499999999998, -121.9688), (37.377499999999998, -121.9688), (37.3782, -121.9688), (37.3782, -121.9688), (37.378700000000002, -121.9688), (37.378700000000002, -121.9688), (37.378900000000002, -121.9687), (37.378900000000002, -121.9687), (37.379199999999997, -121.9687), (37.379199999999997, -121.9687), (37.379800000000003, -121.9688), (37.379800000000003, -121.9688), (37.380000000000003, -121.9688), (37.380000000000003, -121.9688), (37.380299999999998, -121.9688), (37.380299999999998, -121.9688), (37.380899999999997, -121.9688), (37.380899999999997, -121.9688), (37.381700000000002, -121.9688), (37.381700000000002, -121.9688), (37.382300000000001, -121.9688), (37.382300000000001, -121.9688), (37.382599999999996, -121.9688), (37.382599999999996, -121.9688), (37.383099999999999, -121.9687), (37.383099999999999, -121.9687), (37.383200000000002, -121.9687), (37.383200000000002, -121.9687), (37.383499999999998, -121.9687), (37.383499999999998, -121.9687), (37.383899999999997, -121.9687), (37.383899999999997, -121.9687), (37.384099999999997, -121.9688), (37.384099999999997, -121.9688), (37.384599999999999, -121.9688), (37.384599999999999, -121.9688), (37.385100000000001, -121.9688), (37.385100000000001, -121.9688), (37.3857, -121.9689), (37.3857, -121.9689), (37.386200000000002, -121.96899999999999), (37.386200000000002, -121.96899999999999), (37.386699999999998, -121.96899999999999), (37.386699999999998, -121.96899999999999), (37.3874, -121.96899999999999), (37.3874, -121.96899999999999), (37.388000000000005, -121.9689), (37.388000000000005, -121.9689), (37.388500000000001, -121.9688), (37.388500000000001, -121.9688), (37.389099999999999, -121.9687), (37.389099999999999, -121.9687), (37.389499999999998, -121.9688), (37.389499999999998, -121.9688), (37.389899999999997, -121.9688), (37.389899999999997, -121.9688), (37.390300000000003, -121.9687), (37.390300000000003, -121.9687), (37.390500000000003, -121.9688), (37.390500000000003, -121.9688), (37.390599999999999, -121.9686), (37.390599999999999, -121.9686), (37.390799999999999, -121.96810000000001), (37.390799999999999, -121.96810000000001), (37.390999999999998, -121.9676), (37.390999999999998, -121.9676), (37.391300000000001, -121.96700000000001), (37.391300000000001, -121.96700000000001), (37.391599999999997, -121.9662), (37.391599999999997, -121.9662), (37.391999999999996, -121.9654), (37.391999999999996, -121.9654), (37.392499999999998, -121.96429999999999), (37.392499999999998, -121.96429999999999), (37.392800000000001, -121.9636), (37.392800000000001, -121.9636), (37.393000000000001, -121.96299999999999), (37.393000000000001, -121.96299999999999), (37.3934, -121.96210000000001), (37.3934, -121.96210000000001), (37.393799999999999, -121.96129999999999), (37.393799999999999, -121.96129999999999), (37.394199999999998, -121.96040000000001), (37.394199999999998, -121.96040000000001), (37.394500000000001, -121.95959999999999), (37.394500000000001, -121.95959999999999), (37.3947, -121.959), (37.3947, -121.959), (37.394799999999996, -121.9588), (37.394799999999996, -121.9588), (37.3949, -121.95869999999999), (37.3949, -121.95869999999999), (37.395000000000003, -121.9585), (37.395000000000003, -121.9585), (37.395099999999999, -121.95820000000001), (37.395099999999999, -121.95820000000001), (37.395299999999999, -121.9576), (37.395299999999999, -121.9576), (37.395400000000002, -121.9571), (37.395400000000002, -121.9571), (37.395699999999998, -121.9563), (37.395699999999998, -121.9563), (37.396099999999997, -121.9555), (37.396099999999997, -121.9555), (37.3964, -121.95480000000001), (37.3964, -121.95480000000001), (37.396500000000003, -121.9541), (37.396500000000003, -121.9541), (37.396500000000003, -121.9534), (37.396500000000003, -121.9534), (37.396299999999997, -121.9529), (37.396299999999997, -121.9529), (37.396099999999997, -121.9522), (37.396099999999997, -121.9522), (37.395800000000001, -121.9517), (37.395800000000001, -121.9517), (37.395400000000002, -121.95100000000001), (37.395400000000002, -121.95100000000001), (37.395099999999999, -121.95059999999999), (37.395099999999999, -121.95059999999999), (37.3949, -121.95050000000001), (37.3949, -121.95050000000001), (37.3949, -121.95059999999999), (37.3949, -121.95059999999999), (37.394799999999996, -121.9509), (37.394799999999996, -121.9509), (37.394599999999997, -121.95100000000001), (37.394599999999997, -121.95100000000001), (37.394399999999997, -121.9509), (37.394399999999997, -121.9509), (37.393900000000002, -121.95050000000001), (37.393900000000002, -121.95050000000001), (37.393799999999999, -121.95050000000001), (37.393799999999999, -121.95050000000001), (37.393599999999999, -121.95050000000001), (37.393599999999999, -121.95050000000001), (37.393500000000003, -121.95059999999999), (37.393500000000003, -121.95059999999999), (37.3932, -121.9511), (37.3932, -121.9511), (37.393099999999997, -121.9515), (37.393099999999997, -121.9515), (37.392899999999997, -121.9517), (37.392899999999997, -121.9517), (37.392899999999997, -121.9517), (37.392899999999997, -121.9517)]

def split_list_if_long(raw_lat_long):
    """
    google maps api will reject requests if they're too long.
    generator to check length of list and split up to do separate requests.

    :param raw_lat_long: list of tuples
    :return: shorter lists of tuples
    """

    if len(raw_lat_long) > 100:
        for x in xrange(0,len(raw_lat_long),100):
            chunk = raw_lat_long[x:x+100]
            yield chunk


def collapse_to_unique_points(chunk):
    """ Remove adjacent duplicate points, since that will be faster and won't affect the path.

    :param raw_lat_long: list of tuples
    :return: points: shorter list of tuples
    """
    points = []
    for pair in chunk:
        if len(points)==0 or pair != points[-1]:  #compare to element most recently appended to points
            points.append(pair)
    print len(points)
    return points


def convert_to_path(points):
    """
    Reformat list of latitude and longitude values into string separated by pipe symbols.

    >>> convert_to_path([(37,-121), (37,-121)])
    '37,-121|37,-121'
    >>> convert_to_path([(37.3932, -121.9513), (37.3932, -121.9512), (37.393500000000003, -121.95059999999999)])
    '37.3932,-121.9513|37.3932,-121.9512|37.3935,-121.9506'

    :param points: list of tuples
    :return: path as string of tuples separated by pipe symbols (no spaces)
    """
    samples = str(len(points))

    pathStr=""
    pathStr+= '{0},{1}|'.format(points[0][0],points[0][1]) # does first item need open quotes?

    for item in range(1,(len(points)-1)):
        pathStr += "{0},{1}|".format(points[item][0], points[item][1])

    pathStr += '{0},{1}'.format(points[-1][0],points[-1][1]) #get last item and do you need to close quotes?

    #print pathStr
    print len(pathStr)

    return pathStr, samples

def check_distances(lat1,long1,lat2,long2):
    """
    modified from http://www.johndcook.com/blog/python_longitude_latitude/

    to do: apply this to check for points that are very close together, to further shorten the request list

    :param points: list of tuples
    :return: list of distances

    >>>check_distances(37.3932, -121.9513, 37.3932, -121.9512)
    8.837368757855673

    >>>check_distances(37.3932, -121.9512,37.393500000000003, -121.95059999999999)
    62.64861413446365

    >>>check_distances(37.393500000000003, -121.95059999999999,37.393599999999999, -121.9504)
    20.882823394147213
    """
    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0

    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians

    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians

    # Compute spherical distance from spherical coordinates.

    # For two locations in spherical coordinates
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) =
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length

    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth
    # in your favorite set of units to get length.
    # I'm using km conversion * 1000: this should return meters
    arc = arc*6373000

    return arc

def getElevation(path="36.578581,-118.291994|36.23998,-116.83171",samples="2",sensor="false", **elvtn_args):
    elvtn_args.update({
        'path': path,
        'samples': samples,
        'sensor': sensor
    })

    url = ELEVATION_BASE_URL + '?' + urllib.urlencode(elvtn_args)
    #print elvtn_args
    #print url
    #print urllib.urlopen(url)

    response = simplejson.load(urllib.urlopen(url))
    #print response

    # Create a dictionary for each results[] object
    elevationArray = []

    for resultset in response['results']:
      elevationArray.append(resultset['elevation'])

    print elevationArray
    #
    # # Create the chart passing the array of elevation data
    # getChart(chartData=elevationArray)

if __name__ == '__main__':
        
    print("")
    print("Elevation Chart Maker 1.0")
    print("")
    print("The following service calculates elevation data between two points")
    print("and builds an HTTP chart using Google's Elevation service and Chart API")
    print("")

    # Collect the Latitude/Longitude input string
    # from the user
    # startStr = raw_input('Enter the start latitude,longitude value (default Mt. Whitney) --> ').replace(' ','')
    # if not startStr:
    #   startStr = "36.578581,-118.291994"
    #
    # endStr = raw_input('Enter the end latitude,longitude value (default Death Valley) --> ').replace(' ','')
    # if not endStr:
    #   endStr = "36.23998,-116.83171"
    #
    # pathStr = startStr + "|" + endStr
    #
    # getElevation(pathStr)


    chunk = split_list_if_long(raw_lat_long)

    while chunk:
        try:
            points = collapse_to_unique_points(next(chunk))
            pathStr, samples = convert_to_path(points)
            getElevation(pathStr, samples)
        except StopIteration:
            break


