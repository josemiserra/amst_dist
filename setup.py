from setuptools import setup, find_packages,Distribution

class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True

setup(
   name='amst_bin_win',
   version='0.1.1',
   author='Julian Hennies',
   author_email='julian.hennies@embl.de',
   packages= find_packages(),
   scripts=[],
   url='https://github.com/jhennies/amst',
   license='LICENSE.txt',
   description='AMST wheel for Windows',
   package_data={
        'amst': ['ANNlib-5.0.dll','elastix.exe','transformix.exe'],
    },
    distclass=BinaryDistribution,
   long_description=open('README.md',encoding="utf8").read(),
   install_requires=[
       "numpy >= 1.17",
       "scikit-image >=0.15" ,
       "tifffile",
       "silx",
       "pyopencl"
   ],
   python_requires='>=3.6'
)