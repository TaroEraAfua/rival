#!/bin/bash

IMG_PATH="../src/frontend/src/components/common/images/logo.png"
DIR_PATH="../src/backend/storage/images/test"
DIR_PATH2="../src/backend/storage/images/aaa"
echo start insert sql
for row in `ls ./sql/*.sql`; do
  echo ${row}
  eval mysql -u root -proot rival < ${row}
done
echo end insert sql
COUNT=1

