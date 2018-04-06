from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

#https://python-packaging.readthedocs.io/en/latest/
setup(name='chat4nltk',
      version='0.1a',
      description='Chabot extensions for NLTK',
      long_description=readme(),
#      classifiers=[
#        'Development Status :: 3 - Alpha',
#        'License :: OSI Approved :: MIT License',
#        'Programming Language :: Python :: 2.7',
#        'Topic :: Text Processing :: Linguistic',
#      ],
#      keywords='funniest joke comedy flying circus',
#      url='http://github.com/storborg/funniest',
      author='FSMarcondes',
      license='MIT',
      scripts=['bin/chatto'],
      packages=['chat4nltk', 'chat4nltk.lib', 'chat4nltk.data'],
      install_requires=[
          'nltk',
      ],
      include_package_data=True, #declarar no Manifesto
      zip_safe=False)
