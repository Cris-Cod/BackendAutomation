run with allure report:
behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReports

generate allure report: allure serve + "report folder"

run all features: behave --no-capture

run specify feature: behave features/github.feature --no-capture

