from setuptools import setup

package_name = 'zundam_orne2'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ryusei Baba',
    maintainer_email='babaryusei.kw@gmail.com',
    description='VOICEVOX ROS 2',
    license='BSD 3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'zundam_orne2_node = zundam_orne2.zundam_orne2_node:main'
        ],
    },
)
