from setuptools import setup, find_packages

setup(
    name='dog_motion_detector',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.8',
    install_requires=[
        'opencv-python>=4.5.3',
        'numpy>=1.21.1'
    ],
    entry_points={
        'console_scripts': [
            'run_detector=src.dog_motion.detector:main'
        ]
    }
)
