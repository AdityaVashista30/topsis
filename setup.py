# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:27:12 2020

@author: Aditya Vashista (101703039,TIET)
"""

from distutils.core import setup
setup(
  name = 'topsis',        
  packages = ['topsis'],   
  version = '0.1',      
  license='MIT',        
  description = 'Topsis package to find the best option among given products depending upon their features and weightage of each feature for product selection',   
  author = 'Aditya Vashista, 10703039',              
  author_email = 'aditya.vashista30@gmail.com',      
  url = 'https://github.com/AdityaVashista30/topsis',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    
  keywords = ['command-line', 'Best Option', 'Topsi','Product selection'],
  install_requires=[            
          'pandas',
          'sys',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)