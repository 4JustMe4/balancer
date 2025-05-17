#!/bin/sh

set -xue

APP=${1}
VERSION=${2}

DIST_TMP="/home/mikhnenko/tmp/"
VERSION_DIR="/home/boincadm/projects/myboinc/apps/${APP}/${VERSION}/x86_64-pc-linux-gnu"

scp ../tasks/dtransversal/bin/DTransversal boinc-server:${DIST_TMP}
scp ../tasks/transversal/bin/Transversal boinc-server:${DIST_TMP}


ssh boinc-server "sudo mkdir -p ${VERSION_DIR}"
ssh boinc-server "sudo chmod 777 ${VERSION_DIR}"
ssh boinc-server "sudo cp ${DIST_TMP}/${APP} ${VERSION_DIR}/${APP}_${VERSION}"
cat > version.xml <<EOF
<version>
    <file>
        <physical_name>${APP}_${VERSION}</physical_name>
        <main_program/>
    </file>
</version>
EOF

scp version.xml boinc-server:${DIST_TMP}
ssh boinc-server "sudo cp ${DIST_TMP}/version.xml ${VERSION_DIR}"