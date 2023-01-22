from distutils.core import setup
setup(
  name = 'Topsis_102003274',         
  packages = ['Topsis_102003274'],  
  version = '0.1',
  license='MIT',
  description = 'Calculating Topsis score and saving it in a csv file',
  author = 'Raghav Aggarwal',                   
  author_email = 'rghaggarwal2002@gmail.com',     
  url = 'https://github.com/anirudhchadha02/TOPSIS-102003658.git',
  download_url = '',
  keywords = ['TOPSISSCORE', 'RANK', 'DATAFRAME'],
  install_requires=[
          'numpy',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)