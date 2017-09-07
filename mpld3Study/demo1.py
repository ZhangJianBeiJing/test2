# coding=utf-8
'''
The mpld3 project brings together Matplotlib,
the popular Python-based graphing library,
and D3js, the popular JavaScript library for creating interactive data visualizations for the web.
The result is a simple API for exporting your matplotlib graphics to HTML code which can be used within the browser, within standard web pages, blogs, or tools such as the IPython notebook.
'''

import matplotlib.pyplot as plt, mpld3
plt.plot([3,1,4,1,5], 'ks-', mec='w', mew=5, ms=20)
mpld3.show()