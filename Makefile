OUT_FILE?=./notifications.zip
DELIVERABLE=$(abspath $(OUT_FILE))

install:
	pipenv install --three

clean:
	pipenv clean
	rm -f ${DELIVERABLE}

package:
	$(eval VENV = $(shell pipenv --venv))
	cd ${VENV}/lib/python3.7/site-packages && zip -r9 ${DELIVERABLE} ./*
	zip -r9 ${DELIVERABLE} whichbins
	zip -r9j ${DELIVERABLE} bins.json

deploy:
	aws s3 cp ${DELIVERABLE} s3://cg-notification-artifacts/deploy.zip
	aws lambda update-function-code \
      --function-name notifications-lambda \
      --s3-bucket cg-notification-artifacts \
      --s3-key deploy.zip --region eu-west-1