import yaml

global hparams

def set_hparams(config_yaml_path: str) -> dict:
    with open(config_yaml_path, encoding='UTF-8') as f:
        hparams = yaml.load(f, Loader=yaml.FullLoader)
    print('loaded config.yaml...')
