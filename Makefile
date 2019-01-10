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
	zip -r9 ${DELIVERABLE} notifications

deploy:
	aws s3 cp ${DELIVERABLE} s3://cg-notifications-artifacts/deploy.zip
	aws lambda update-function-code \
      --function-name notifications-lambda \
      --s3-bucket cg-notifications-artifacts \
      --s3-key deploy.zip --region eu-west-1