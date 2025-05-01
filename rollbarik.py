import rollbar

rollbar.init(
    access_token='8f5f4d0522a6451c8fc5d832a798d890',
    environment='testenv',
    code_version='1.0'
)
rollbar.report_message('Rollbar is configured correctly', 'info')