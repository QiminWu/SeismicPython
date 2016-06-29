from distutils.core import setup, Extension
import os
import sys

#Initialize the setup kwargs that are independent of Antelope
kwargs = {'name': 'seispy',
          'version': '0.0alpha',
          'author': 'Malcolm White',
          'author_email': 'malcolcw@usc.edu',
          'maintainer': 'Malcolm White',
          'maintainer_email': 'malcolcw@usc.edu',
          'url': 'http://malcolmw.github.io/SeismicPython/',
          'description': 'Seismic data analysis tools',
          'download_url': 'https://github.com/malcolmw/SeismicPython',
          'platforms': ['linux'],
          'requires': ['obspy'],
          'py_modules': ['seispy.core',
                       'seispy.util'],
          'scripts': ['scripts/tests/test_arrival',
                    'scripts/tests/test_origin',
                    'scripts/tests/test_station',
                    'scripts/tests/test_trace',
                    'scripts/tests/test_database']}
#If $ANTELOPE environment variable is not initialized, install only the
#portions of the distribution that will operate independently of
#Antelope
try:
    antelope_dir = os.environ['ANTELOPE']
except KeyError:
    print "INFO:: $ANTELOPE environment variable not detected."
    print "INFO:: Installing Antelope independent components only."
    kwargs['packages'] = ['seispy']
    kwargs['package_dir'] = {'seispy': 'seispy'}
    kwargs['package_data'] = {'seispy': ['data/schemas/*']}
    setup(**kwargs)
    exit()

#If $ANTELOPE environment variable is initialized, install the portions
#the distribution that depend on Antelope
print "INFO:: $ANTELOPE environment variable detected (%s)" % antelope_dir
print "INFO:: Installing all components."
kwargs['packages'] = ['seispy', 'gazelle']
kwargs['package_dir'] = {'seispy': 'seispy',
                         'gazelle': 'gazelle'}
kwargs['package_data'] = {'seispy': ['data/schemas/*',
                                     'data/demodb/db/*',
                                     'data/demodb/dbmaster/*',
                                     'data/demodb/wfs/*']}
kwargs['ext_modules'] = [Extension("gazelle.response",
                                   ["gazelle/responsemodule/responsemodule.c"],
                                   include_dirs=["%s/include" % antelope_dir],
                                   libraries=['coords',
                                              'alk',
                                              #'banner',
                                              'stock',
                                              'deviants',
                                              'brttpool',
                                              'response'],
                                   library_dirs=['%s/lib' % antelope_dir])]
setup(**kwargs)

