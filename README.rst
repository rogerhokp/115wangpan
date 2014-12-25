115 Wangpan
===========

|Build| |PyPI version|

115 Wangpan  is an unofficial Python API for 115.com, mainly pertinent to its "lixian" (offline) features. Currently, only limited features have been implemented. Supported Python verisons are 2.6, 2.7 and 3.3.

* Documentation: http://115wangpan.readthedocs.org
* GitHub: https://github.com/shichao-an/115wangpan
* PyPI: https://pypi.python.org/pypi/115wangpan/


Features
--------

* Authentication
* Tasks management (BitTorrent currently supported)
* File management

Installation
------------
Install dependencies before installing the python package:

Ubuntu

.. code-block:: bash

    $ sudo apt-get install libcurl4-openssl-dev python-dev

Fedora

.. code-block:: bash

    $ sudo yum groupinstall "Development Tools"
    $ sudo yum install libcurl libcurl-devel python-devel


Then, you can install with pip:

.. code-block:: bash

    $ pip install 115wangpan

Usage
-----
.. code-block:: python

    >>> import u115
    >>> api = u115.API()
    >>> api.login('username@example.com', 'password')
    True
    >>> tasks = api.get_tasks()
    >>> task = tasks[0]
    >>> print task.name
    episode of side-A
    >>> print task.status_human
    TRANSFERRED
    >>> print task.size_human
    1.6 GiB
    >>> files = task.list()
    >>> files
    [<File: ep8 xxx.mkv>]
    >>> f = files[0]
    >>> f.get_download_url()
    u'http://cdnuni.115.com/some-very-long-url.mkv'
    >>> f.directory
    <Directory: episode of side-A>
    >>> f.directory.parent
    <Directory: offline download>


Helpers
-------

* `115wangpan-dl <https://gist.github.com/shichao-an/129969edca4fc1282296>`_: file download script
* `115wangpan-up <https://gist.github.com/shichao-an/fa09286436d6f7118b97>`_: torrent upload script


.. |Build| image:: https://api.travis-ci.org/shichao-an/115wangpan.png?branch=master
   :target: http://travis-ci.org/shichao-an/115wangpan
.. |PyPI version| image:: https://pypip.in/v/115wangpan/badge.png
   :target: https://pypi.python.org/pypi/115wangpan/
