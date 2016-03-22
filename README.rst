pcf_bex
========================

Installation
------------

Install the PWS CLI (https://docs.run.pivotal.io/starting/), configure your credentials then::

   $ git clone https://github.com/boundlessgeo/pcf_bex.git
   $ cd pcf_bex
Initial push
   $ cf push -c "bash ./init_db.sh"
Additional pushes
   $ cf push
