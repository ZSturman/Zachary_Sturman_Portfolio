def portfolio_context_processor(config):
    dev_test = config.DEV_TEST
    dev_status = config.DEV_STATUS
    return {'dev_test': dev_test, 'dev_status':dev_status}