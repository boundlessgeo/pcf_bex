Pcf_Geonode
========================

Installation
------------

Install the PWS CLI (https://docs.run.pivotal.io/starting/), configure your credentials then::

   $ git clone https://github.com/terranodo/pcf_geonode.git
   $ cd pcf_geonode
Initial push
   $ cf push -c "bash ./init_db.sh"
Additional pushes
   $ cf push
